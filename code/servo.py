from tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)
pwm2 = GPIO.PWM(15, 100)
pwm2.start(5)

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=180, 
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)

        scale = Scale(frame, from_=0, to=180, 
              orient=HORIZONTAL, command=self.update2)
        scale.grid(row=0,column=10)




    def update(self, angle):
        duty = float(angle) / 10.0 + 2.5
        pwm.ChangeDutyCycle(duty)
        
    def update2(self, angle):
        duty = float(angle) / 10.0 + 2.5
        pwm2.ChangeDutyCycle(duty)
        
root = Tk()
root.wm_title('Servo Controler')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()
