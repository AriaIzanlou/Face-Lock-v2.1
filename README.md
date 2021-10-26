# Face-Lock-v2.1
Face lock application which can process the entering of windows using your face! It's called "Codoffee Freeze Wall", The base code was for a startup called Codoffee Programming Group and since it's 1.3 release, It has developed by I.T.I Cloud API.

  There are 3 main files in the repository's main folder! These are "SETTINGS.pyw", "LOCKER.pyw" and "AUTORUN.pyw"; The first one creates and trains your face using machine learning arrays, The seconde one reads the trained data "TData.yml" and matches it's arrays with the one that will take from your face during the login process! And the third one makes sure that run the "LOCKER.pyw" when ever you press the hotkey "Win + ~" action!
  
  Required libraries:
    opencv-python==4.5.1.48
    opencv-contrib-python==4.5.1.48
    pyautogui
    pillow
    jdatetime
    numy
    playsound==1.2.2
    keyboard
    screeninfo
    pynput
