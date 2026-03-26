# modified from arducam RPi example to work with jetson libs instead

# External module imports
import Jetson.GPIO as GPIO
import time

# Pin Definitons:
trigger_pin = 7 

def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme
    GPIO.setup(trigger_pin, GPIO.OUT, initial=GPIO.LOW) # trig pin set as output, low to start

    # trigger is a short, high pulse

    print("Start Trigger! Press CTRL+C to exit")
    try:
        while 1:
            # should be a 30hz trigger rate
            GPIO.output(trigger_pin, GPIO.HIGH)
            # trigger pulse must be longer than 2us
            time.sleep(0.001)
            GPIO.output(trigger_pin, GPIO.LOW)
            time.sleep(0.032)
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() # cleanup all GPIO


if __name__ == '__main__':
    main()