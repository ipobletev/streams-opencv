import logging
import cv2
import os
from modules.camera import camera
from dotenv import load_dotenv
load_dotenv()

ENABLE_GUI = (os.getenv('ENABLE_GUI', 'False') == 'True')
SENSORSTXT_PATH = os.getenv('SENSORSTXT_PATH', 'streams.txt')

STREAM_LIST = []
NAME_STREAM_LIST = []

USE_DIRECT_UUID = (os.getenv('USE_DIRECT_UUID', 'False') == 'True')
with open(SENSORSTXT_PATH, "r") as myfile:   
    lines = myfile.readlines()
    for i,line in enumerate(lines):
        line = line.rstrip('\r').rstrip('\n').split(",")
        name_stream = line[0]
        stream =  line[1]
        STREAM_LIST.append(stream)
        NAME_STREAM_LIST.append(name_stream)
    
print("Stream list:")        

for i,stream in enumerate(STREAM_LIST):
    print(str(i) + ": " + str(NAME_STREAM_LIST[i]) + " - " + str(STREAM_LIST[i]))
        
print(STREAM_LIST)

if __name__ == '__main__':

    print("INIT PROCESS")
    cameraobj = camera(STREAM_LIST)
        
    print(".....")
    while True:
        try:
            for i,stream in enumerate(STREAM_LIST):
                id_stream, frame = cameraobj.camera_process(i)
                if ENABLE_GUI == True:
                    cv2.imshow('Frame' + str(id_stream), frame)
                    cv2.waitKey(1)
        except KeyboardInterrupt:
            break
    
    cameraobj.camera_deinit()
    print("END PROCESS")