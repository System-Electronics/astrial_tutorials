from __future__ import (
    unicode_literals,
    absolute_import,
    print_function,
    division,
    )
native_str = str
str = type('')

import io
import os
import glob
import errno
import struct
import select
import inspect
from functools import wraps
from collections import namedtuple
from threading import Thread, Event
from smbus2 import SMBus


DIRECTION_UP     = 'up'
DIRECTION_DOWN   = 'down'
DIRECTION_LEFT   = 'left'
DIRECTION_RIGHT  = 'right'
DIRECTION_MIDDLE = 'middle'

ACTION_PRESSED  = 'pressed'
ACTION_RELEASED = 'released'
ACTION_HELD     = 'held'

LED_MATRIX_I2C_ADDR = 0x46


InputEvent = namedtuple('InputEvent', ('timestamp', 'direction', 'action'))


class SenseStick(object):
    """
    Represents the joystick on the Sense HAT.
    """
    SENSE_HAT_EVDEV_NAME = 'Raspberry Pi Sense HAT Joystick'
    EVENT_FORMAT = native_str('llHHI')
    EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

    EV_KEY = 0x01

    STATE_RELEASE = 0
    STATE_PRESS = 1
    STATE_HOLD = 2

    KEY_UP = 2
    KEY_LEFT = 4
    KEY_RIGHT = 1
    KEY_DOWN = 16
    KEY_ENTER = 8

    last_state = STATE_RELEASE
    last_code = 0

    def __init__(self):
        self._callbacks = {}
        self._callback_thread = None
        self._callback_event = Event()
        self._bus = SMBus(4) # Initialize the I2C bus

    def close(self):
        self._bus.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()

    def _read(self):
        """
        Reads a single event from the joystick, blocking until one is
        available. Returns `None` if a non-key event was read, or an
        `InputEvent` tuple describing the event otherwise.
        """
        data = self._bus.read_i2c_block_data(LED_MATRIX_I2C_ADDR, 242, 1)
        code = data[0]

        if (code == 0 and self.last_state == self.STATE_RELEASE):
            return None
        
        if (code == 0):
            code = self.last_code
            value = self.STATE_RELEASE
        else:
            if (code != self.KEY_ENTER):
                code = code & 0x17 # bit-wise logical AND to remove the ENTER event

            if (self.last_state == self.STATE_RELEASE):
                value = self.STATE_PRESS
            else:
                value = self.STATE_HOLD

            self.last_code = code
        
        self.last_state = value
        
        
        
        return InputEvent(
            timestamp=0,
            direction={
                self.KEY_UP:    DIRECTION_UP,
                self.KEY_DOWN:  DIRECTION_DOWN,
                self.KEY_LEFT:  DIRECTION_LEFT,
                self.KEY_RIGHT: DIRECTION_RIGHT,
                self.KEY_ENTER: DIRECTION_MIDDLE,
                }[code],
            action={
                self.STATE_PRESS:   ACTION_PRESSED,
                self.STATE_RELEASE: ACTION_RELEASED,
                self.STATE_HOLD:    ACTION_HELD,
                }[value])
        
        

    def _wait(self, timeout=None):
        """
        Waits *timeout* seconds until an event is available from the
        joystick. Returns `True` if an event became available, and `False`
        if the timeout expired.
        """
        return True

    def _wrap_callback(self, fn):
        # Shamelessley nicked (with some variation) from GPIO Zero :)
        @wraps(fn)
        def wrapper(event):
            return fn()

        if fn is None:
            return None
        elif not callable(fn):
            raise ValueError('value must be None or a callable')
        elif inspect.isbuiltin(fn):
            # We can't introspect the prototype of builtins. In this case we
            # assume that the builtin has no (mandatory) parameters; this is
            # the most reasonable assumption on the basis that pre-existing
            # builtins have no knowledge of InputEvent, and the sole parameter
            # we would pass is an InputEvent
            return wrapper
        else:
            # Try binding ourselves to the argspec of the provided callable.
            # If this works, assume the function is capable of accepting no
            # parameters and that we have to wrap it to ignore the event
            # parameter
            try:
                inspect.getcallargs(fn)
                return wrapper
            except TypeError:
                try:
                    # If the above fails, try binding with a single tuple
                    # parameter. If this works, return the callback as is
                    inspect.getcallargs(fn, ())
                    return fn
                except TypeError:
                    raise ValueError(
                        'value must be a callable which accepts up to one '
                        'mandatory parameter')

    def _start_stop_thread(self):
        if self._callbacks and not self._callback_thread:
            self._callback_event.clear()
            self._callback_thread = Thread(target=self._callback_run)
            self._callback_thread.daemon = True
            self._callback_thread.start()
        elif not self._callbacks and self._callback_thread:
            self._callback_event.set()
            self._callback_thread.join()
            self._callback_thread = None

    def _callback_run(self):
        while not self._callback_event.wait(0):
            event = self._read()
            if event:
                callback = self._callbacks.get(event.direction)
                if callback:
                    callback(event)
                callback = self._callbacks.get('*')
                if callback:
                    callback(event)

    def wait_for_event(self, emptybuffer=False):
        """
        Waits until a joystick event becomes available.  Returns the event, as
        an `InputEvent` tuple.

        If *emptybuffer* is `True` (it defaults to `False`), any pending
        events will be thrown away first. This is most useful if you are only
        interested in "pressed" events.
        """
        if emptybuffer:
            while self._wait(0):
                self._read()
        while self._wait():
            event = self._read()
            if event:
                return event

    def get_events(self):
        """
        Returns a list of all joystick events that have occurred since the last
        call to `get_events`. The list contains events in the order that they
        occurred. If no events have occurred in the intervening time, the
        result is an empty list.
        """
        result = []
        while self._wait(0):
            event = self._read()
            if event:
                result.append(event)
        return result

    @property
    def direction_up(self):
        """
        The function to be called when the joystick is pushed up. The function
        can either take a parameter which will be the `InputEvent` tuple that
        has occurred, or the function can take no parameters at all.
        """
        return self._callbacks.get(DIRECTION_UP)

    @direction_up.setter
    def direction_up(self, value):
        self._callbacks[DIRECTION_UP] = self._wrap_callback(value)
        self._start_stop_thread()

    @property
    def direction_down(self):
        """
        The function to be called when the joystick is pushed down. The
        function can either take a parameter which will be the `InputEvent`
        tuple that has occurred, or the function can take no parameters at all.

        Assign `None` to prevent this event from being fired.
        """
        return self._callbacks.get(DIRECTION_DOWN)

    @direction_down.setter
    def direction_down(self, value):
        self._callbacks[DIRECTION_DOWN] = self._wrap_callback(value)
        self._start_stop_thread()

    @property
    def direction_left(self):
        """
        The function to be called when the joystick is pushed left. The
        function can either take a parameter which will be the `InputEvent`
        tuple that has occurred, or the function can take no parameters at all.

        Assign `None` to prevent this event from being fired.
        """
        return self._callbacks.get(DIRECTION_LEFT)

    @direction_left.setter
    def direction_left(self, value):
        self._callbacks[DIRECTION_LEFT] = self._wrap_callback(value)
        self._start_stop_thread()

    @property
    def direction_right(self):
        """
        The function to be called when the joystick is pushed right. The
        function can either take a parameter which will be the `InputEvent`
        tuple that has occurred, or the function can take no parameters at all.

        Assign `None` to prevent this event from being fired.
        """
        return self._callbacks.get(DIRECTION_RIGHT)

    @direction_right.setter
    def direction_right(self, value):
        self._callbacks[DIRECTION_RIGHT] = self._wrap_callback(value)
        self._start_stop_thread()

    @property
    def direction_middle(self):
        """
        The function to be called when the joystick middle click is pressed. The
        function can either take a parameter which will be the `InputEvent` tuple
        that has occurred, or the function can take no parameters at all.

        Assign `None` to prevent this event from being fired.
        """
        return self._callbacks.get(DIRECTION_MIDDLE)

    @direction_middle.setter
    def direction_middle(self, value):
        self._callbacks[DIRECTION_MIDDLE] = self._wrap_callback(value)
        self._start_stop_thread()

    @property
    def direction_any(self):
        """
        The function to be called when the joystick is used. The function
        can either take a parameter which will be the `InputEvent` tuple that
        has occurred, or the function can take no parameters at all.

        This event will always be called *after* events associated with a
        specific action. Assign `None` to prevent this event from being fired.
        """
        return self._callbacks.get('*')

    @direction_any.setter
    def direction_any(self, value):
        self._callbacks['*'] = self._wrap_callback(value)
        self._start_stop_thread()

