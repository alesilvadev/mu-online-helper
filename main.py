import easyocr
import time
from imageOCR import analizeImage
from windowService import getWindow,takeScreenShoot, getMiddleCoordinates
from mouseService import moveCursor, clickCursor, release_key, press_key
import keyboard

run = True
print("starting")
reader = easyocr.Reader(['en'], gpu=True)
window = getWindow("Hakom")
middleCoordinates = getMiddleCoordinates(window)
rect = window.rectangle()
window_x = rect.left
window_y = rect.top


def stop_running(e):
    print("stopping...")
    global run
    if e.name == 'esc':
        run = False
        
def running_process():
    takeScreenShoot(window)
    time.sleep(0.5)
    items =  analizeImage(reader, window_x, window_y, middleCoordinates)
    if(len(items) > 0):
        for item in items:
            print(f"Levantando: {item['name']}")
            moveCursor(item["coords"]["x"], item["coords"]["y"])
            press_key()
            time.sleep(0.5)
            clickCursor(item["coords"]["x"], item["coords"]["y"])
    time.sleep(2)

keyboard.on_press(stop_running)

while(run):
    running_process()

release_key()
print("finished")


