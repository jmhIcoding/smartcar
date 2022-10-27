__author__ = 'dk'
import pygame
import time, datetime
import threading
pygame.joystick.init()
pygame.init()
print(pygame.joystick.get_count())
joy = pygame.joystick.Joystick(0)
print(joy.get_name())

def process_axes():
   print(datetime.datetime.now())
   print('change axes!')
   axes = joy.get_numaxes()
   print("Number of axes: {}".format(axes) )
   for i in range( axes ):
       axis = joy.get_axis( i )
       print("Axis {} value: {:>6.3f}".format(i, axis) )
def process_hat():
    print(datetime.datetime.now())
    print('change hat!')
    hats = joy.get_numhats()
    print( "Number of hats: {}".format(hats) )
    for i in range( hats ):
        hat = joy.get_hat( i )
        print('Hat {0}: {1}'.format(i, hat))
def process_button():
    print(datetime.datetime.now())
    print('change button!')
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
            th = threading.Thread(target=func)
            th.start()
main()




