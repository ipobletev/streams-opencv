# Streams opencv

## Run Program

Programs:
- singlecapture.py
- savevideo_tofile.py
- test_stream.py

-Make a .env file in main folder to configure. Add macros. \
-Add streams.txt with all streams sensors
```
device_name1,url_stream1
device_name2,url_stream2
```

Run:
```
python3 program
```
## Configure and macros for .env file

### singlecapture.py
Single capture for all cameras and save the capture image in /rec
```
SENSORSTXT_PATH 
```
### savevideo_tofile.py
Save the capture streams in a video file.
```
TIME_TO_SEND
SENSORSTXT_PATH 
FOLDER_TOSAVE
ENABLE_GUI
SAVE_VIDEO
```
### test_stream.py
Capture frame from stream source
```
ENABLE_GU
SENSORSTXT_PATH
```
