import RPi.GPIO as GPIO
import time
import  numpy as np
GPIO.setmode(GPIO.BOARD)
pins = [8,10,38,40]

global p0, p1, p2, p3
fc = 50

def setup():
    global p0, p1, p2, p3
    for each in pins:
        GPIO.setup(each, GPIO.OUT)

    p0 = GPIO.PWM(pins[0], fc )
    p1 = GPIO.PWM(pins[1], fc)
    p2 = GPIO.PWM(pins[2], fc)
    p3 = GPIO.PWM(pins[3], fc)
    p0.start(0)
    p1.start(0)
    p2.start(0)
    p3.start(0)

def stop():
   GPIO.output(pins, [False]*len(pins))

def pwm(dc):
    p1.ChangeDutyCycle(dc)
    p3.ChangeDutyCycle(dc)

def move(left_ratio, right_ratio, up_ratio, down_ratio):
    left = np.array([0,1,0,1]) * left_ratio
    right = np.array([1,0,1,0]) * right_ratio
    up = np.array([0,1,1,0]) * up_ratio
    down = np.array([1,0,0,1]) * down_ratio

    dc_vec = (left + right + up + down) * 100
    p0.ChangeDutyCycle(max(0, min(100, dc_vec[0])))
    p1.ChangeDutyCycle(max(0, min(100, dc_vec[1])))
    p2.ChangeDutyCycle(max(0, min(100, dc_vec[2])))
    p3.ChangeDutyCycle(max(0, min(100, dc_vec[3])))

setup()

