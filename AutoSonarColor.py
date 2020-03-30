#-*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time


#Definition of  motor pin 

LED_R = 22
LED_G = 27
LED_B = 24

#Definition of  motor pin 
IN1 = 20
IN2 = 21
IN3 = 19
IN4 = 26
ENA = 16
ENB = 13
ServoSonar = 23
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
    global pwm_ServoSonar
    GPIO.setup(ENA,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(ENB,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)
    #Set the PWM pin and frequency is 2000hz
    GPIO.setup(key,GPIO.IN) # setting button as input
    GPIO.setup(EchoPin,GPIO.IN)
    GPIO.setup(ServoSonar, GPIO.OUT)#ServoSonar setup
    GPIO.setup(TrigPin,GPIO.OUT)#pins for sensor emmitter and listenning
    pwm_ServoSonar = GPIO.PWM(ServoSonar, 50)
    pwm_ServoSonar.start(6.5)
    pwm_ENA = GPIO.PWM(ENA, 2000)
    pwm_ENB = GPIO.PWM(ENB, 2000)
    pwm_ENA.start(0)
    pwm_ENB.start(0)
    GPIO.setup(LED_R, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)

#turn left in place after detecting obstacle
def avoid_left():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(50)
    pwm_ENB.ChangeDutyCycle(50)
    time.sleep(1.5)
    
#Button detection
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
def run(speed):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
    

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
    
def Distancetotheright():
    distance = Distance_test()
    print('searching right')
    pwm_ServoSonar.ChangeDutyCycle(8)
    time.sleep(1)
    pwm_ServoSonar.ChangeDutyCycle(0)
    distance = Distance_test()
def Distancetotheleft():
    distance = Distance_test()
    print('searching left')
    pwm_ServoSonar.ChangeDutyCycle(4)
    time.sleep(1)
    pwm_ServoSonar.ChangeDutyCycle(0)
    distance = Distance_test()

   
try:
    init()
    
    while True:
        
        
        if Distance_test() > 50:
            run(50)
            
            GPIO.output(LED_R, GPIO.LOW)#green
	    GPIO.output(LED_G, GPIO.HIGH)
	    GPIO.output(LED_B, GPIO.LOW)
            
        elif 25 <= Distance_test() <= 50:
            
            run(20)
            
            GPIO.output(LED_R, GPIO.HIGH)#amarillio
	    GPIO.output(LED_G, GPIO.HIGH)
	    GPIO.output(LED_B, GPIO.LOW) 
            
        elif Distance_test() < 25:
            brake()#we are static and we search to the right
            time.sleep(0.5)
            print('Obstacle Ahead')
            Distancetotheright()
            GPIO.output(LED_R, GPIO.HIGH)
	    GPIO.output(LED_G, GPIO.LOW)
	    GPIO.output(LED_B, GPIO.LOW)
	    
	    GPIO.output(LED_R, GPIO.LOW)
	    GPIO.output(LED_G, GPIO.LOW)
	    GPIO.output(LED_B, GPIO.LOW)
            time.sleep(0.1)
            
            
            if Distance_test() > 50:
                
                print('Clear path to the right')
                spin_right()
                time.sleep(0.5)
                pwm_ServoSonar.ChangeDutyCycle(6.5)
                time.sleep(1)
                pwm_ServoSonar.ChangeDutyCycle(0)
                print("resetting Servo")
                time.sleep(0.5)
                
            elif Distance_test() < 50:#static we found an obstacle to the right
                GPIO.output(LED_R, GPIO.HIGH)#amarillio
                GPIO.output(LED_G, GPIO.HIGH)
                GPIO.output(LED_B, GPIO.LOW)
                #Distance_test()
                print('Obstacle to the right, searching left')
                Distancetotheleft()
                time.sleep(0.5)
                 
                
                if Distance_test() < 50:
                    GPIO.output(LED_R, GPIO.HIGH)
                    GPIO.output(LED_G, GPIO.LOW)
                    GPIO.output(LED_B, GPIO.LOW)
                    print('found obstacle to the left too, going back')
                    spin_left()
                    time.sleep(1.7)
                    pwm_ServoSonar.ChangeDutyCycle(6.5)
                    time.sleep(0.5)
                    pwm_ServoSonar.ChangeDutyCycle(0)
                    print("resetting Servo")
                    time.sleep(0.5)
                    


                
                elif Distance_test() > 50: #static no obstacle to the left
                    print('Clear path to the left')
                    spin_left()
                    time.sleep(0.5)
                    pwm_ServoSonar.ChangeDutyCycle(6.5)
                    time.sleep(0.5)
                    pwm_ServoSonar.ChangeDutyCycle(0)
                    distance = Distance_test()
            
                      
        

finally:
    GPIO.cleanup()
    pwm_ENA.stop()
    pwm_ENB.stop()
    pwm_ServoSonar.stop()
    GPIO.cleanup()



