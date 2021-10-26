try:
    from datetime import datetime
    import playsound
    import time
    import os
    import subprocess
    import hashlib
    import turtle as t
    from turtle import *
    import pyautogui
    import cv2
    from threading import Thread
    import jdatetime
    import numpy as np
    from PIL import Image
    m=t.Turtle()
    m.ht()
    dcw=t.Turtle()
    dcw.ht()
    scr=t.Screen()
    t.ht()

    def button_design(bnum,text1,text2,text3):
        t.pensize(2)
        t.speed(4)
        t.ht()
        t.pencolor("#8000ff")
        t.fillcolor("#f3e6ff")
        if(bnum==2):
            t.begin_fill()
            t.pu()
            t.goto(-105,-30)
            t.pd()
            t.goto(-255, -30)
            t.goto(-255, -90)
            t.goto(-105, -90)
            t.goto(-105, -30)
            t.end_fill()
            t.pu()
            t.goto(-180, -65)
            t.pd()
            t.write(text1, align="center", font=("Candara Light", 10,"bold"))
            t.begin_fill()
            t.pu()
            t.goto(105, -30)
            t.pd()
            t.goto(255, -30)
            t.goto(255, -90)
            t.goto(105, -90)
            t.goto(105, -30)
            t.end_fill()
            t.pu()
            t.goto(180, -65)
            t.pd()
            t.write(text3, align="center", font=("Candara Light", 10,"bold"))
        elif(bnum==3):
            t.begin_fill()
            t.pu()
            t.goto(-105, -30)
            t.pd()
            t.goto(-255, -30)
            t.goto(-255, -90)
            t.goto(-105, -90)
            t.goto(-105, -30)
            t.end_fill()
            t.pu()
            t.goto(-180, -65)
            t.pd()
            t.write(text1, align="center", font=("Candara Light", 10,"bold"))
            t.begin_fill()
            t.pu()
            t.goto(-75, -30)
            t.pd()
            t.goto(75, -30)
            t.goto(75, -90)
            t.goto(-75, -90)
            t.goto(-75, -30)
            t.end_fill()
            t.pu()
            t.goto(0, -65)
            t.pd()
            t.write(text2, align="center", font=("Candara Light", 10,"bold"))
            t.begin_fill()
            t.pu()
            t.goto(105, -30)
            t.pd()
            t.goto(255, -30)
            t.goto(255, -90)
            t.goto(105, -90)
            t.goto(105, -30)
            t.end_fill()
            t.pu()
            t.goto(180, -65)
            t.pd()
            t.write(text3, align="center", font=("Candara Light", 10,"bold"))
        t.speed(0)
        t.pensize(1)

    def errpage():
        try:
            scr.clearscreen()
            t.setup(620, 510)
            t.write("Error", align="center", font=("Broadway", 35))
            t.ht()
            scr.bgcolor("#e6ccff")
            t.pencolor("red")
            t.pu()
            t.goto(0, -190)
            t.pd()
            t.write("Unfortunatly, An error has been detected.", align="center", font=("Broadway", 10))
            t.pu()
            t.goto(0, -215)
            t.pd()
            t.pencolor("#4d0099")
            t.write("You may have given the program wrong value!", align="center", font=("Broadway", 10))
            time.sleep(5)
            main_menu()
        except:
            os._exit(0)

    def rview():
        t.speed(0)
        t.setup(500,600)
        t.bgcolor("#ccccff")
        t.title("Codoffee FreezeWall 2.1")
        image = "pgpic.gif"
        scr.bgpic(image)
        t.bgcolor("#ccccff")
        playsound.playsound("Codoffee Audio.mp3")

    def main_menu():
        file = open("DATA/dtcheck.txt","w")
        file.write("1")
        file.close()
        scr.clearscreen()
        t.ht()
        t.speed(0)
        t.setup(620, 510)
        t.title("Codoffee FreezeWall 2.1")
        image = "bgpic.gif"
        scr.bgpic(image)
        m = t.Turtle()
        m.ht()
        m.speed(0)
        t.clear()
        t.bgcolor("#ccccff")
        button2 = Turtle()
        image = "exit.gif"
        scr.addshape(image)
        button2.shape(image)
        button2.speed(0)
        button2.pu()
        button2.goto(225, -211)
        button1 = Turtle()
        image = "face.gif"
        scr.addshape(image)
        button1.shape(image)
        button1.speed(0)
        button1.pu()
        button1.goto(75, -211)
        button3 = Turtle()
        image = "security.gif"
        scr.addshape(image)
        button3.shape(image)
        button3.speed(0)
        button3.pu()
        button3.goto(-70, -211)
        button4 = Turtle()
        image = "info.gif"
        scr.addshape(image)
        button4.shape(image)
        button4.speed(0)
        button4.pu()
        button4.goto(-225, -211)
        m.clear()
        m.pu()
        m.goto(0, 20)
        m.pd()
        m.pencolor("#4d0099")
        m.write('Codoffee FreezeWall | Control Panel', align="center", font=("Broadway", 12))
        button1.onclick(buton1)
        button2.onclick(buton2)
        button3.onclick(buton3)
        button4.onclick(buton4)
        
    def recorder(number,count,scr,t):
        try:
            scr.clearscreen()
            t.pencolor("black")
            t.write("Recording...", align="center", font=("Broadway", 13))
            t.ht()
            scr.bgcolor("#e6ccff")
            t.pencolor("#4d0099")
            t.pu()
            t.goto(0, -190)
            t.pd()
            t.write("For the best train, move your head during", align="center", font=("Broadway", 10))
            t.pu()
            t.goto(0,-215)
            t.pd()
            t.write("the last 20% of recording your face!", align="center",font=("Broadway", 10))
            t.pu()
            t.goto(0,-240)
            t.pd()
            t.pencolor("red")
            t.write("Recording will stop if it can't detect your face.", align="center",font=("Broadway", 10))
            t.pu()
            t.goto(0,-30)
            t.pd()
            t.pencolor("green")
            t.write("Progress: "+str(0)+"%", align="center", font=("Broadway", 13))
            face_cascade = cv2.CascadeClassifier('DATA/haarcascade_frontalface_default.xml')
            cap = cv2.VideoCapture(0)
            id =number
            sampleN = 0;
            while 1:
                t.undo()
                t.write("Progress: "+str(int(sampleN * 100 / count))+"%", align="center", font=("Broadway", 13))
                ret, img = cap.read()
                gray = img
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    sampleN = sampleN + 1;
                    #print(sampleN)
                    cv2.imwrite(
                        "DATA/FData/User." + str(id) + "." + str(sampleN) + ".jpg",
                        gray[y:y + h, x:x + w])
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                if sampleN > count:
                    break
            cap.release()
            cv2.destroyAllWindows()
            return 'ok'
        except:
            return 'error'

    def trainer(scr,t):
        try:
            scr.clearscreen()
            t.write("In process...", align="center", font=("Broadway", 13))
            t.ht()
            scr.bgcolor("#e6ccff")
            t.pencolor("#4d0099")
            t.pu()
            t.goto(0, -190)
            t.pd()
            t.write("The software is training your face, Please wait!", align="center", font=("Broadway", 10))
            t.pu()
            t.goto(0,-215)
            t.pd()
            t.pencolor("red")
            t.write("This action may take up to 5 minutes!", align="center",font=("Broadway", 10))
            recognizer = cv2.face.LBPHFaceRecognizer_create();
            path = "DATA/FData"
            def getImagesWithID(path):
                imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
                faces = []
                IDs = []
                for imagePath in imagePaths:
                    facesImg = Image.open(imagePath).convert('L')
                    faceNP = np.array(facesImg, 'uint8')
                    ID = int(os.path.split(imagePath)[-1].split(".")[1])
                    faces.append(faceNP)
                    IDs.append(ID)
                return np.array(IDs), faces
            Ids, faces = getImagesWithID(path)
            recognizer.train(faces, Ids)
            recognizer.save("DATA/TData.yml")
            cv2.destroyAllWindows()
            return 'ok'
        except:
            return 'error'

    try:
        button1=t.Turtle()
        button2=t.Turtle()
        button3=t.Turtle()
        button4=t.Turtle()
        button1.ht()
        button2.ht()
        button3.ht()
        button4.ht()
        def buton1(x,y):
            try:
                file = open("DATA/dtcheck.txt","w")
                file.write("0")
                file.close()
                time.sleep(0.5)
                scr.clearscreen()
                scr.bgcolor('#e6ccff')
                files = os.listdir('DATA/FData')
                num = 0
                u1 = 0
                u2 = 0
                u3 = 0
                u4 = 0
                u5 = 0
                u6 = 0
                u7 = 0
                u8 = 0
                u9 = 0
                u10 = 0
                for file in files:
                    if ("User.1" in file):
                        u1 = 1
                    elif ("User.2" in file):
                        u2 = 1
                    elif ("User.3" in file):
                        u3 = 1
                    elif ("User.4" in file):
                        u4 = 1
                    elif ("User.5" in file):
                        u5 = 1
                    elif ("User.6" in file):
                        u6 = 1
                    elif ("User.7" in file):
                        u7 = 1
                    elif ("User.8" in file):
                        u8 = 1
                    elif ("User.9" in file):
                        u9 = 1
                num = u1 + u2 + u3 + u4 + u5 + u6 + u7 + u8 + u9
                fl=open("DATA/usernum.txt","w")
                fl.write(str(num))
                fl.close()
                t.ht()
                t.pu()
                t.goto(0,0)
                t.pd()
                t.pencolor("#4d0099")
                t.write("By now, you have "+str(num)+" saved faces trained!", align="center", font=("Broadway", 12))
                button_design(3,"Deleting Face","Test Locker","Adding Face")
                def buttonn(x,y):
                    if x > -255 and x < -105 and y < -30 and y > -90:
                        files = os.listdir('DATA/FData')
                        fl=open("DATA/usernum.txt","r")
                        num=int(fl.read())
                        fl.close()
                        if(num==0):
                            pyautogui.alert("You don't have any face yet!", 'Notification', 'I understand!')
                        else:
                            command = scr.textinput("Input", "Please enter the number-ID of that face:")
                            while command not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] and(command != None):
                                pyautogui.alert('Please enter a valid one char number!', 'Notification', 'I understand!')
                                command = scr.textinput("Input", "Please enter a valid number-ID from 1 to 9:")
                            c = 0
                            if command in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                                for file in files:
                                    if ('User.' + str(command) in file):
                                        os.remove('DATA/FData/' + file)
                                        c += 1
                                if (c > 100)or(c==1):
                                    if (num > 1):
                                        result = trainer(scr, t)
                                    else:
                                        os.remove('DATA/TData.yml')
                                        result = 'ok'
                                        fl=open("DATA/usernum.txt","w")
                                        fl.write("0")
                                        fl.close()
                                    if (result == 'ok'):
                                        pyautogui.alert('Deleting the face was successfull!', 'Notification', 'I understand!')
                                        main_menu()
                                    else:
                                        errpage()
                                else:
                                    pyautogui.alert("There's no trained data to be deleted!", 'Notification', 'I understand!')
                                    main_menu()
                    if x < 75 and x > -75 and y < -30 and y > -90:
                        fl = open("DATA/usernum.txt", "r")
                        num = int(fl.read())
                        fl.close()
                        if(num==0):
                            pyautogui.alert("You don't have any face yet!", 'Notification', 'I understand!')
                        else:
                            os.startfile("LOCKER.exe")
                        main_menu()
                    if x < 255 and x > 105 and y < -30 and y > -90:
                        files = os.listdir('DATA/FData')
                        fl = open("DATA/usernum.txt", "r")
                        num = int(fl.read())
                        fl.close()
                        command = scr.textinput("Input", "Please enter a valid number-ID from 1 to 9:")
                        while command not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] and (command != None):
                            pyautogui.alert('Please enter a valid one char number!', 'Notification', 'I understand!')
                            command = scr.textinput("Input", "Please enter a valid number-ID from 1 to 9:")
                        if command in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            dn = 0
                            for file in files:
                                if ('User.' + str(command) in file):
                                    dn = 1
                            while dn == 1:
                                pyautogui.alert('This number is used!', 'Notification', 'I understand!')
                                command = scr.textinput("Input", "Please enter a valid number-ID from 1 to 9:")
                                dn = 0
                                for file in files:
                                    if ('User.' + str(command) in file):
                                        dn = 1
                            result = recorder(command, 100, scr, t)
                            if (result == 'ok'):
                                print('ok')
                                result = trainer(scr, t)
                                if (result == 'ok'):
                                    scr.clearscreen()
                                    scr.bgcolor("#e6ccff")
                                    t.write("Please set a certian pin-code.", align="center", font=("Broadway", 13))
                                    t.ht()
                                    t.pu()
                                    t.goto(0, -180)
                                    t.pd()
                                    t.pencolor("red")
                                    t.write("You must keep this pin-code!", align="center", font=("Broadway", 10))
                                    pincode = command = scr.textinput("Input", "Please enter your pin-code:")
                                    file = open("DATA/pin.txt", "w")
                                    file.write(pincode)
                                    file.close()
                                    scr.clearscreen()
                                    scr.bgcolor("#e6ccff")
                                    t.pencolor("black")
                                    t.write("Progress is done!", align="center", font=("Broadway", 13))
                                    t.ht()
                                    t.pu()
                                    t.goto(0, -180)
                                    t.pd()
                                    t.pencolor("red")
                                    t.write("Now software can detect your face!", align="center", font=("Broadway", 10))
                                    t.pu()
                                    t.goto(0, -205)
                                    t.pd()
                                    t.pencolor("red")
                                    t.write("You can pass detection by using 'p' key!", align="center",
                                            font=("Broadway", 10))
                                    time.sleep(5)
                                    fl=open("DATA/usernum.txt","w")
                                    fl.write("1")
                                    fl.close()
                                    main_menu()
                            else:
                                errpage
                def mmenu():
                    main_menu()
                t.onscreenclick(buttonn, 1, add=False)
                scr.onkey(mmenu, 'Escape')
                scr.listen()
                t.done()
            except:
                errpage()
        def buton2(x,y):
            try:
                file = open("DATA/dtcheck.txt","w")
                file.write("0")
                file.close()
                pyautogui.alert("BYE-BYE! :)",'Notification', 'BB :)')
                os._exit(0)
            except:
                errpage()
        def buton3(x,y):
            try:
                file = open("DATA/dtcheck.txt","w")
                file.write("0")
                file.close()
                scr.title("Codoffee FreezeWall 2.1")
                scr.clearscreen()
                scr.bgcolor('#e6ccff')
                t.ht()
                t.pu()
                t.goto(0, 0)
                t.pd()
                t.pencolor("#4d0099")
                t.write("What is your command?", align="center",font=("Broadway", 12))
                button_design(2,"Deleting Photos","null","Showing Reports")
                def buttonn(x,y):
                    if x > -255 and x < -105 and y < -30 and y > -90:
                        files = os.listdir('DATA/FData')
                        files.pop(0)
                        for file in files:
                            os.remove("DATA/FData/" + file)
                        pyautogui.alert('Deleting photos has been done successfully!', 'Notification', 'I understand!')
                        main_menu()
                    if x > 105 and x < 255 and y < -30 and y > -90:
                        try:
                            os.startfile('log.txt')
                            main_menu()
                        except:
                            errpage()
                def mmenu():
                    main_menu()
                t.onscreenclick(buttonn, 1, add=False)
                scr.onkey(mmenu, 'Escape')
                scr.listen()
                t.done()
            except:
                errpage()
        def buton4(x,y):
            try:
                file = open("DATA/dtcheck.txt", "w")
                file.write("0")
                file.close()
                scr.title("Codoffee FreezeWall 2.1")
                scr.clearscreen()
                scr.bgcolor('#e6ccff')
                t.ht()
                t.pu()
                t.goto(0, 150)
                t.pd()
                t.pencolor("red")
                t.write("Codoffee FreezeWall v2.1", align="center", font=("Broadway", 16))
                t.pu()
                t.goto(-40, -210)
                t.pd()
                t.pencolor("black")
                t.write('''
                The colabration result of two friends!
                [ Aria Izanlou & Amirhossein Safarzadeh ]
                
                They released the first free-bug version(v1.3) when
                they were 14.y.o for their school camputer project! 
                Hope, you enjoyed our product. 
                
                Huge tnx to : mjrovai -github_repository-
                Redesigned by : I.T.I Programming APIs
                G-UI by : Aria Izanlou
                        ''', align="center", font=("Candara Light", 13))
                time.sleep(10)
                main_menu()
            except:
                errpage()
        def date_time():
            dt=t.Turtle()
            tm=t.Turtle()
            dt.speed(0)
            tm.speed(0)
            jdatetime.set_locale('fa_IR')
            tm.pu()
            tm.goto(-240, 220)
            tm.pd()
            dt.pu()
            dt.goto(270, 220)
            dt.pd()
            dt.ht()
            tm.ht()
            dt.ht()
            tm.ht()
            dt.fd(1)
            tm.fd(1)
            while True:
                file = open("DATA/dtcheck.txt", "r")
                dtval = file.read()
                file.close()
                if(dtval=="1"):
                    now=datetime.now()
                    now_date=jdatetime.datetime.now().strftime("%Y/%m/%d")
                    now_time=jdatetime.datetime.now().strftime("%H:%M")
                    dt.undo()
                    tm.undo()
                    dt.pencolor("black")
                    tm.pencolor("black")
                    dt.write(now_time,align="center",font=("Microsoft YaHei UI Light",15))
                    tm.write(now_date,align="center",font=("Microsoft YaHei UI Light",15))
                    time.sleep(1)
        rview()
        main_menu()
        thread1=Thread(target=date_time,args=[])
        thread1.start()
        t.mainloop()
    except:
        pass

except:
    pass


#Codoffee FreezeWall Version 2.1
#I.T.I-Certified:: BY Aria Izanlou - <573 Lines>
