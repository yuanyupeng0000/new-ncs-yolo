# Copyright(c) 2017 Intel Corporation. 
# License: MIT See LICENSE file in root directory.
import numpy
import cv2
import sys
import time
import os

video_list = []
def search(root, target='.ts'): 
    file_list = []
    items = os.listdir(root) 
    for item in items: 
        path = os.path.join(root, item) 
        if os.path.isdir(path): 
            print('[-]', path) 
            search(path, target) 
        elif (path.split('/')[-1]).endswith(target): 
            print('[+]', path)
            video_list.append(path) 
        else: 
            print('[!]', path)

if(len(sys.argv) < 4):
    print('please input start_index, fram_gap, video_dir, save_dir , total_frame_per_video, from command line by order')
    exit(1)
video_dir = sys.argv[3]
start_index = int(sys.argv[1])
gap = int(sys.argv[2])
save_dir = sys.argv[4]
os.system('mkdir -p ' + save_dir)
total_frame_per_video = sys.argv[5]

os.system("mkdir " + save_dir)

def main():
    search(video_dir)
    print('find video : {0}'.format(len(video_list)))
    image_index = start_index
    for video_file in video_list:
        '''video_time_stamp = int((video_file.split('/')[-1])[:2])
        if(video_time_stamp < 17):
            continue'''
        print(video_file)
        loop = 0
        cap = cv2.VideoCapture(video_file)
        if (cap.isOpened()== False): 
            print("Error opening video stream or file")

        # Read until video is completed
        ###fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        ###out = cv2.VideoWriter('saved_video/output_confidence0.35.avi', fourcc,15,(640,480))
    
        while(cap.isOpened()):
        # Capture frame-by-frame
            ret, frame = cap.read()
            loop = loop + 1
            if(int(loop/gap) == int(total_frame_per_video)):
                break
            if ret == True:
                if int(image_index%gap) == 0:
                    #cropImg = frame[0:240, 160:480]
                    #img = cv2.resize(cropImg, (640,480))
                    save_name = save_dir + '/' + video_dir.split('/')[-1] + (video_file.split('/')[-1])[:-4] + str(int(start_index + (image_index-start_index)/gap)) + ".jpg"
                    save_name = save_name.replace(' ','')
                    print('save_name:{0}'.format(save_name))
                    cv2.imwrite(save_name, frame)
                    print('Created {0}'.format(int(start_index + (image_index-start_index)/gap)))
                image_index = image_index + 1
                continue
        
            # Press Q on keyboard to  exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # When everything done, release the video capture object
        cap.release()
# main entry point for program. we'll call main() to do what needs to be done.
if __name__ == "__main__":
    sys.exit(main())
