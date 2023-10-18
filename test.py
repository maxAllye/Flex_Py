import RPi.GPIO as GPIO
import time

# Define the GPIO pins and corresponding labels
pin_data = {
    6: "output",
    27: "pre-charge",
    5: "interlock",
    4: "main"
}

# List of pins, for easy looping
pins = list(pin_data.keys())

# Setup the board
GPIO.setmode(GPIO.BCM)  # Use Broadcom SoC numbering
GPIO.setwarnings(False) # Disable warnings

# Setup each pin as an output and set it to LOW
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

try:
    while True:
        for pin in pins:
            label = pin_data[pin]

            # Turn on the current pin
            GPIO.output(pin, GPIO.HIGH)
            print(f"{label} is HIGH")
            time.sleep(5) # Wait 5 seconds

            # Turn off the current pin
            GPIO.output(pin, GPIO.LOW)
            print(f"{label} is LOW")

except KeyboardInterrupt:
    # This code runs on a keyboard interrupt, main loop is above.
    print("Interrupted - GPIO cleanup underway.")
    
    # Reset the status of the GPIO pins back to their default state (inputs)
    GPIO.cleanup()

    print("GPIO cleanup completed.")