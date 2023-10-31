def run_servo(x):
	import RPi.GPIO as GPIO
	from time import sleep
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(8,GPIO.OUT)
	p=GPIO.PWM(8,50)
	p.start(0)
	p.ChangeDutyCycle(int(x))
	sleep(2)
	p.stop()
	GPIO.cleanup()
