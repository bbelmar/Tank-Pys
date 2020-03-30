#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time
import curses
import os

screen = curses.initscr()
curses.cbreak()
screen.keypad(True)

#Definition of  motor pin 
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13

key = 8

#Definition of ultrasonic module pin
EchoPin = 0
TrigPin = 1
#Definition of RGB module pins
LED_R = 22
LED_G = 27
LED_B = 24
#Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#Motor pin initialization operation
def motor_init():
    global pwm_ENA
    global pwm_ENB
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(key,GPIO.IN) # setting button as input
    GPIO.setup(EchoPin,GPIO.IN)
    GPIO.setup(TrigPin,GPIO.OUT)#pins for sensor emmitter and listenning

    #Set the PWM pin and frequency is 2000hz
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)
    
    
#Button detection on pcb (key)
def key_scan():
    while GPIO.input(key):
         pass
    while not GPIO.input(key):
     time.sleep(0.01)
    if not GPIO.input(key):
             time.sleep(0.01)
    while not GPIO.input(key):
             pass
#Ultrasonic function
def Distance_test():
    GPIO.output(TrigPin,GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TrigPin,GPIO.LOW)
    while not GPIO.input(EchoPin):
        pass
    t1 = time.time()
    while GPIO.input(EchoPin):
        pass
    t2 = time.time()
    print "distance is %d " % (((t2 - t1)* 340 / 2) * 100)
    time.sleep(0.01)
    return ((t2 - t1)* 340 / 2) * 100

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
    key_scan()
    while True:
        distance = Distance_test()
        char = screen.getch()
        if char == ord('w'):
            run()
            distance = Distance_test()
        elif char == ord('s'):
            back()
            distance = Distance_test()
        elif back() and char == ord('a'):
            back_to_right()
            distance = Distance_test()
        elif char == ord('a'):
            left()
            distance = Distance_test()
        elif char == ord('d'):
            right()
            distance = Distance_test()
        elif char == ord('q'):
            spin_left()
            distance = Distance_test()
        elif char == ord('e'):
            spin_right()
            distance = Distance_test()
        elif char == ord('x'):
            brake()              
            distance = Distance_test()
        elif char == ord('1'):
            pwm_ENA.ChangeDutyCycle(10)
            pwm_ENB.ChangeDutyCycle(10)
        elif char == ord('2'):
            pwm_ENA.ChangeDutyCycle(20)
            pwm_ENB.ChangeDutyCycle(20)
        elif char == ord('5'):
            pwm_ENA.ChangeDutyCycle(50)
            pwm_ENB.ChangeDutyCycle(50)
        #distance reading
	if distance > 50:
            GPIO.output(LED_R, GPIO.LOW)
	    GPIO.output(LED_G, GPIO.HIGH)
	    GPIO.output(LED_B, GPIO.LOW)
	    print('Distance is more than 50')
	elif 30 <= distance <= 50:
            GPIO.output(LED_R, GPIO.HIGH)
	    GPIO.output(LED_G, GPIO.HIGH)
	    GPIO.output(LED_B, GPIO.LOW)
	    print('Distance is less than 50')
	        
	elif distance < 30:
            GPIO.output(LED_R, GPIO.HIGH)
	    GPIO.output(LED_G, GPIO.LOW)
	    GPIO.output(LED_B, GPIO.LOW)
	    print('Distance is less than 30')
            
        
	    #spin_right(40, 40)
            #time.sleep(0.7) 
	    #brake()
            #time.sleep(0.001)
	    #distance = Distance_test() 
	    #if distance >= 30:
	        #run(50, 50)      
	    #elif distance < 30:
		#spin_left(40, 40)
		#time.sleep(1.4)  
		#brake()
               # time.sleep(0.001)
		#distance = Distance_test() 
		#if distance >= 30:
	       #     run(50, 50)       
		#elif distance < 30:
		 #   spin_left(40, 40)   
		 #   time.sleep(0.7)
		 #   brake()
                 #   time.sleep(0.001)    
#


finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    GPIO.cleanup()

