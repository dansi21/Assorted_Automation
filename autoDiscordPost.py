import time
import pyautogui as ui
import random as rand

input("press Any Key, Then A 5 Second Timer Will Await Mouse Location\n")




for x in range(1,5):
    print(f"{x}\n")
    time.sleep(1)

x, y = ui.position()

input(f"Confirm Mouse Location Is {x}:{y}\nAnd Copy Discord Message")

while(True):
    timeToWait = 900 + rand.randint(1, 120)
    print(f"Posted at time {time.time()}")
    ui.click(x,y)
    ui.click()
    ui.hotkey('ctrl','v')
    ui.press('enter')
    time.sleep(timeToWait)


