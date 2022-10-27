import RPi.GPIO as GPIO
import time
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

def go(vec):
   print('car go()')
   GPIO.output(pins, vec)
   #time.sleep(t)
def try_vec():
    vec=[0,0,0,1]
    go( vec)

def left():
    print('car left')
    vec=[0,1,0,1]
    go(vec)

def right():
    print('car right')
    vec=[1,0,1,0]
    go( vec)

def clockwise_180():
    go(vec=[1,0,1,0])

def backward():
   print('car back')
   vec = [1,0,0,1]
   go(vec=vec)

def forward():
   print('car forward')
   vec = [0,1,1,0]
   go(vec=vec)

def debug():
    while True:
        vec = input('Input the vector:')
        vec = vec.split()
        vec = [int(x) for x in vec]
        go(vec)

setup()
if __name__ == '__main__':
    t = 0.5
    try:
        while True:
            cmd = input('Input the command:')
            if cmd =='a':
                left()
            elif cmd=='d':
                right()
            elif cmd=='w':
                forward()
            elif cmd=='s':
                backward()
            elif cmd=='pwd':
                for dc in range(40, 101, 1):
                   pwm(dc)
                   print(dc)
                   time.sleep(0.1)
            else:
                stop()
    except  BaseException as exp:
        GPIO.cleanup()
        print(exp)
