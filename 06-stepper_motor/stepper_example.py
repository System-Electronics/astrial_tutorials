import time
from DRV8825 import DRV8825 # Stepper motor driver

try:
    # Initialize Motor1 and Motor2 with specified GPIO pins for direction, step, enable, and mode
    Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
    Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))
    
    # Set the microstepping mode of Motor1 to full step using software control
    Motor1.SetMicroStep('softward', 'fullstep')
    # Turn Motor1 forward for 400 steps with a delay of 0.002 seconds per step
    Motor1.TurnStep(Dir='forward', steps=400, stepdelay=0.002)
    # Wait for 0.5 seconds
    time.sleep(0.5)
    # Turn Motor1 backward for 400 steps with a delay of 0.002 seconds per step
    Motor1.TurnStep(Dir='backward', steps=400, stepdelay=0.002)
    # Stop Motor1
    Motor1.Stop()

    # Set the microstepping mode of Motor2 to half step using hardware control
    Motor2.SetMicroStep('hardward', 'halfstep')
    # Turn Motor2 forward for 400 steps with a delay of 0.002 seconds per step
    Motor2.TurnStep(Dir='forward', steps=400, stepdelay=0.002)
    # Wait for 0.5 seconds
    time.sleep(0.5)
    # Turn Motor2 backward for 400 steps with a delay of 0.002 seconds per step
    Motor2.TurnStep(Dir='backward', steps=400, stepdelay=0.002)
    # Stop Motor2
    Motor2.Stop()

    # Ensure both motors are stopped at the end
    Motor1.Stop()
    Motor2.Stop()
    
except:
    print("\nMotor stop")
    Motor1.Stop()
    Motor2.Stop()
    exit()
