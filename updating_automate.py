from actions import *
import pyautogui
from time import sleep
sleep(3)
no_of_lines=[10, 9, 9, 11, 9, 6, 11, 8, 7, 9, 6, 8, 8, 8, 8, 10, 11, 10, 9, 6, 7, 6, 6, 7, 8, 7, 8, 11, 11, 9, 9, 10, 10, 11, 10, 10, 8, 8, 9, 7, 11, 6, 6, 10, 12, 9, 8, 10, 12]
for i in range(len(no_of_lines)):
    for j in range(no_of_lines[i]-1):
        pyautogui.leftClick(1226,332+j*22)
        pyautogui.leftClick(1133,126)
        pyautogui.leftClick()
        pyautogui.leftClick()
        pyautogui.leftClick()
    next_slide()