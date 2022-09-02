import pyautogui
import time
# time.sleep()
def copy():
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')
def exit():
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
def paste():
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')
def select_all():
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
def toggle():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
def to_desktop():
    pyautogui.keyDown('win')
    pyautogui.press('d')
    pyautogui.keyUp('win')
def save():
    pyautogui.keyDown('ctrl')
    pyautogui.press('s')
    pyautogui.keyUp('ctrl')
def next_slide():
    pyautogui.moveTo(1141,673)
    time.sleep(0.5)
    pyautogui.leftClick()


