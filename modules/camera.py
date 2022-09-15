from datetime import datetime
import cv2

FOLDER_TOSAVE = "temp"
SAVE_VIDEO = False

class camera:

    stream_obj_list =[]
    videowriter_obj_list =[]
    stream_path_file=[]
    
    def __init__(self,stream_list) -> None:
        for i,stream in enumerate(stream_list):
            if stream.isnumeric(): stream = int(stream)
            stream_obj = cv2.VideoCapture(stream)  
            ret, frame = stream_obj.read()
            if ret == True: 

                self.stream_obj_list.append(stream_obj)
            
            else:
                print("error")    
                
    def camera_deinit(self):
        for i,stream_obj in enumerate(self.stream_obj_list):
            self.stream_obj_list[i].release()
            
            if SAVE_VIDEO:
                self.videowriter_obj_list[i].release()

    def start_video(self):
        self.videowriter_obj_list.clear()
        self.stream_path_file.clear()
        for i,stream_obj in enumerate(self.stream_obj_list):
            frame_width = int(self.stream_obj_list[i].get(3))
            frame_height = int(self.stream_obj_list[i].get(4))
            
            size = (frame_width, frame_height)
            date_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            path_file = FOLDER_TOSAVE + '/temp_' + str(date_time) + "_" + str(i) + '.mp4'
            videowriter = cv2.VideoWriter(path_file, 
                                            cv2.VideoWriter_fourcc(*'mp4v'),
                                            10, size)
            self.videowriter_obj_list.append(videowriter)
            self.stream_path_file.append(path_file)
        
        return self.stream_path_file
        
    def finish_video(self):
        for i,stream_obj in enumerate(self.stream_obj_list):
            self.videowriter_obj_list[i].release()
        
    def camera_process(self,id_stream):
        
            ret, frame = self.stream_obj_list[id_stream].read()
            if not ret:
                print("failed to grab frame")
                return '',''
            else:
                
                if SAVE_VIDEO:
                    #Write video
                    self.videowriter_obj_list[id_stream].write(frame)
            
                return id_stream, frame
            