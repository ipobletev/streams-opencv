import cv2,os
from modules.camera import camera
from dotenv import load_dotenv
load_dotenv()

SENSORSTXT_PATH = os.getenv('SENSORSTXT_PATH', 'streams.txt')

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

if __name__ == '__main__':

    print("INIT PROCESS")
    cameraobj = camera(STREAM_LIST)

    try:
        os.mkdir('rec')
    except:
        pass
                
    print(".....")
    for i,stream in enumerate(STREAM_LIST):
        id_stream, frame = cameraobj.camera_process(i)
        cv2.imwrite("rec/temp_" + str(i) + "_" +  str(NAME_STREAM_LIST[i]) + ".png",frame)
    
    cameraobj.camera_deinit()
    print("END PROCESS")
