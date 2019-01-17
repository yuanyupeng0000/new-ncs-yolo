# Copyright(c) 2017 Intel Corporation. 
# License: MIT See LICENSE file in root directory.
import numpy
import cv2
import sys
import time

if(len(sys.argv) < 4):
    print('please input start_index, fram_gap, video_file, save_dir from command line by order')
    exit(1)
video_file = sys.argv[3]
start_index = int(sys.argv[1])
gap = int(sys.argv[2])
save_dir = sys.argv[4]

def main():
    cv_window_name = "SSD MobileNet - hit key 'q' to exit"
    cap = cv2.VideoCapture(video_file)

    image_index = start_index
    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    # Read until video is completed
    ###fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    ###out = cv2.VideoWriter('saved_video/output_confidence0.35.avi', fourcc,15,(640,480))
    
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            if int(image_index%gap) == 0:
                #cropImg = frame[0:240, 160:480]
                #img = cv2.resize(cropImg, (640,480))
                cv2.imwrite(save_dir + '/' + str(start_index + (image_index-start_index)/gap).zfill(12) + ".jpg", frame)
        image_index = image_index + 1
        #cv2.HoughLinesP
        #cv2.namedWindow("SSD-Mobilenet",0)
        #cv2.resizeWindow("SSD-Mobilenet", 640, 480)
        #cv2.imshow(cv_window_name, frame)
        
        # Press Q on keyboard to  exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()


# main entry point for program. we'll call main() to do what needs to be done.
if __name__ == "__main__":
    sys.exit(main())
