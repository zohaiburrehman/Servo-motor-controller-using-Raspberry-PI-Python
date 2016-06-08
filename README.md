# Servo Motor Controller using Raspberry-PI and Python
<p align="center">This study examined that how anyone can control servo with Raspberry pi.
You just need little bit knowledge of electronics and programming in python.
This journal will help you to solve every problem regarding servo controlling, 
whether it is for personal use or for industrial use</p>



<img src="https://github.com/zohaiburrehman/Servo-motor-controller-using-Raspberry-PI-Python/blob/master/images/Pi2ModB1GB_-comp.jpeg">


<h2 align="center" >WHAT IS A RASPBERRY PI?</h2>

<p align="center" >Raspberry Pi is a low cost, credit-card sized computer that plugs into a computer monitor or

TV, and uses a standard keyboard and mouse. It is a capable little device that enables people of

all ages to explore computing, and to learn how to program in languages like  Python.

It’s capable of doing everything you’d expect a computer to do, from browsing the Internet and

playing high-definition video, to making spreadsheets, word-processing, and controlling

machinery. What’s more, the Raspberry Pi  has the ability to interact with the outside world, and

has been used in a wide array of digital maker projects, from music machines and parent

detectors to weather stations and tweeting birdhouses with infra-red cameras.</p>


<h2 align="center" >Servomotor</h2>



<p align="center">A servomotor is a rotary actuator or linear actuator that allows for precise control of angular or 

linear position, velocity and acceleration.  It consists of a suitable motor coupled to a sensor for 

position feedback. It also requires a relatively sophisticated controller, often a dedicated module 

designed specifically for use with servomotors.</p>

<h3 align="center" >How Servo Motor Works</h3>

<p align="center"><img  src="https://github.com/zohaiburrehman/Servo-motor-controller-using-Raspberry-PI-Python/blob/master/images/servo_lable.png"  ></p>

<p align="center">The servo hardware is manufactured right inside the engine unit and has a position able shaft, 

which for the most part  is fitted with an apparatus (as demonstrated as follows). The engine is 

controlled with an electric sign which determines the amount of movement of the shaft. </p>


<h3 align="center">How is the Servo Controlled?</h3>

<p align="center">Servos are controlled by sending an electrical pulse of variable width, or pulse width 

modulation  (PWM), through the control wire. There is a minimum pulse, a maximum pulse and 

a repetition rate. A servo motor can usually only turn 90° in either direction for a total of 180° 

movement. 

 The PWM sent to the motor determines position of the shaft, and based on the duration of the 

pulse sent via the control wire the rotor will turn to the desired position. The servo motor expects 

to see a pulse every 20 milliseconds (ms) and the length of the pulse will determine how far the 

motor turns. For example, a 1.5ms pulse will make the motor turn to the 90° position. Shorter 

than 1.5ms moves it to 0° and any longer than 1.5ms will turn the servo to 180°, as diagramed 

below. </p>
<p align="center"><img  src="https://github.com/zohaiburrehman/Servo-motor-controller-using-Raspberry-PI-Python/blob/master/images/servo_freq.png"  ></p>

<p>Use PWM to control the width of pulses to a servo motor to change its angle. Although this will work,
 the PWM generated is not completely stable, so there will be a little bit of jitter with the servo.
You should also power the servo from a separate 5V power supply because peaks in the load 
current are likely to crash or overload the Raspberry Pi.
You will need:
<br>•	5V servo motor 
<br>•	1kΩ resistor 
<br>•	5V power supply</p>
 </p>
<p align="center"><img  src="https://github.com/zohaiburrehman/Servo-motor-controller-using-Raspberry-PI-Python/blob/master/images/bread_board.png"  ></p>
 


The 1kΩ resistor is not essential, but it does protect the GPIO pin from unexpectedly high

currents in the control signal, which could occur if a fault developed on the servo.

The leads of the servo may not be the same as the colors indicated in Figure 5-2. It is common 

for the 5V wire to be red, the ground brown, and the control lead orange.

You can, if you prefer, power the servo from a battery pack rather than a power supply. Using a 




four-cell AA battery holder with rechargeable batteries will provide around 4.8V and work well 

with a servo. Using four alkali AA cells to provide 6V will be fine for many servos, but check 

the datasheet of your servo to make sure it is OK with 6V.

The user interface for setting the angle of the servo is based on the gui_slider.py program 

intended for controlling the brightness of an LED (“Controlling the Brightness of an LED”). 

However, you can modify it so that the slider sets the angle, between 0 and 180 degrees

<h2 align="center">Pyhton Code</h2>
 
<h6 align="center" >How to use files </h6>

<p align="center"><a href="https://github.com/zohaiburrehman/Servo-motor-controller-using-Raspberry-PI-Python/blob/master/code/servo.py">servo.py</a> will work if you attach  Ruspberry Pi.
Use <a href="https://github.com/zohaiburrehman/Servo-motor-controller-using-Raspberry-PI-Python/blob/master/code/servo_commented.py">servo_commented.py</a> just for GUI.  </p>


<h3 align="center" >Servo Motor Applications</h3>

Servos are used in radio-controlled airplanes to position control surfaces like elevators, rudders, walking a robot or operatinggrippers. Servo motors are small, have built-in control circuitry and have good power for their size. 

In food services and pharmaceuticals, the tools are designed to be used in harsher environments where the potential for corrosion is high due to being washed at high pressures and temperatures repeatedly to maintain strict hygiene standards. Servos are also used in in-line manufacturing, where high repetition and precise work is necessary. 

Of course, you don't have to know how a servo works to use one, but as with most electronics, the more you understand, the more doors open for expanded projects and projects' capabilities. Whether you're a hobbyist building robots, an engineer designing industrial systems or just constantly curious,




