
import time 

name = "NPC"

camera = PiCamera() 
camera.resolution = (640, 480) #resolution of camera 
camera.framerate = 10
camera.vflip = True #flips camera view to right 

camera.start_preview() 
time.sleep(2) #camera warming up 

camera.start_recording("npc_show.h264") #name of recording 
camera.stop_recording()  #stop recording 