__author__ = 'adol'
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
## 超声测距模块
Trig=35
ECHO=37

GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
def distance():
    GPIO.output(Trig, True)
    time.sleep(0.00001)
    GPIO.output(Trig, False)

    while GPIO.input(ECHO) == 0:
        pass
    pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pass

    pulse_end = time.time()

    dist = (pulse_end- pulse_start) * 17150
    print("Distance: {0:.2} cm".format(dist))
    return dist

if __name__ == '__main__':
    try:
        while True:
            distance()
            time.sleep(2)
    except :
        GPIO.cleanup()

