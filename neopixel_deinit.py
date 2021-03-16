import time
import board
import neopixel

pixel_pin = board.NEOPIXEL
pixels = neopixel.NeoPixel(pixel_pin, 1, brightness=0.2, auto_write=False)

pixels[0] = (16,0,0)
pixels.show()
while True:
    time.sleep (600)
pixels.deinit()
