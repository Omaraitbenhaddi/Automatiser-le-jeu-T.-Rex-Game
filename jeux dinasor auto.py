import pyautogui


while True :
    x=pyautogui.position()
    p=pyautogui.pixel(x[0],x[1])
    if p[0]==p[1] and p[1]==p[2] and p[2]==83 :
        pyautogui.hotkey('up')


