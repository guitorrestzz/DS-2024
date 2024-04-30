import machine 
import time

ledRed = machine.Pin(15, machine.Pin.OUT)
ledYellow = machine.Pin(14, machine.Pin.OUT)
ledGreen = machine.Pin(27, machine.Pin.OUT)

while True:
    ledGreen.value(1)
    time.sleep(3)
    ledGreen.value(0)
    ledYellow.value(1)
    time.sleep(1)
    ledYellow.value(0)
    ledRed.value(1)
    time.sleep(5)
    ledRed.value(0)
