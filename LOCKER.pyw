import os
from pynput.keyboard import Key, Listener
import playsound
import pyautogui
import jdatetime
import turtle as t 
import time
from random import randint
import keyboard
from threading import Thread
import screeninfo
import numpy as np
import cv2
from datetime import datetime
pyautogui.FAILSAFE = False
stop = "no"

try:
    file=open("DATA/usernum.txt","r")
    num=int(file.read())
    file.close()
    if(num == 0):
        pass
    else:
        def lock():
            while True:
                pyautogui.moveTo(5,5)
                if(stop == "yes"):
                    break
        thread1=Thread(target=lock,args=[])
        thread1.start()

        def on_press(key):
            key_press = key
            if ("ctrl" in str(key_press)):
                os.system("shutdown /p /f")
            if ("cmd" in str(key_press)):
                os.system("shutdown /p /f")
            if ("esc" in str(key_press)):
                os.system("shutdown /p /f")
                
        def listen():
            with Listener(on_press=on_press) as listener:
                listener.join()
        thread2=Thread(target=listen,args=[])
        thread2.start()

        def slides():
            screen_id = 2
            is_color = False
            screen = screeninfo.get_monitors()[0]
            width, height = screen.width, screen.height
            window_name = 'FreezeWall;'
            cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
            cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
            cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                                  cv2.WINDOW_FULLSCREEN)
            file2=open("DATA/dtcheck2.txt","w")
            file2.write("0")
            file2.close()
            file2=open("DATA/dtcheck2.txt","r")
            rdf=file2.read()
            file2.close()
            while rdf=="0":
                file2=open("DATA/dtcheck2.txt","r")
                rdf=file2.read()
                file2.close()
                if(rdf=="1"):
                    break
                files = os.listdir("pic")
                num = randint(1,len(files))
                try:
                    image = cv2.imread("pic/Slide"+str(num)+".png")
                    cv2.imshow(window_name, image)
                    key = cv2.waitKey(1000)
                except Exception as e:
                    pass
            cv2.destroyAllWindows()
        thread3=Thread(target=slides,args=[])
        thread3.start()

        face_cascade = cv2.CascadeClassifier('DATA/haarcascade_frontalface_default.xml')
        playsound.playsound("DATA/activated.mp3")
        time.sleep(0.1)
        playsound.playsound("DATA/locked.mp3")
        rec = cv2.face.LBPHFaceRecognizer_create();
        rec.read("DATA/TData.yml")
        cap = cv2.VideoCapture(0)
        id = 0
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        fontColor = (255, 255, 255)
        file=open("DATA/dtcheck2.txt",'w')
        file.write("1")
        file.close()
        playsound.playsound("DATA/start.mp3")
        times =0
        afk=0
        file=open("DATA/pin.txt")
        bpin=file.read()
        file.close()
        con=0
        while True:
            con+=1
            screen_id = 2
            is_color = False
            screen = screeninfo.get_monitors()[0]
            width, height = screen.width, screen.height
            window_name = 'Face Recognizer;'
            cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
            cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
            cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            times +=1
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.5, 5)
            if keyboard.is_pressed("p")or keyboard.is_pressed("P"):
                pyautogui.alert(text='Please enter the PIN-CODE!', title='Notification', button='OK')
                while True:
                    if keyboard.is_pressed(bpin[0]):
                        while True:
                             if keyboard.is_pressed(bpin[1]):
                                 while True:
                                     if keyboard.is_pressed(bpin[2]):
                                         break
                                 break
                        break
                break
            for (x, y, w, h) in faces:
                qx=x+w//2
                qy=y+h//2
                id, conf = rec.predict(gray[y:y + h, x:x + w])
                if(conf<=35):
                    cv2.rectangle(img, (x, y), (x + w, y + h), (50,255,50), 2)
                    ido="User Detected, Access Granted;"
                    stop = "yes"
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 2)
                    ido="Unknown, Access Denied;"
                    afk+=1
                if(afk>=80):
                    pyautogui.alert(text='Please enter the PIN-CODE!', title='Notification', button='OK')
                    while True:
                        if keyboard.is_pressed(bpin[0]):
                            while True:
                                 if keyboard.is_pressed(bpin[1]):
                                     while True:
                                         if keyboard.is_pressed(bpin[2]):
                                             break
                                     break
                            break
                    stop = "yes"
                cv2.putText(img, ido, (x+5,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
                cv2.putText(img, str(int(conf)//1), (x+5,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1)      
                cv2.imshow(window_name, img)
                cv2.waitKey(1)
                if(stop=="yes"):
                    break
            if(stop == "yes"):
                break
            
        file=open("log.txt",'r')
        files=file.read()
        file.close()
        file=open("log.txt",'w')
        now = datetime.now()
        jdatetime.set_locale('fa_IR')
        now_date=jdatetime.datetime.now().strftime("%Y/%m/%d")
        now_time=jdatetime.datetime.now().strftime("%H:%M")
        reg_date =  str(now_date)+" at "+ str(now_time)
        logtex=files+"ID "+str(id)+", logged on with confidence of "+str(100 - int(conf))+"% in "+str(reg_date)+"\n"
        file.write(logtex)
        file.close()
        playsound.playsound("DATA/done.mp3")
        playsound.playsound("DATA/unlocked.mp3")
        cap.release()
        cv2.destroyAllWindows()
        os._exit(0)
except:
    pass

#I.T.I-Certified:: BY Aria Izanlou - <185 Lines>
