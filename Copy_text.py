import pyautogui
import time
from actions import *
time.sleep(2)
# print(pyautogui.position())
for i in range(2,11):
    pyautogui.leftClick(605,500)
    select_all()
    copy()
    to_desktop()
    pyautogui.rightClick(1117,149)
    pyautogui.press('down',presses=11)
    pyautogui.press('right')
    pyautogui.press('up',presses=3)
    pyautogui.press('enter')
    pyautogui.write(f'Media{i}')
    pyautogui.press('enter',presses=2)
    time.sleep(0.75)
    paste()
    save()
    exit()
    toggle()
    next_slide()


