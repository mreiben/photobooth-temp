import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.OUT)
p = GPIO.PWM(10, 100)

p.start(50)
p.ChangeDutyCycle(35)
#p.ChangeFrequency(100)
print "LED on"
#GPIO.output(10,GPIO.HIGH)
time.sleep(5)

p.ChangeDutyCycle(75)

time.sleep(5)
print "LED off"
GPIO.output(10,GPIO.LOW)

p.stop()
GPIO.cleanup()
