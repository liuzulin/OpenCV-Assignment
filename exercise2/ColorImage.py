import cv2
import numpy as np
def main():
	img=cv2.imread('Test_images/Lenna.png')
	cv2.namedWindow('Original image')
	cv2.imshow('Original',img)
	b,g,r=cv2.split(img)
	cv2.imshow("Blue",b)
	cv2.imshow("Green", g)
	cv2.imshow("Red",r)
	cv2.imwrite("Blue.jpg",b)
	cv2.imwrite("Green.jpg",g)
	cv2.imwrite("Red.jpg",r)
	print('value at R(20,25):',r[20][25])
	print('value at G(20,25):',g[20][25])
	print('value at B(20,25):',b[20][25])

	YCrCb=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
	y,cb,cr=cv2.split(YCrCb)
	cv2.imshow("Y",y)
	cv2.imshow("Cb", cb)
	cv2.imshow("Cr",cr)
	cv2.imwrite("Y.jpg",y)
	cv2.imwrite("Cb.jpg",cb)
	cv2.imwrite("Cr.jpg",cr)
	print('value at Y(20,25):',y[20][25])
	print('value at Cb(20,25):',cb[20][25])
	print('value at Cr(20,25):',cr[20][25])

	HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	hue,saturation,value=cv2.split(HSV)
	cv2.imshow("Hue",hue)
	cv2.imshow("Saturation", saturation)
	cv2.imshow("Value",value)
	cv2.imwrite("Hue.jpg",hue)
	cv2.imwrite("Saturation.jpg",saturation)
	cv2.imwrite("Value.jpg",value)
	print('value at Hue(20,25):',hue[20][25])
	print('value at Saturation(20,25):',saturation[20][25])
	print('value at Value(20,25):',value[20][25])
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return
main()
