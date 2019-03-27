#Heavy recommendation that you read the RPi.GPIO documentation first
#When you see a Var=Number in parameters of a function, that means DEFAULT value. Subject to change.

import RPi.GPIO as IO # The Module that lets you control GPIO pins in the Raspberry Pi
from time import sleep #Used to maintain an action for a set duration of time -NO CONCURRENCY ALLOWED

class Movement: #The Movement Class for moving the robot; assign a variable to use
    def __init__(self):
        IO.setmode(IO.BCM) #BCM and BOARD are the two different modes, BOARD seems easier.
        self.outpins = [[18, 6], [13, 19]] #sub-arrays with the Input and Direction pins for both left and right
        IO.setup(self.outpins[0] + self.outpins[1], IO.OUT) #Setting up every pin as an output
        self.left  = IO.PWM(self.outpins[0][0], 100) #setting up PWM (analogue) signal for left wheels
        self.right = IO.PWM(self.outpins[1][0], 100) #setting up PWM (analogue) signal for right wheels
        self.left.start(0) #Initialise with DUTYCYCLE 0%
        self.right.start(0) #Initialise with DUTYCYCLE 0%

    def set(self, speedl, speedr, dirl=0, dirr=0):
        self.left.ChangeDutyCycle(speedl) #Change DUTYCYCLE to speedl%
        self.right.ChangeDutyCycle(speedr) #Change DUTYCYCLE to speedl%
        IO.output(self.outpins[0][1], dirl) #Digital Output Direction where 1 is Backwards and 0 is Forwards
        IO.output(self.outpins[1][1], dirr) #Digital Output Direction where 1 is Backwards and 0 is Forwards

    def stop(self): #General Function to stop Robot
        self.set(0,0,0,0) #Backtrack to set function to see why this works

    def wait(self, duration): #General Function to wait for t seconds (if t != 0) and then stop
        if duration != 0: #When duration is 0, an exclusion is made to allow ease of programming continuous movement
            sleep(duration) #Stops program for duration seconds.
            self.stop() # Take a guess: it stops after that duration.

    def turn(self, rot, t=0, speed=100): #Experimental Turning Function based on my convoluted intuition of maths
        if rot== 'r': #For rotation towards left from front aka, anticlockwise.
            self.set(speed,speed,1,0) #0 == FORWARDS
        elif rot== 'l': #For rotation towards right from front aka, clockwise.
            self.set(speed,speed,0,1) #0 == FORWARDS
        self.wait(t) #Now you see why I made a wait function ;D
    """
    def proTurn(self, aFromWall, xFromEnd, direction):
		Vo = 100
		Vi = 100/(1+((46*xFromEnd)/((xFromEnd)**2)*((aFromWall)**2))))
		if direction = 'l':
			self.set(Vi, Vo, 0, 0)
		elif direction = 'r':
			self.set(Vo, Vi, 0,0)
    """
    
    def forward(self, speed=50, t=0,direction = 0): #Basic Forwards movement; impossible to underestimate
        if direction != 0:
            dir1 = direction
            dir2 = direction
        else:
            dir1,dir2 = 0,0
        self.set(speed, speed, dir1, dir2) #0 == FORWARDS
        self.wait(t) # ;D
