import glob
import logging
import time
import cv2
import os
from modules.camera import camera
from dotenv import load_dotenv
load_dotenv()

TIME_TO_SEND = int(os.getenv('TIME_TO_SEND', '5'))
SENSORSTXT_PATH = os.getenv('SENSORSTXT_PATH', 'streams.txt')
FOLDER_TOSAVE = os.getenv('FOLDER_TOSAVE', 'temp')
ENABLE_GUI = (os.getenv('ENABLE_GUI', 'False') == 'True')
SAVE_VIDEO = (os.getenv('SAVE_VIDEO', 'True') == 'True')

STREAM_LIST = []
NAME_STREAM_LIST = []

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
        
def sendToCloud(paths_stream_files):
    
    print("send to cloud")
    print(paths_stream_files)
    
    for i,path_file in enumerate(paths_stream_files):
        
    
        pass

if __name__ == '__main__':
    
    # Clear terminal
    #clear = lambda: os.system('clear')
    #clear()

    # # Delete temp lo
    # for filename in glob.glob("temp/*"):
    #     os.remove(filename)

    print("INIT PROCESS")
    cameraobj = camera(STREAM_LIST)

    print(".....")
    while True:
        try:
        
        
            last_time = time.time()
            
            # Init video
            paths_stream_files = cameraobj.start_video()
            
            #Get camera frames and save
            while(time.time()-last_time <= TIME_TO_SEND):
                #print(time.time()-last_time )
                for i,stream in enumerate(STREAM_LIST):
                    id_stream, frame = cameraobj.camera_process(i)
                    if ENABLE_GUI == True:
                        cv2.imshow('Frame' + str(id_stream), frame)
                        cv2.waitKey(1)
            
            #Finish video file
            cameraobj.finish_video()
            
            #Send to cloud
            sendToCloud(paths_stream_files)
    
        except Exception as error_info:
            print("Un error ha ocurrido.")
            print(error_info)
            
    cameraobj.camera_deinit()
    print("END PROCESS")