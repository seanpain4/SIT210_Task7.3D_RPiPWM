import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

TRIG = 16
ECHO = 18
BUZZ = 11

print("Now measuring distance...")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZ, GPIO.OUT)

buzzer = GPIO.PWM(BUZZ, 100)
buzzer.start(0)


try:
	while True:
		GPIO.output(TRIG, False)
		time.sleep(0.1)
		
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)
		
		while GPIO.input(ECHO) == 0:
			pulseStart = time.time()
			
		while GPIO.input(ECHO) == 1:
			pulseEnd = time.time()
		
		pulseDuration = pulseEnd - pulseStart
		
		distance = pulseDuration * 17150
		distance = round(distance, 1)
		
		dutyCycle = 100 - ((distance / 50) * 100)
		
		buzzer.ChangeDutyCycle(dutyCycle)
				
		print("Distance: " + str(distance) + "cm.")

except KeyboardInterrupt:
	print("Cleaning up pins!")
	GPIO.cleanup()
