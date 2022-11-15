import picamera


from time import sleep
from picamera import PiCamera
while(True):
    camera = PiCamera()
    camera.resolution = (2560,1936)
    camera.start_preview()
    sleep(5)
    camera.capture('test1.jpg')
    camera.stop_preview()
