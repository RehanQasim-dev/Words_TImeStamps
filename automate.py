arr=[]
import pyautogui
import time
from actions import *
def array_generator(array):
    if array[0]=='f':
        return ['0']*4+[str(array[i]) for i in range(1,len(array))]
    else:
        return ['0','1','1']+[str(round(array[i]+1,2)) for i in range(1,len(array))]
generated_array=[]
for i in arr:
    generated_array.append(array_generator(i))
time.sleep(3)
for i in generated_array:
    print(i)
    for j in range(len(i)):
        print(j)
        pyautogui.leftClick(1226,242+j*22)
        pyautogui.leftClick(1106,120)
        pyautogui.write(i[j])
    next_slide()


