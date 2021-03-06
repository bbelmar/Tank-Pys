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
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13
ServoUpDownPin = 9
ServoLeftRightPin = 11

#Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#Motor pin initialization operation
def motor_init():
    global pwm_ENA
    global pwm_ENB
    global delaytime
    global pwm_servo
    global pwm_UpDownServo
    global pwm_LeftRightServo
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
    #servopin
    GPIO.setup(ServoUpDownPin, GPIO.OUT)
    GPIO.setup(ServoLeftRightPin, GPIO.OUT)
    pwm_UpDownServo = GPIO.PWM(ServoUpDownPin, 50)
    pwm_LeftRightServo = GPIO.PWM(ServoLeftRightPin, 50)
    pwm_UpDownServo.start(0)
    pwm_LeftRightServo.start(0)



#advance
def run():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(25)
    pwm_ENB.ChangeDutyCycle(25)
    

#back
def back():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(25)
    pwm_ENB.ChangeDutyCycle(25)
    

#turn left
def left():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(25)
    pwm_ENB.ChangeDutyCycle(50)
    

#turn right
def right():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(25)
    

#turn left in place
def spin_left():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
   

#turn right in place
def spin_right():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    
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
            run()
        elif char == ord('s'):
            back()
        elif char == ord('a'):
            left()
        elif char == ord('d'):
            right()
        elif char == ord('q'):
            spin_left()
        elif char == ord('e'):
            spin_right()
        elif char == ord('x'):
            brake()              
        elif char == ord('1'):
            pwm_ENA.ChangeDutyCycle(10)
            pwm_ENB.ChangeDutyCycle(10)
        elif char == ord('2'):
            pwm_ENA.ChangeDutyCycle(20)
            pwm_ENB.ChangeDutyCycle(20)
        elif char == ord('5'):
            pwm_ENA.ChangeDutyCycle(50)
            pwm_ENB.ChangeDutyCycle(50)
        elif char == ord('k'):
            pwm_LeftRightServo.ChangeDutyCycle(9)
            time.sleep(0.5)
            pwm_LeftRightServo.ChangeDutyCycle(0)
        elif char == ord(';'):
            pwm_LeftRightServo.ChangeDutyCycle(4)
            time.sleep(0.5)
            pwm_LeftRightServo.ChangeDutyCycle(0)
        elif char == ord('o'):
            pwm_UpDownServo.ChangeDutyCycle(2)
            time.sleep(0.5)
            pwm_UpDownServo.ChangeDutyCycle(0)
        elif char == ord('.'):
            pwm_UpDownServo.ChangeDutyCycle(6)
            time.sleep(0.5)
            pwm_UpDownServo.ChangeDutyCycle(0)
        elif char == ord('l'):
            pwm_LeftRightServo.ChangeDutyCycle(6)
            time.sleep(0.5)
            pwm_LeftRightServo.ChangeDutyCycle(0)
            pwm_UpDownServo.ChangeDutyCycle(4)
            time.sleep(0.5)
            pwm_UpDownServo.ChangeDutyCycle(0)
            
        else:
            pwm_ENA.ChangeDutyCycle(0)
            pwm_ENB.ChangeDutyCycle(0)



finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    pwm_ENA.stop()
    pwm_ENB.stop()
    
    pwm_LeftRightServo.stop()
    pwm_UpDownServo.stop()
    GPIO.cleanup()

