import cv2
import numpy as np

#卷积核，一个腐蚀，一个膨胀
kernel_Ero=np.ones((3,1),np.uint8)
kernel_Dia=np.ones((5,3),np.uint8)

img=cv2.imread(r"")
copy_img=img.copy()
#原图copy修改尺寸
copy_img=cv2.resize(copy_img,(1600,800))
#灰度值转化
imgGray=cv2.cvtColor(copy_img,cv2.COLOR_BRG2GRAY)
#高斯滤波去噪
imgBlur=cv2.GaussianBlur(imgGray,(5,5),0)
#阈值处理
ret,thresh=cv2.threshold(imgBlur,127,255,cv2.THRESH_BINARY)
#腐蚀
imgEro=cv2.erode(thresh,kernel_Ero,iterations=2)
#膨胀
imgDia=cv2.dilate(imgEro,kernel_Dia,iterations=4)

#轮廓检测
_,contous,hie=cv2.findContours(imgDia,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt=contous

for i in cnt:
    #location
    x,y,w,h=cv2.boundingRect(i)
    #roi判断
    if y>350 and y<450 and x<1200 and w>50 and h>10:
        cv2.drawContours(copy_img,i,-1,(0,255,0),2)

cv2.imshow("img",copy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()