#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time
 



#Definition of  motor pin 

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
    
    global delaytime
    
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    #Set the PWM pin and frequency is 2000hz
    GPIO.setup(key,GPIO.IN) # setting button as input
    GPIO.setup(EchoPin,GPIO.IN)
    GPIO.setup(TrigPin,GPIO.OUT)#pins for sensor emmitter and listenning
    

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
            GPIO.output(LED_R, GPIO.LOW)#green
	    GPIO.output(LED_G, GPIO.HIGH)
	    GPIO.output(LED_B, GPIO.LOW)  
        elif 20 <= distance <= 100:#yellow
            GPIO.output(LED_R, GPIO.HIGH)
	    GPIO.output(LED_G, GPIO.HIGH)
	    GPIO.output(LED_B, GPIO.LOW)    
        elif 0 <= distance <= 19:#red
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
    
    GPIO.cleanup()




