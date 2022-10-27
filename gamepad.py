__author__ = 'dk'
import os
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.environ["SDL_VIDEODRIVER"] = "dummy"
import pygame
import time, datetime
import threading
import hc_sr05
import pwm_movement
pygame.joystick.init()
pygame.init()
print(pygame.joystick.get_count())
left_ratio = 0
right_ratio = 0
up_ratio = 0
down_ratio = 0
if pygame.joystick.get_count():
    joy = pygame.joystick.Joystick(0)
    print(joy.get_name())

def process_axes():
    #print(datetime.datetime.now())
    #print('change axes!')
    joy = pygame.joystick.Joystick(0)
    #axes = joy.get_numaxes()
    #print("Number of axes: {}".format(axes) )
    #for i in range( axes ):
    #    axis = joy.get_axis( i )
    #    print("Axis {} value: {:>6.3f}".format(i, axis) )
    up_ratio = joy.get_axis(1)
    down_ratio = joy.get_axis(1)
    left_ratio = joy.get_axis(0)
    right_ratio = joy.get_axis(0)

    up_ratio = - up_ratio + 0.1 if up_ratio < 0  else 0
    down_ratio = down_ratio + 0.1 if down_ratio > 0 else 0

    left_ratio = - left_ratio+0.1 if left_ratio < 0 else 0
    right_ratio = right_ratio+0.1 if right_ratio >0 else 0
    if hc_sr05.distance() < 30:
        up_ratio = 0.0
    pwm_movement.move(left_ratio, right_ratio, up_ratio, down_ratio)

def process_hat():
    print(datetime.datetime.now())
    print('change hat!')
    joy = pygame.joystick.Joystick(0)
    hats = joy.get_numhats()
    print( "Number of hats: {}".format(hats) )
    for i in range( hats ):
        hat = joy.get_hat( i )
        print('Hat {0}: {1}'.format(i, hat))

def process_button():
    print(datetime.datetime.now())
    print('change button!')
    joy = pygame.joystick.Joystick(0)
    buttons = joy.get_numbuttons()
    print("Number of buttons: {}".format(buttons) )
    for i in range( buttons ):
        button = joy.get_button( i )
        print( "Button {:>2} value: {}".format(i,button) )

def main():
    while True:
        # Possible joystick events: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION, JOYDEVICEADDED, JOYDEVICEREMOVED
        for event in pygame.event.get():
            func = None
            if event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP:
                func = process_button
            elif event.type == pygame.JOYAXISMOTION:
                func = process_axes
            elif event.type == pygame.JOYHATMOTION:
                func = process_hat
            #print(func, event)
            if func ==None:
                continue
            th = threading.Thread(target=func)
            th.start()
        if hc_sr05.distance() < 30:
            up_ratio = 0.0
            pwm_movement.move(left_ratio,right_ratio, up_ratio, down_ratio)
import multiprocessing
if __name__ == '__main__':
    main()
    #subproc = multiprocessing.Process(target=main, args=())
    #subproc.daemon = True
    #subproc.start()
    #subproc.join()
    #print(subproc)
    #print('end')

