import RPi.GPIO as GPIO
import time

sensor = 21
led=20

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT)

previous_state = False
current_state = False

while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if GPIO.input(sensor) == 1:
    	GPIO.output(led, True) ## Enciendo
    else:
        GPIO.output(led, False) ## Apago


    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        print("GPIO pin %s is %s" % (sensor, new_state))