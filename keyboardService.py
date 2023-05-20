import ctypes
import time
import pyautogui


def touchSystemCharacter(key):
    ctypes.windll.user32.keybd_event(key, 0, 0, 0)
    time.sleep(0.2)
    ctypes.windll.user32.keybd_event(key, 0, 0x0002, 0)
    
def keepDownKey(key):
    ctypes.windll.user32.keybd_event(key, 0, 0, 0)
    
def releaseKey(key):
    ctypes.windll.user32.keybd_event(key, 0, 0x0002, 0)
    
def typeWords(words):
    pyautogui.typewrite(words)