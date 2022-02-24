import time
import datetime
import RPi.GPIO as GPIO
LED=27
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.out)
f = open("on.txt",'r')
q = open('off.txt','r')
while (true):
 now = datetime.datetime.now()
 todayon = now.replace(f)
 todayoff = now.replace(q)
 turnon = noq>todayon and now<todayoff
 turnoff = now>todayoff

 if(turnon == True):
 GPIO.output(LED, GPIO.HIGH)
 time.sleep(1)
 GPIO.output(LED, GPIO.LOW)
 time.sleep(1)