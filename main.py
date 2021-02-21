import time
import click
import findpic
import cv2 
import numpy as np
import time
import win32gui, win32ui, win32con, win32api

def find(img,x,y,w,h,str):
    svm = cv2.ml.SVM_create()
    if str == "sure":
        svm = cv2.ml.SVM_load('sure.xml')
    elif str == "skip":
        svm = cv2.ml.SVM_load('skip.xml')
    else:
        svm = cv2.ml.SVM_load('other.xml')
    img = img[y:y+h,x:x+w]
    cv2.imshow(str,img)
    mask = np.ones((img.shape[0],img.shape[1]),dtype=np.uint8)
    mask[:,:] = 0
    for i in range (0,img.shape[0]-1,3):
        for j in range(0,img.shape[1]-1,3):
            point=img[i,j]
            sampleMat =np.vstack([point])
            sampleMat = np.array(sampleMat,dtype='float32')
            (c,response)=svm.predict(sampleMat)
            if response==1:
                mask[i,j]=255
    #cv2.imshow(str+"-m",mask)
    kernel = np.ones((7,7),np.uint8)
    mask=cv2.dilate(mask,kernel,iterations =2)
    mask=cv2.erode(mask,kernel,iterations = 2)
    mask=cv2.dilate(mask,kernel,iterations =1)
   
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if(len(contours)!=0):  
        return True
    else:
        return False

def zhuzhan():
    click.sendmsg(500,520)    #助战选择  
    time.sleep(1)
    click.sendmsg(600,1000)      #出击sub

def main():
    count =0
    flag = 0
    while True:
        findpic.window_capture("../temp.jpg")
        img = cv2.imread("../temp.jpg")
        height = img.shape[0]
        width = img.shape[1]
        #print(height,width)
        count += 1
        if find(img,790,550,230,65,"sure"):      #确定
            click.sendmsg(720,850)
            time.sleep(1)
            zhuzhan()
            count =0
        if find(img,1130,720,230,65,"attack"):     #出击
            click.sendmsg(980,1150)
            time.sleep(1)
            zhuzhan()
            count =0
        if find(img,1060,650,230,65,"go"):     #前往
            click.sendmsg(930,1020)
            count =0
        
        if find(img,1220,30,20,60,"skip"):
            click.sendmsg(1050,50)
            count =0
        if count == 10:
            click.sendmsg(1000,950)#等级提升
            time.sleep(3)
            click.sendmsg(900,1100) #退出
            count = 0
        cv2.waitKey(1000) 
    cv2.destroyAllWindows()

def tiaoshi():
    while True:
        findpic.window_capture("temp.jpg")
        img = cv2.imread("temp.jpg")
        height = img.shape[0]
        width = img.shape[1]
        #print(height,width)
        if find(img,340,110,50,20,"sure"):      #确定
           pass
        if find(img,1130,720,230,65,"attack"):     #出击
            pass
        if find(img,1060,650,230,65,"go"):     #前往
            pass
        if find(img,1220,30,20,60,"skip"):
            pass

        cv2.waitKey(1000) 

if __name__ == "__main__":
    count = 0
    while True:
        c = input("调试请输入‘t’,运行请输入‘y’:")
        if c == 't':
            tiaoshi()
        elif c == 'y':
            main()
        else:
            count +=1
            if count >= 1:
                print("你的输入不合法！")
                print("叫你输啥你就输啥")
            if count >= 2:
                print("非得给我整花样")
                print("给爷爬！")
            if count >= 3:
                print(".....很有趣是不")
            if count >= 4:
                print("你再试？信不信我把你电脑搞炸")
            if count >= 5:
                print("最后一次警告了")
            if count >= 6:
                print("自毁模式开始！！")
                time.sleep(1)
                print("5")
                time.sleep(1)
                print("4")
                time.sleep(1)
                print("3")
                time.sleep(1)
                print("2")
                time.sleep(1)
                print("1")
                time.sleep(1)
                print("0")
                time.sleep(1)
                print("....")
                time.sleep(1)
                print("你赢了")

