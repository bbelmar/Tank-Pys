import RPi.GPIO as GPIO
import time
import curses
import os
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

# global angle0
# global angle1
# global angle2
# global angle3
angle0 = 90
angle1 = 90
angle2 = 90
angle3 = 90

increment_factor = 2

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

#Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#Servo initialization operation
def Servo_init():
#     global angleleft
#     global angleright
    #servo1
    kit.servo[0].angle = 90
    kit.servo[0].actuation_range = 180
    #servo2
    kit.servo[1].angle = 90
    kit.servo[1].actuation_range = 180
    #servo3
    kit.servo[2].angle = 90
    kit.servo[2].actuation_range = 180
    #servo4
    kit.servo[3].angle = 90
    kit.servo[3].actuation_range = 180    
    kit.servo[0].set_pulse_width_range(475, 2550)    
    kit.servo[1].set_pulse_width_range(475, 2550)
    kit.servo[2].set_pulse_width_range(475, 2550)   
    kit.servo[3].set_pulse_width_range(475, 2550)
    
    
def center():
    global angle0
    global angle1
    global angle2
    global angle3
    
    kit.servo[0].angle = 90
    kit.servo[1].angle = 90
    kit.servo[2].angle = 90
    kit.servo[3].angle = 90
    angle0 = 90
    angle1 = 90
    angle2 = 90
    angle3 = 90
    
    print("Centered")
    return
    
    
def rise():#we add degs to raise the platform
    global angle0
    global angle1
    global angle2
    global angle3
    
    if 0 <= angle0 < 180:
        angle0 += increment_factor
        kit.servo[0].angle = angle0
        
    if 0 <= angle1 < 180:
        angle1 += increment_factor
        kit.servo[1].angle = 180 - angle1
#         
    if 0 <= angle2 < 180:
        angle2 += increment_factor
        kit.servo[2].angle = angle2
#         
    if 0 <= angle3 < 180:
        angle3 += increment_factor
        kit.servo[3].angle = 180 - angle3
   
    print(angle0, angle1, angle2, angle3)
    return
    
def fall():#we substract degrees to lower the platform
    global angle0
    global angle1
    global angle2
    global angle3
    
    if 0 < angle0 <= 180:
        angle0 -= increment_factor
        kit.servo[0].angle = angle0
        
    if 0 < angle1 <= 180:
        angle1 -= increment_factor
        kit.servo[1].angle = 180 - angle1
#         
    if 0 < angle2 <= 180:
        angle2 -= increment_factor
        kit.servo[2].angle = angle2
#         
    if 0 < angle3 <= 180:
        angle3 -= increment_factor
        kit.servo[3].angle = 180 - angle3
   
    print(angle0, angle1, angle2, angle3)
    return
    
    
def tilt_left():
    global angle0
    global angle1
    global angle2
    global angle3
    
    if 0 < angle0 <=180:   #we lift the left track     
        angle0 -= increment_factor        
        kit.servo[0].angle = angle0        
    if 0 < angle2 <=180:        
        angle2 -= increment_factor        
        kit.servo[2].angle = angle2
    if 0 <= angle1 < 180: #we lower the right track
        angle1 += increment_factor
        kit.servo[1].angle = 180 - angle1        
    if 0 <= angle3 < 180: #we lower the right track
        angle3 += increment_factor
        kit.servo[3].angle = 180 - angle3
            
        print(angle0, angle1, angle2, angle3)
        return

def tilt_right():
    global angle0
    global angle1
    global angle2
    global angle3
    
    if 0 < angle1 <=180:   #we lift the left track     
        angle1 -= increment_factor        
        kit.servo[1].angle = 180 - angle1        
    if 0 < angle3 <=180:        
        angle3 -= increment_factor        
        kit.servo[3].angle = 180 - angle3
    if 0 <= angle0 < 180: #we lower the right track
        angle0 += increment_factor
        kit.servo[0].angle = angle0        
    if 0 <= angle2 < 180: #we lower the right track
        angle2 += increment_factor
        kit.servo[2].angle = angle2            
        print(angle0, angle1, angle2, angle3)
        return
        
#def tilt_forward():    
    
try:
    
    Servo_init()
    while True:        
        char = screen.getch()
        if char == ord('o'):
            rise()                        
            
        elif char == ord('l'):            
            fall()
                 
        elif char == ord('k'):                        
            tilt_left()         
               
        elif char == ord(';'):
            tilt_right()            
                            
        elif char == ord(' '):
           # if 180 > angleleft >= 0 and 180 > angleright >= 0:            
#                 angleleft -= 2
#                 angleright += 2
                angleleft = angleright
                
                kit.servo[0].angle = angleleft
                kit.servo[1].angle = 180 - angleright
                kit.servo[2].angle = angleleft
                kit.servo[3].angle = 180 - angleright
                
                print(angleleft, angleright)
                
        elif char == ord('w'):
            #if 180 > angleleft >= 0 and 180 > angleright >= 0:            
#                 angleleft -= 2
#                 angleright += 2
                kit.servo[0].angle = 0
                kit.servo[1].angle = 180
                kit.servo[2].angle = 0
                kit.servo[3].angle = 180
                
        elif char == ord('s'):
            #if 180 > angleleft >= 0 and 180 > angleright >= 0:            
#                 angleleft -= 2
#                 angleright += 2
                kit.servo[0].angle = 180
                kit.servo[1].angle = 0
                kit.servo[2].angle = 180
                kit.servo[3].angle = 0
                angleleft = 180
                angleright = 180
            
                print(angleleft, angleright)

        elif char == ord('r'):
            center()
#             global angle0
#             global angle1
#             global angle2
#             global angle3
#             #if 180 > angleleft >= 0 and 180 > angleright >= 0:            
# #                 angleleft -= 2
# #                 angleright += 2
#             kit.servo[0].angle = 180 - angle0
#             kit.servo[1].angle = 180 - angle1
#             kit.servo[2].angle = 180 - angle2
#             kit.servo[3].angle = 180 - angle3
                
            
               













finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    kit.servo[0].angle = 90
    kit.servo[1].angle = 90
    kit.servo[2].angle = 90
    kit.servo[3].angle = 90
    kit.servo[4].angle = 90    
