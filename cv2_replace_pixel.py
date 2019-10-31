#视频特定颜色追踪
import cv2
import numpy as np
import sys, os
jpg_path = sys.argv[1]
jpgs = os.listdir(jpg_path)
print(len(jpgs))

from PIL import Image



def replace_img_pixel_hsv(frame):
    hsv = cv2.cvtColor(frame, cv.COLOR_BGR2HSV)      #色彩空间由RGB转换为HSV
    lower_hsv = np.array([100, 43, 46])             #设置要过滤颜色的最小值
    upper_hsv = np.array([124, 255, 255])           #设置要过滤颜色的最大值
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)    #调节图像颜色信息（H）、饱和度（S）、亮度（V）区间，选择蓝色区域
	cv2.imshow("video",frame)
	cv2.imshow("mask", mask)
	c = cv2.waitKey(40)
	if c == 27:      #按键Esc的ASCII码为27
	    break

def extrace_object_demo():
    capture=cv2.VideoCapture("E:/imageload/video_example.mp4")
    while True:
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv2.cvtColor(frame, cv.COLOR_BGR2HSV)      #色彩空间由RGB转换为HSV
        lower_hsv = np.array([100, 43, 46])             #设置要过滤颜色的最小值
        upper_hsv = np.array([124, 255, 255])           #设置要过滤颜色的最大值
        mask = cv2.inRange(hsv, lower_hsv, upper_hsv)    #调节图像颜色信息（H）、饱和度（S）、亮度（V）区间，选择蓝色区域
        cv2.imshow("video",frame)
        cv2.imshow("mask", mask)
        c = cv2.waitKey(40)
        if c == 27:      #按键Esc的ASCII码为27
            break

def replace_img_pixel_rgb(img_file_path):
    img = Image.open(img_file_path)#读取系统的内照片
    print (img.size)#打印图片大小
    print (img.getpixel((4,4)))

    width = img.size[0]#长度
    height = img.size[1]#宽度
    i=1
    j=1
    for i in range(0,width):#遍历所有长度的点
        for j in range(0,height):#遍历所有宽度的点
            data = (img.getpixel((i,j)))#打印该图片的所有点
            print (data)#打印每个像素点的颜色RGBA的值(r,g,b,alpha)
            print (data[0])#打印RGBA的r值
            if (data[0]>=170 and data[1]>=170 and data[2]>=170):#RGBA的r值大于170，并且g值大于170,并且b值大于170
                img.putpixel((i,j),(234,53,57,255))#则这些像素点的颜色改成大红色
    img = img.convert("RGB")#把图片强制转成RGB
    img.save("e:/pic/testee1.jpg")#保存修改像素点后的图片

#extrace_object_demo()
cv2.destroyAllWindows()
