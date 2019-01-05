# Copyright(c) 2017 Intel Corporation. 
# License: MIT See LICENSE file in root directory.
import numpy
import cv2
import sys,os
import time

if(len(sys.argv) < 6):
    print('please input xmin, ymin, xmax, ymax, images_dir and save_dir from command line by order')
    exit(1)
xmax = int(sys.argv[3])
xmin = int(sys.argv[1])
ymin = int(sys.argv[2])
ymax = int(sys.argv[4])
images_dir = sys.argv[5]
save_dir = sys.argv[6]
images = os.listdir(images_dir)
print(images)

def main():
    for image in images:
        if(image.endswith('.jpg') or image.endswith('png')):
            frame = cv2.imread(images_dir + image)
            cropImg = frame[ymin:ymax, xmin:xmax]               
            cv2.imwrite(save_dir + 'croped_' + image, cropImg)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

# main entry point for program. we'll call main() to do what needs to be done.
if __name__ == "__main__":
    sys.exit(main())
