# RPi-Quadcopter
A Quadcopter controlled by a Raspberry Pi and a PS3 controller

  I started this project to participate in an event at ISU called HackISU. My goal was to use things that I already had, such as the RPI, PS3 controller, MYO armband, etc. I didn't want to buy a whole bunch of expensive stuff just for this project. I did have to buy ESC's and brushless motors along with a battery to power them.
  As I get better at programming, I will return and update my code and perhaps (hopefully) improve it. For now, here is a description of what to do and how to do it. To see pictures along with procedures, visit my website at sites.google.com/a/iastate.edu/steenhagen
  
Parts:

		RPi
		ESC's 
		Brushless Motors
		PS3 controllers
		LiPo Battery
		Quadcopter Power Distribution plate
		male to female wire connectors
		Small phone battery charger
		K'NEX

Problems I ran into: 

		--Connecting the PS3 controller to the RPi -- Solved
		--Connecting the MYO to the RPi -- Solved
		--Calibrating ESC's --Solved
		--Using the MYO inputs -- Not Solved Yet 
  
  To start, you must have NOOBS, or some OS installed on the RPi, this can be easily done if you visit their website. Basically, download the OS onto a formatted microSD card and plug it into the Pi and then power it up. To sign in for the first time, the username is "pi" and the password is "raspberry".
  
# PS3 CONTROLLER
The PS3 Controller is fairly easy to set up. Basically the commands download executable file sixpair that allows your Pi to recognize the bluetooth address of the controller. Once the file is installed, it is really plug and play. I have found it incredibly easy to get the controller up and running. First, download and compile the files, then plug in the PS3 controller via usb. Then, simply run sudo ./sixpair, then sixad --start and the controller is good to go.

# PWM
The motors are controlled by what is called pulse width modulation. Basically, there is the frequency and the duty cycle. Frequency is the amount of loops per second. The duty cycle is the percentage of time that the motor gets the on signal. So if you have a duty cycle of 50%, the motor will be on for half the loop and off for the other half.

With that explained, it is fairly easy to understand. I practiced the PWM with LED's and tacked down the code by using the controller to perfect it. I hooked up 4 LED's (one for each motor) and went from there. I ran into trouble when I connected the motors. The LED's could be programmed with a duty cycle from 0 to 100. However when I hooked the motors up, the code didn't work. This had me puzzled for a while, so I wrote out the PWM_Motor_Range script. 

Essentially this script maps out the motors duty cycle range by plugging numbers in from 0 to 20. I found that my motors wouldnt start until the duty cycle was around 3, and it would cut off at anything above 13. Although this range seems small, this is plenty of room to work with. I simply rewrote the QuadControl to a scale more suitable. After doing this, the motors seemed to work well. 

From here I went on to build the copter out of K'NEX. It has a octagonal central tower that is two platforms high. From there it has 4 arms with reinforcment truss's underneath. All of this is resting on 8 landing gear each extending from a side of the arms. I strapped the Pi onto the top, the Myo inbetween the two platfroms, and the batteries on a small shelf like roof above the Pi. From there I had the ESC's tied midway down the arms and the motors obviously on the end of each arm.

Of course your copter will weight slightly different then mine so you may have to adjust the PWM percentages to be able to lift the craft correctly.

# Build
The ESC's and motors I bought didn't come with bullet connectors on so I soldered some on and put some heat shrink wrap on them to clean them up. To build the frame, I threw some K'NEX together and modified it as I went. I put two full platforms on and another half platform stacked above the other two. These allowed me the room to store the computer, the batteries, and the gyro. Since it was K'NEX, it is fairly strong and at the same time incredibly light. I bolted a wood square to the ends of the arms, and screwed the motors onto there. I just used velcro straps and zip ties to secure everything down and plugged everything in.

# Controls
I designed the controls for this to be as simple but fun as possible. That is why I chose the PS3 controller, it has has so many buttons that are all easy to program with. Here is how I programmed the controls. 

Start ---- starts motors

PS button ----autopilot

Select ---- autopilot off

Up/Down
		Right joystick up and down
		
Forward backward side to side
    Left joystick in the direction you want to tilt
    
Yaw
    Right joystick left and right
    
Increase hover 

    Dpad up
    
Decrease hover 

    Dpad down
    
X ----- reset hover

L1 R1 L2 and R2

    Ends program 

  
