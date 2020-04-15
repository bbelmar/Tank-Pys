#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time
import curses
import os

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

#Definition of  motor pin 
IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23
ENA = 24
ENB = 18


#constants for speed:

leftspeed = 0
rightspeed = 0

#Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#Motor pin initialization operation
def motor_init():
    global pwm_ENA
    global pwm_ENB
    global delaytime
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    #Set the PWM pin and frequency is 2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)


#advance
#advance
def run(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
#start def to start motor    

#back
def back(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
    

#turn left
def left(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
    

#turn right
def right(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
    

#turn left in place
def spin_left(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
   

#turn right in place
def spin_right(leftspeed, rightspeed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(leftspeed)
    pwm_ENB.ChangeDutyCycle(rightspeed)
    
#back to the right
def back_to_right():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    
#brake
def brake():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(10)
    pwm_ENB.ChangeDutyCycle(10)
    

try:

    motor_init()
    while True:
        char = screen.getch()
        if char == ord('w'):
            if leftspeed > 90:
                pass
            
            
            if leftspeed <= 90:
                leftspeed += 10
                rightspeed = leftspeed
                print(leftspeed, rightspeed)
                time.sleep(0.1)
                run(leftspeed, rightspeed)
            
            
        elif char == ord('s'):
            if rightspeed > 90:
                    pass
            if leftspeed > 10:
                
                leftspeed -= 10
                rightspeed = leftspeed
                print(leftspeed, rightspeed)
                run(leftspeed, rightspeed)
                time.sleep(0.1)
                
                
            elif leftspeed <= 10:
                leftspeed += 10
                rightspeed += 10
                print(leftspeed, rightspeed)
                back(leftspeed, rightspeed)
                time.sleep(0.1)
            
            
        elif char == ord('a'):
            if rightspeed > 90:
                pass
            if leftspeed > 90:
                pass
            
            
            if rightspeed < 90:
                rightspeed += 10
                left(leftspeed, rightspeed)
                print('Turning Left', leftspeed, rightspeed)
                time.sleep(0.1)
            
        elif char == ord('d'):
            if leftspeed > 90:
                pass
            if rightspeed >90:
                pass
            
            
            if leftspeed < 90:
                leftspeed += 10
                right(leftspeed, rightspeed)
                print("Turning Right", leftspeed, rightspeed)
                time.sleep(0.1)
            
        elif char == ord('q'):
            if rightspeed > 90:
                pass
            if leftspeed > 90:
                pass
            rightspeed += 10
            leftspeed += 10
            if 80 > leftspeed >= 10: 
                spin_left(leftspeed, rightspeed)
                print('Spinning left at', leftspeed, rightspeed)
                time.sleep(0.1)
            
        elif char == ord('e'):
            if rightspeed > 95:
                pass
            if leftspeed > 95:
                pass
            rightspeed += 10
            leftspeed += 10
            if 80 > leftspeed >= 10: 
                spin_right(leftspeed, rightspeed)
                print("Spinning right at", leftspeed, rightspeed)
                time.sleep(0.1)
            
        elif char == ord('x'):
            print('stopping')
            brake()
            time.sleep(0.1)
        elif char == ord('1'):
            pwm_ENA.ChangeDutyCycle(10)
            pwm_ENB.ChangeDutyCycle(10)
        elif char == ord('2'):
            pwm_ENA.ChangeDutyCycle(20)
            pwm_ENB.ChangeDutyCycle(20)
        elif char == ord('5'):
            start_motor(10, 10)  
        



finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    pwm_ENA.stop()
    pwm_ENB.stop()
    GPIO.cleanup()
