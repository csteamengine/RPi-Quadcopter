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

# Build
The ESC's and motors I bought didn't come with bullet connectors on so I soldered some on and put some heat shrink wrap on them to clean them up. To build the frame, I threw some K'NEX together and modified it as I went. I put two full platforms on and another half platform stacked above the other two. These allowed me the room to store the computer, the batteries, and the gyro. Since it was K'NEX, it is fairly strong and at the same time incredibly light. I bolted a wood square to the ends of the arms, and screwed the motors onto there. I just used velcro straps and zip ties to secure everything down and plugged everything in.

# Code
The code was written in python and started off using Pulse width modulation to control the motor speed. This, however, turned out to not work very well because the RPi is bad at it. The Pi doesn't have a real time processor so it makes the motors incredibly choppy. We got around this by sending the controller info to an Arduino via serial usb cable. This was done by converting the numbers generated in the RPi's python code into strings, then sending them to the Arduino which then converted them back to integers and sent them to the motors. This worked out incredibly well and we ended up with an incredibly responsive set of controls.

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

  
