# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
from can_lib.canio import Message, RemoteTransmissionRequest
from can_lib import MCP2515 as CAN
import time
NODE_ID = 0x12

can_bus = CAN(baudrate=125000)
while True:
   message = Message(id=NODE_ID, data=b'Hello', extended=True)
   send_success = can_bus.send(message)
   time.sleep(1)
