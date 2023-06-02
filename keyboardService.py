import ctypes
import time
import pyautogui
from config import SEND_WINDOWS_ALERT
from win10toast import ToastNotifier

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
    
def sendAlert(title, message):
    if(SEND_WINDOWS_ALERT == True):
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=10)