import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
pins = [8,10,38,40]

def setup():
    for each in pins:
        GPIO.setup(each, GPIO.OUT)
def stop():
   GPIO.output(pins, [False]*len(pins))

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


if __name__ == '__main__':
    setup()
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
    except  BaseException as exp:
        GPIO.cleanup()
        print(exp)