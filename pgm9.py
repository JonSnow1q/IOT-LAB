import Adafruit_DHT
import RPi.GPIO as GPIO
from time import sleep
sensor = Adafruit_DHT.DHT11
gpio = 17
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(8, GPIO.OUT, initial = GPIO.LOW)
while True:
 hum , temp = Adafruit_DHT.read_retry(sensor , gpio)
 if hum is not None and temp is not None:
     print("Temp = {0:0.1f}*C Humidity= {1:0.1f}%".format(temp,hum))
 if temp>=28:
     GPIO.output(8,GPIO.HIGH)
     sleep(0.5)
 else:
     GPIO.output(8,GPIO.LOW)
     sleep(0.5)
 else:
     print("Try again")