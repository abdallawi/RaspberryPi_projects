from sense_hat import SenseHat
import time

sense = SenseHat()
r = [255, 0, 0]
o = [255, 127, 0]
y = [255, 255, 0]
g = [0, 255, 0]
b = [0, 0, 255]
i = [75, 0, 130]
v = [159, 0, 255]
e = [0, 0, 0] # e is for empty
w = [255, 255, 255]

image = [ w,e,w,w,w,w,e,w,
 w,w,w,r,r,w,w,w,
 w,r,r,o,o,r,r,w,
 r,o,o,y,y,o,o,r,
 o,y,y,g,g,y,y,o,
 y,g,g,b,b,g,g,y,
 b,b,b,i,i,b,b,b,
 b,i,i,v,v,i,i,b ]
sense.set_pixels(image)
while True:
   sense.set_rotation(180)
   time.sleep(0.2)
   sense.set_rotation(0)
   time.sleep(0.2)
