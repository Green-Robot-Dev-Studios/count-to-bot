import pyautogui
import time
print("NOTE: To stop at any time, close this window! This bot will write numbers in ascending order for as long as you set and press enter after each number.")
x = int(input("What number to start spamming from? | Recomended:0 | Input here then press enter: "))
a = int(input("What number do you want to stop at? | Recomended:1000 | Input here then press enter: "))
z = float(input("How fast does each number get typed in seconds? | Recomended:0.2 | Input here then press enter: "))
print("Starting in 5 seconds! Get ready!")
time.sleep(6)
def start() :
    while True:
        global x
        if x < a:
            x += 1
            y = str(x)
            pyautogui.typewrite(y, interval=z)
            pyautogui.press('enter')
        else:
            quit()
start()
