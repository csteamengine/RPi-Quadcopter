
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
done = False
p = GPIO.PWM(4,50)
clock = pygame.time.Clock()

pygame.init()
p.start(50)


#this will allow you to figure out what the motors limits are. For Leds
#they can often take higher Duty Cycles all the way up to 100 but I found for
#my motors that they had to be in the range of 3-13
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    
    for i in range(0,20):
        p.ChangeDutyCycle(i)
        time.sleep()
        print(i)
    
    clock.tick(20)
p.stop()
GPIO.cleanup()

    


