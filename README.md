# RPi-Quadcopter
A Quadcopter controlled by a Raspberry Pi and a PS3 controller

  I started this project to participate in an event at ISU called HackISU. My goal was to use things that I already had, such as the RPI, PS3 controller, MYO armband, etc. I didn't want to buy a whole bunch of expensive stuff just for this project. I did have to buy ESC's and brushless motors along with a battery to power them.
  As I get better at programming, I will return and update my code and perhaps (hopefully) improve it. For now, here is a description of what to do and how to do it.
  
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

The $ denotes the beginning of a line of code to be entered in the Terminal. 
First make sure your Pi is up to date (This may take a while depending on your pi):
	
		$sudo apt-get update

Next install the bluetooth support (Drivers, compilers and such) this one will take a long time so get comfortable:   
   $ denotes a new line. this first one is a long line.
   
    $sudo apt-get install bluez-utils bluez-compat bluez-hcidump checkinstall libusb-dev 
      libbluetooth-dev joystick
      Make sure to run the above command as a single line.
      Once this is done you will need to download and compile the controller utility:
    $wget http://www.pabr.org/sixlinux/sixpair.c
    $gcc -o sixpair sixpair.c -lusb

Next connect the PS3 controller to the Pi using the USB cable and type the following
    
    $sudo ./sixpair

If this is successful, it will return something like this:

		Current Bluetooth master: 00:10:60:57:15:C7
 		Setting master bd_addr to: 00:10:60:57:15:C7 

If no controller is connected, a message will pop up saying "No controller found on USB busses". In my experience I only     needed to run the sudo ./sixpair command once for each controller, as long as you haven't reset it. Now run the following 		to download sixad, the controller manager.
    
    $wget http://sourceforge.net/projects/qtsixa/files/QtSixA%201.5.1/QtSixA-1.5.1-src.tar.gz
    $sudo tar xfvz QtSixA-1.5.1-src.tar.gz
    $cd QtSixA-1.5.1/sixad
    $sudo make
    $sudo mkdir -p /var/lib/sixad/profiles
    $sudo checkinstall

Once that is done, run the following to allow the controller mangager to run at boot. Now when you reboot the Pi, sixad will automatically run.

		$sudo update-rc.d sixad defaults

Finally, unplug the controller and reboot the system.

		$sudo reboot

Once it is up and running again, sixad will already be running so all you have to do is press the PS button. If it does not connect or doesnt recognize it, first try restarting sixad.

    $sudo sixad --stop
    $sudo sixad --start
    
At this point it will prompt you to press the PS button. When you do so it will display this if it connected successfully.
This will be displayed on the screen.

		sixad-bin[2535]: started
		sixad-bin[2535]: sixad started, press the PS button now
		sixad-bin[2535]: unable to connect to sdp session
		sixad-bin[2535]: Connected Sony Computer Entertainment Wireless Controller

If it still wont connect then try plugging the controller in again and running.

		$sudo ./sixpair

Each time you start the pi, you simply have to press the PS button on the controller to connect it, as long as you ran the update -rc command above. However if you want to connect a second controller on boot up, in the terminal just type 
		$sixad --stop
		$sixad --start
Then press the PS button on the second controller.

# PWM
The motors are controlled by what is called pulse width modulation. Basically, there is the frequency and the duty cycle. Frequency is the amount of loops per second. The duty cycle is the percentage of time that the motor gets the on signal. So if you have a duty cycle of 50%, the motor will be on for half the loop and off for the other half.

With that explained, it is fairly easy to understand. I practiced the PWM with LED's and tacked down the code by using the controller to perfect it. I hooked up 4 LED's (one for each motor) and went from there. I ran into trouble when I connected the motors. The LED's could be programmed with a duty cycle from 0 to 100. However when I hooked the motors up, the code didn't work. This had me puzzled for a while, so I wrote out the PWM_Motor_Range script. 

Essentially this script maps out the motors duty cycle range by plugging numbers in from 0 to 20. I found that my motors wouldnt start until the duty cycle was around 3, and it would cut off at anything above 13. Although this range seems small, this is plenty of room to work with. I simply rewrote the QuadControl to a scale more suitable. After doing this, the motors seemed to work well. 

From here I went on to build the copter out of K'NEX. It has a octagonal central tower that is two platforms high. From there it has 4 arms with reinforcment truss's underneath. All of this is resting on 8 landing gear each extending from a side of the arms. I strapped the Pi onto the top, the Myo inbetween the two platfroms, and the batteries on a small shelf like roof above the Pi. From there I had the ESC's tied midway down the arms and the motors obviously on the end of each arm.

Of course your copter will weight slightly different then mine so you may have to adjust the PWM percentages to be able to lift the craft correctly.


  
