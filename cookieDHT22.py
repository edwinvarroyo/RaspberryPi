"""
Remember to start the daemon with the command
'sudo pigpiod' before running this script. It
needs to be restarted every time your pi
is restarted.
"""

import pigpio
import DHT22
from time import sleep
import RPi.GPIO as GPIO


# Initiate GPIO for pigpio
pi = pigpio.pi()
# Setup the sensor
dht22 = DHT22.sensor(pi,4) # use the actual GPIO pin name
sensor =21
led =19
dht22.trigger()


GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(led, GPIO.OUT)

contador=0

# We want our sleep time to be above 2 seconds.
sleepTime = 3

def readDHT22():
    # Get a new reading
    dht22.trigger()
    # Save our values
    humidity  = '%.2f' % (dht22.humidity())
    temp = '%.2f' % (dht22.temperature())
    return (humidity, temp)

while True:
    humidity, temperature = readDHT22()
    print("Humedad : " + humidity + "%")
    print("Temperatura: " + temperature + "C")
    print("movimiento: " + cantador)
    if GPIO.input(sensor)==1:
    		GPIO.output(led, True)
    		contador++
    else:
    		GPIO.output(led, False)
    sleep(sleepTime)

