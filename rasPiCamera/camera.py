from picamera import PiCamera
import time 

camera = PiCamera()
camera.resolution = (640, 480)
camera.vflip = True

camera.start_preview()
time.sleep(2)

camera.start_recording("npc_show.h264")
camera.stop_recording()