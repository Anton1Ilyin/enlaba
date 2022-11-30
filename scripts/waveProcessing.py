import waveFunctions as b
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac=[26, 19,13,6,5,11,9,10]
leds=[21,20,16,12,7,8,25,24]
GPIO.setup(dac ,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(leds,GPIO.OUT)
comp=4
troyka=17
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
def adc():
    value=0
    for i in range(7, -1, -1):
        value+=2**i
        a=d2b(value)
        GPIO.output(dac,a)
        time.sleep(0.0007)
        if GPIO.input(comp)==0:
            value-=2**i
    return value


b.initSpiAdc()
result = []

b.waitForOpen()

door_open = time.time()

finish = door_open + 15

while time.time() < finish:
    result.append(adc())

b.save(result, door_open, finish)

b.deinitSpiAdc()
GPIO.LOW
GPIO.cleanup()

