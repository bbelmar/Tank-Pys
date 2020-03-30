#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time
 



#Definition of  motor pin 
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13
LED_R = 22
LED_G = 27
LED_B = 24
#key definition (button on PCB)

key = 8

#Definition of ultrasonic module pin
EchoPin = 0
TrigPin = 1

#Set the GPIO port to BCM encoding mode
GPIO.setmode(GPIO.BCM)

#Ignore warning information
GPIO.setwarnings(False)

#Motor pin initialization operation
def init():
    global pwm_ENA
    global pwm_ENB
    global delaytime
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    #Set the PWM pin and frequency is 2000hz
    GPIO.setup(key,GPIO.IN) # setting button as input
    GPIO.setup(EchoPin,GPIO.IN)
    GPIO.setup(TrigPin,GPIO.OUT)#pins for sensor emmitter and listenning
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)
    
    
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
    pwm_ENB.ChangeDutyCycle(60)
    

#turn right
def right():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(60)
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

#Ultrasonic function
def Distance_test():
    GPIO.output(TrigPin,GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TrigPin,GPIO.LOW)
    while not GPIO.input(EchoPin):
        pass
    t1 = time.time()
    while GPIO.input(EchoPin):
        pass
    t2 = time.time()
    print "distance is %d " % (((t2 - t1)* 340 / 2) * 100)
    time.sleep(0.5)
    return ((t2 - t1)* 340 / 2) * 100

   
try:
    init()
    while True:
        distance = Distance_test()
        if distance > 100:
            GPIO.output(LED_R, GPIO.LOW)
	    GPIO.output(LED_G, GPIO.HIGH)
	    GPIO.output(LED_B, GPIO.LOW)  
        elif 20 <= distance <= 100:
            GPIO.output(LED_R, GPIO.HIGH)
	    GPIO.output(LED_G, GPIO.HIGH)
	    GPIO.output(LED_B, GPIO.LOW)
	    
        elif 0 <= distance <= 19:
            GPIO.output(LED_R, GPIO.HIGH)
	    GPIO.output(LED_G, GPIO.LOW)
	    GPIO.output(LED_B, GPIO.LOW)
	    time.sleep(0.1)
	    GPIO.output(LED_R, GPIO.LOW)
	    GPIO.output(LED_G, GPIO.LOW)
	    GPIO.output(LED_B, GPIO.LOW)
            time.sleep(0.1)
	    GPIO.output(LED_R, GPIO.HIGH)
	    GPIO.output(LED_G, GPIO.LOW)
	    GPIO.output(LED_B, GPIO.LOW)
            time.sleep(0.1)
	    GPIO.output(LED_R, GPIO.LOW)
	    GPIO.output(LED_G, GPIO.LOW)
	    GPIO.output(LED_B, GPIO.LOW)
	    time.sleep(0.1)
	    GPIO.output(LED_R, GPIO.HIGH)
	    GPIO.output(LED_G, GPIO.LOW)
	    GPIO.output(LED_B, GPIO.LOW)
            time.sleep(0.1)
	    GPIO.output(LED_R, GPIO.LOW)
	    GPIO.output(LED_G, GPIO.LOW)
	    GPIO.output(LED_B, GPIO.LOW)
	    time.sleep(0.1)
	    GPIO.output(LED_R, GPIO.HIGH)
	    GPIO.output(LED_G, GPIO.LOW)
	    GPIO.output(LED_B, GPIO.LOW)
           
finally:
    GPIO.cleanup()
    pwm_ENA.stop()
    pwm_ENB.stop()
    GPIO.cleanup()



