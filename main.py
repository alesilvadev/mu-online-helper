import easyocr
import time
from imageOCR import analizeImage
from windowService import getWindow,takeScreenShoot, getMiddleCoordinates
from mouseService import moveCursor, clickCursor, release_key, press_key
from chatService import chatKeepAlive
import keyboard

run = True
print("starting")
reader = easyocr.Reader(['en'], gpu=True)
window = getWindow("Hakom")
middleCoordinates = getMiddleCoordinates(window)
rect = window.rectangle()
window_x = rect.left
window_y = rect.top
runTimes = 1


def stop_running(e):
    print("stopping...")
    print(e.name)
    global run
    if(e.name == 'esc' or e.name == "delete"):
        run = False
        
def running_process():
    global runTimes
    if(runTimes == 150):
        release_key()
        print("chatting")
        chatKeepAlive()
        press_key()
        runTimes = 1
    takeScreenShoot(window)
    items =  analizeImage(reader, window_x, window_y, middleCoordinates)
    if(len(items) > 0):
        for item in items:
            print(f"Levantando: {item['name']}")
            moveCursor(item["coords"]["x"], item["coords"]["y"])
            press_key()
            time.sleep(0.3)
            clickCursor(item["coords"]["x"], item["coords"]["y"])
    time.sleep(1.7)
    runTimes = runTimes + 1

keyboard.on_press(stop_running)

while(run):
    running_process()

release_key()
print("finished")


