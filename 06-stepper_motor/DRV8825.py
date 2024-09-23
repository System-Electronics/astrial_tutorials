import gpiod
from gpiod.line import Direction, Value
import time


MotorDir = [
    'forward',
    'backward',
]

ControlMode = [
    'hardward',
    'softward',
]

gpio_dict = {
    0: (2, 20),
    1: (2, 19),
    2: (2, 25),
    3: (2, 21),
    4: (1, 8),
    5: (1, 9),
    6: (3, 27),
    7: (3, 26),
    8: (4, 9),
    9: (4, 8),
    10: (4, 7),
    11: (4, 6),
    12: (4, 2),
    13: (4, 5),
    16: (3, 24),
    17: (3, 23),
    18: (4, 13),
    19: (4, 12),
    20: (4, 11),
    21: (4, 10),
    22: (1, 0),
    23: (1, 1),
    24: (1, 2),
    25: (1, 3),
    26: (1, 4),
    27: (1, 5),
}


class DRV8825():
    def __init__(self, dir_pin, step_pin, enable_pin, mode_pins):
        self.dir_pin = dir_pin
        self.step_pin = step_pin        
        self.enable_pin = enable_pin
        self.mode_pins = mode_pins

        configs = [{}, {}, {}, {}]
        self.requests = [None, None, None, None]

        dir_pin_chip_idx = gpio_dict[dir_pin][0]
        dir_pin_line = gpio_dict[dir_pin][1]

        step_pin_chip_idx = gpio_dict[step_pin][0]
        step_pin_line = gpio_dict[step_pin][1]

        enable_pin_chip_idx = gpio_dict[enable_pin][0]
        enable_pin_line = gpio_dict[enable_pin][1]

        mode_pins_chip_idx = [gpio_dict[mode_pins[0]][0], gpio_dict[mode_pins[1]][0], gpio_dict[mode_pins[2]][0]]
        mode_pins_line = [gpio_dict[mode_pins[0]][1], gpio_dict[mode_pins[1]][1], gpio_dict[mode_pins[2]][1]]
        

        # Define configuration for the GPIO lines
        configs[dir_pin_chip_idx-1][dir_pin_line] = gpiod.LineSettings(
            direction=Direction.OUTPUT, output_value=Value.INACTIVE
        )
        configs[step_pin_chip_idx-1][step_pin_line] = gpiod.LineSettings(
            direction=Direction.OUTPUT, output_value=Value.INACTIVE
        )
        configs[enable_pin_chip_idx-1][enable_pin_line] = gpiod.LineSettings(
            direction=Direction.OUTPUT, output_value=Value.INACTIVE
        )
        for i in range(3):
            configs[mode_pins_chip_idx[i]-1][mode_pins_line[i]] = gpiod.LineSettings(
                direction=Direction.OUTPUT, output_value=Value.INACTIVE
            )
        
        # Request control over the GPIO lines with initial settings
        for i in range(4):
            if configs[i]:
                self.requests[i] = gpiod.request_lines(
                    f'/dev/gpiochip{i+1}',
                    consumer="stepper-motor-example",
                    config=configs[i],
                )

        
    def digital_write(self, pin, value):
        if isinstance(pin, int):
            chip_idx = gpio_dict[pin][0]
            line = gpio_dict[pin][1]
            self.requests[chip_idx-1].set_value(line, Value.ACTIVE if value else Value.INACTIVE)
        else:
            for i in range(len(pin)):
                chip_idx = gpio_dict[pin[i]][0]
                line = gpio_dict[pin[i]][1]
                self.requests[chip_idx-1].set_value(line, Value.ACTIVE if value[i] else Value.INACTIVE)
        
    def Stop(self):
        self.digital_write(self.enable_pin, 0)
    
    def SetMicroStep(self, mode, stepformat):
        """
        (1) mode
            'hardward' :    Use the switch on the module to control the microstep
            'software' :    Use software to control microstep pin levels
                Need to put the All switch to 0
        (2) stepformat
            ('fullstep', 'halfstep', '1/4step', '1/8step', '1/16step', '1/32step')
        """
        microstep = {'fullstep': (0, 0, 0),
                     'halfstep': (1, 0, 0),
                     '1/4step': (0, 1, 0),
                     '1/8step': (1, 1, 0),
                     '1/16step': (0, 0, 1),
                     '1/32step': (1, 0, 1)}

        print ("Control mode:", mode)
        if (mode == ControlMode[1]):
            print ("set pins")
            self.digital_write(self.mode_pins, microstep[stepformat])
        
    def TurnStep(self, Dir, steps, stepdelay=0.005):
        if (Dir == MotorDir[0]):
            print ("forward")
            self.digital_write(self.enable_pin, 1)
            self.digital_write(self.dir_pin, 0)
        elif (Dir == MotorDir[1]):
            print ("backward")
            self.digital_write(self.enable_pin, 1)
            self.digital_write(self.dir_pin, 1)
        else:
            print ("the dir must be : 'forward' or 'backward'")
            self.digital_write(self.enable_pin, 0)
            return

        if (steps == 0):
            return
            
        print ("turn step:",steps)
        for i in range(steps):
            self.digital_write(self.step_pin, True)
            time.sleep(stepdelay)
            self.digital_write(self.step_pin, False)
            time.sleep(stepdelay)
