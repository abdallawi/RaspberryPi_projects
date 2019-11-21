from sense_hat import SenseHat
import time
sense = SenseHat()
w = [150, 150, 150]
b = [0, 0, 255]
e = [0, 0, 0]
r = [255,255,0]
image = [
e,e,e,e,e,e,e,e,
w,w,w,e,e,w,w,w,
w,b,b,e,e,w,b,b,
w,w,w,e,e,w,w,w,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,e,e,e,e,e,
e,e,r,r,r,r,e,e
]
sense.set_pixels(image)
while True:
 time.sleep(1)
 sense.flip_h()