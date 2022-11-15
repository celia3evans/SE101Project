##import image data from tensor flow
#width = image_np.shape[1]
#height = image_np.shape[0]
import Rpi.GPIO as gpio

import time


#an example of how this may be done
#for box,score,cls in zip(detections['detection_boxes'][0],detections['detection_scores'][0],detections['detection_classes'][0]):
#   if score >= 0.5: # or any other value
#        xmin = box[1]*width
#        ymin = box[0]*height
#        xmax = box[3]*width
#        ymax = box[2]*height
##


##assume we have a 800x800 grid, object is about 200x200 in the frame
ymin = 0
ymax = 100
xmin = 0
xmax = 100

forward = 7
backwards = 11
turn = 13

gpio.setmode(gpio.BOARD)

gpio.setup(7, gpio.OUT)

gpio.setup(11, gpio.OUT)

gpio.setup(13, gpio.OUT)

def reverse():
    







if ymin < 200 :
    if xmin > 600:
        reverse()

    if xmax < 200:
        reverse()
    
    else: scoop()

if ymin > 200 | ymax < 600:

    if xmin > 600:
        reverse()

    if xmax < 200:
        reverse()
    
    else: forward()

elif ymax > 600:
        
    if xmin > 600:
        forwardleft()

    if xmax < 200:
        forwardleft()
    
    else: forward()

