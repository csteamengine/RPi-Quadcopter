# RPi-Quadcopter
A Quadcopter controlled by a Raspberry Pi and a PS3 controller

  I started this project to participate in an event at ISU called HackISU. My goal was to use things that I already had, such as the RPI, PS3 controller,MYO armband, etc. I didn't want to buy a whole bunch of expensive stuff just for this project. I did have to buy ESC's and brushless motors along with a battery to power them.
  As I get better at programming, I will return and update my code and perhaps (hopefully) improve it. For now here is a description of what to do and how to do it.

Problems I ran into:
  Connecting the PS3 controller to the RPi -- Solved
  Connecting the MYO to the RPi -- Solved
  Calibrating ESC's --Solved
  Using the MYO inputs -- Not Solved Yet
  
  To start, you must have NOOBS, or some OS installed on the RPi, this can be easily done if you visit their website. Basically, download the OS onto a formatted microSD card and plug it into the Pi and then power it up. 
  
-------PS3 CONTROLLER-------
The $ denotes the beginning of a line of code. 
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

If no controller is connected, a message will pop up saying "No controller found on USB busses". In my experience I only        needed to run the sudo ./sixpair command once for each controller, as long as you haven't reset it. Now run the following to    download sixad, the controller manager.
    
    $wget http://sourceforge.net/projects/qtsixa/files/QtSixA%201.5.1/QtSixA-1.5.1-src.tar.gz
    $sudo tar xfvz QtSixA-1.5.1-src.tar.gz
    $cd QtSixA-1.5.1/sixad
    $sudo make
    $sudo mkdir -p /var/lib/sixad/profiles
    $sudo checkinstall

Once that is done run the following to run controller manager at boot. Now when you reboot the Pi, sixad will automatically run.

    $sudo update-rc.d sixad defaults

Finally, unplug the controller and reboot the system.

		$sudo reboot

Once it is up and running again, sixad will alread be running so all you have to do is press the PS button. If it does not connect or doesnt recognise it, first try restarting sixad.

    $sudo sixad --stop
    $sudo sixad --start
    
At this point it will prompt you to press the PS button. When you do so it will display this if it connected successfully.
This will be displayed on the screen.

		sixad-bin[2535]: started
		sixad-bin[2535]: sixad started, press the PS button now
		sixad-bin[2535]: unable to connect to sdp session
		sixad-bin[2535]: Connected Sony Computer Entertainment Wireless Controller

If it still wont connect then try plugging the controller in again and running 
		$sudo ./sixpair





  
