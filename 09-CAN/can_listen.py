# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

from can_lib.canio import Timer
from can_lib.canio import RemoteTransmissionRequest, Message
from can_lib import MCP2515 as CAN

mcp = CAN(baudrate=125000)

t = Timer(timeout=5)
next_message = None
message_num = 0
while True:
    # print occationally to show we're alive
    if t.expired:
        print(".", end="")
        t.rewind_to(1)
    with mcp.listen(timeout=1.0) as listener:
        message_count = listener.in_waiting()

        if message_count == 0:
            continue

        next_message = listener.receive()
        message_num = 0
        while not next_message is None:
            message_num += 1

            msg = next_message
            print("ID:", hex(msg.id), end=",")
            if isinstance(msg, Message):
                if len(msg.data) > 0:
                    print("Data:", end="")
                    message_str = ",".join(["0x{:02X}".format(i) for i in msg.data])
                    print(message_str)

            if isinstance(msg, RemoteTransmissionRequest):
                print("RTR_LEN:", msg.length)
            next_message = listener.receive()