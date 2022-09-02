from actions import *
import pyautogui
from time import sleep
import pyperclip
sleep(3)
# Lesson5Dispatch7
# no_of_lines=[11,11,8, 7, 8, 9, 6, 6, 9, 6, 10, 11, 7, 10, 11, 8, 6, 7, 9, 13, 8, 8, 9, 9, 13, 7, 9, 8, 6, 11, 9, 8, 10, 9, 7, 11, 8, 9, 9, 9, 6]
# Conclusion
# no_of_lines=[7, 9, 10, 5, 8]
# lesson7
# no_of_lines=[10, 10, 8, 7]
# lesson8
# no_of_lines=[9, 11, 8, 9, 9, 11, 8]
# lesson14
# no_of_lines=[10, 12, 8, 9, 13, 7, 8, 12, 11]
no_of_lines=[10]
for i in range(len(no_of_lines)):
    # bucket=[]
    for j in range(no_of_lines[i]-1):
        pyautogui.leftClick(1226,332+j*22)
        pyautogui.moveTo(1106,120)
        pyautogui.leftClick()
        copy()
        pyautogui.write(str(float(pyperclip.paste())-1))
    #     bucket.append(pyperclip.paste())

    # timmings.append(bucket)
    next_slide()