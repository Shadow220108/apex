import time
import board
import digitalio

# Setup the blue user LED (You can change this to board.LED_GREEN or board.LED_RED)
led = digitalio.DigitalInOut(board.LED_BLUE)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = False  # Turn LED ON (Active Low)
    time.sleep(0.5)    # Wait half a second
    led.value = True   # Turn LED OFF
    time.sleep(0.5)    # Wait half a second
