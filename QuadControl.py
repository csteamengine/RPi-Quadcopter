import pygame
import RPi.GPIO as GPIO
from myo import Myo
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
RightMotor = GPIO.PWM(17,50)
FrontMotor = GPIO.PWM(4,50)
BackMotor = GPIO.PWM(10,50)
LeftMotor = GPIO.PWM(5,50)

pygame.init()

#Boolean to help with loops
done = False #to help close
Side = False #prevent Gyro from correcting while purposely tilting
Front = False # ^^
AutoPilot = False #Allows Autopilot
StartEngines = False #Engines Start at 0 duty cycle. This starts them.

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Initialize the joysticks
pygame.joystick.init()
hover =0
BackMotor.start(hover)
FrontMotor.start(hover)
RightMotor.start(hover)
LeftMotor.start(hover)

#Preps the motors to receive duty cycle changes. Start at 0 D.C.  
#Calibrates the ESC     
for i in range(0,3):
       RightMotor.ChangeDutyCycle(i)
       BackMotor.ChangeDutyCycle(i)
       LeftMotor.ChangeDutyCycle(i)
       FrontMotor.ChangeDutyCycle(i)
       time.sleep(2)
time.sleep(5)
RightMotor.ChangeDutyCycle(0)
LeftMotor.ChangeDutyCycle(0)
BackMotor.ChangeDutyCycle(0)
FrontMotor.ChangeDutyCycle(0)

TiltAmount = 1
ThrustAmount = 3
#lowest functioning duty cycle is 3 so dont want to go below that.
#remember to change to hover - 3 --Since our current hover is 6 
DownThrust = 3       #--Since our current hover is 6 



#MAIN LOOP
while done==False:
       # EVENT PROCESSING STEP
       for event in pygame.event.get():        # User did something
           if event.type == pygame.QUIT:       # If user clicked close
               done=True       # Flag that we are done so we exit this loop
           
           
      
       #Names the two joysticks we will be using.
       joystick = pygame.joystick.Joystick(0)
       gyro = pygame.joystick.Joystick(1)
       joystick.init()
       gyro.init()

       #Naming the Axis'
       RU = joystick.get_axis(3)       #Right up/down
       RS = joystick.get_axis(2)       #Right Sideways
       LU = joystick.get_axis(1)       #Left up/down
       LS = joystick.get_axis(0)       #Left Sideways
       GYFor = gyro.get_axis(24)*10    #Gyro Forward/Backward
       GYSide = gyro.get_axis(23)*10   #Gyro Side to Side

       #Heres the fun part
       #I made it so each motor has its own Equation.
       #Right Motor Amount which is a collection of different variables.
       #----
       #thrust
       #tilt
       #hover
       #yaw
       #Gyro
       #----
       #All these add to the Duty Cycle for each motor.
       #See equations at the bottom
       RMA = 0
       LMA = 0
       BMA = 0
       FMA = 0
           
       #This is where it decides what to do with the input.
       if AutoPilot == False and StartEngines == True:
                   if RU <0:
                       Rup =(ThrustAmount*abs(RU))
               
                   if RU > 0:
                       Rup =0 - (DownThrust*abs(RU))
               
                   if RU == 0:
                       Rup = 0
                   if RS < 0:
                       YawLeft = TiltAmount*abs(RS)
                   if RS > 0:
                       YawRight = TiltAmount*abs(RS)
                   if RS == 0:
                       YawRight = 0
                       YawLeft = 0
                   if LU < 0:
                       Lfor = TiltAmount*abs(LU)
                       Forw = True
                       Lback =0
               
                   if LU > 0:
                       Lback = TiltAmount*abs(LU)
                       Forw = True
                       Lfor = 0
               
                   if LU == 0:
                       Lfor = 0
                       Lback = 0
                       Forw = False
               
                   if LS < 0:
                       Lright = TiltAmount*abs(LS)
                       Side = True
                       Lleft = 0
               
                   if LS > 0:
                       Lleft = TiltAmount*abs(LS)
                       Side = True
                       Lright = 0
               
                   if LS == 0:
                       Lleft = 0
                       Lright = 0
                       Side = False
          
                   if Side == False:
                           if GYSide > 0:
                                   GyLeft = TiltAmount*GYSide
                           if GYSide < 0:
                                   GyRight = TiltAmount*abs(GYSide)
                           if GYSide == 0:
                                   GyRight = 0
                                   GyLeft = 0
                   if Front == False:
                           if GYFor <0:
                                   GyFront = TiltAmount*abs(GYFor)
                           if GYFor >0:
                                   GyBack = TiltAmount*GYFor
                           if GYFor == 0:
                                   GyFront = 0
                                   GyBack = 0

                                   
                   #Equations for Motors
                   #Rup is thrust, pos if up neg if down so if you want to go down,
                           #Rup is being subtracted from hover.
                   #hover is generally a constant. so if all the other values are 0, you will just hover.
                   #It is the simplest concept I could come up with.               
                   RMA = hover + Rup + Lright + YawLeft +GyRight 
                   LMA = hover + Rup + Lleft + YawLeft + GyLeft
                   BMA = hover + Rup + Lfor + YawRight + GyBack
                   FMA = hover + Rup + Lback + YawRight + GyFront
       if AutoPilot == True:
                   RMA = hover
                   LMA = hover
                   BMA = hover
                   FMA = hover
           
               
       RightMotor.ChangeDutyCycle(RMA)
       LeftMotor.ChangeDutyCycle(LMA)
       BackMotor.ChangeDutyCycle(BMA)
       FrontMotor.ChangeDutyCycle(FMA)
       #remove the following once calibrated correctly       
       print(LMA,BMA,FMA,RMA)
              
          
         
       # Add in Events for if each button is pressed. PWM
       # ex if button == 14 (x) then hover returns to original value.
       
       
       L1 = joystick.get_button(10)
       L2 = joystick.get_button(8)
       R1 = joystick.get_button(11)
       R2 = joystick.get_button(9)
       PS = joystick.get_button(16)
       Start = joystick.get_button(3)
       Select = joystick.get_button(0)
       Up = joystick.get_button(4)
       Down = joystick.get_button(6)
       Xbut = joystick.get_button(14)
               
       if L1 ==1 and R1 == 1 and R2 == 1 and L2 ==1:
               done = True
               print("Done!")
       if PS == 1:
                   AutoPilot = True
       if Select == 1:
                   AutoPilot = False
       if Start == 1:
                   StartEngines = True
                   hover = 6
       if Up == 1 :
                   hover = hover + 1
       if Down == 1 :
                   hover = hover - 1
       if Xbut == 1 and AutoPilot == False:
               hover = 6
       # Limit to 50 frames per second
       clock.tick(20)
       
#stops all the motors from receiving anymore inputs.
BackMotor.stop()
FrontMotor.stop()
LeftMotor.stop()
RightMotor.stop()
GPIO.cleanup()
       
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
