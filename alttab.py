import pyautogui
import time
import pyperclip

pyautogui.FAILSAFE = False

def altTab():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')
