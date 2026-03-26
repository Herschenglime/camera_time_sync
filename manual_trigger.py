# modified from arducam RPi example to work with jetson libs instead

# External module imports
import Jetson.GPIO as GPIO
import sys
import termios
import tty
import time

# Pin Definitions:
trigger_pin = 7


def pulse_trigger(pulse_width_s: float = 0.001) -> None:
    """Send a single HIGH pulse on the trigger pin."""
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(pulse_width_s)
    GPIO.output(trigger_pin, GPIO.LOW)


def get_single_keypress() -> str:
    """Read one keypress from stdin without requiring Enter."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def main() -> None:
    # Pin setup
    GPIO.setmode(GPIO.BOARD)  # Board pin-numbering scheme
    GPIO.setup(trigger_pin, GPIO.OUT, initial=GPIO.LOW)  # Trigger pin as output

    print("Manual trigger ready.")
    print("Press Space to send one pulse. Press 'q' to quit.")

    try:
        while True:
            key = get_single_keypress()
            if key.lower() == "q":
                break
            if key == " ":
                pulse_trigger()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()  # cleanup all GPIO


if __name__ == "__main__":
    main()
