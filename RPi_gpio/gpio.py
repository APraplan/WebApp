import sys
import platform

if platform.system() == 'Windows':
    import fake_rpi
    sys.modules['RPi'] = fake_rpi.RPi
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

OUTPUTPIN = [2,3]

for pin in OUTPUTPIN:
    GPIO.setup(pin, GPIO.OUT)
    
def handleRequestGPIO(actionID):
    id = int(actionID[3])
    print('button id :', id)
    
    if actionID[-2:] == 'on':
        GPIO.output(id, GPIO.HIGH)
    else:        
        GPIO.output(id, GPIO.LOW)
    