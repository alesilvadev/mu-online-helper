import easyocr
import time
from imageOCR import analizeImage
from windowService import getWindow,takeScreenShoot, getMiddleCoordinates
from mouseService import moveCursor, clickCursor, release_key, press_key
from mapService import getCoordinates, moveRoad
from chatService import chatKeepAlive
import keyboard

run = True
print("starting")
reader = easyocr.Reader(['en'], gpu=True)
window = getWindow("Hakom")
middleCoordinates = getMiddleCoordinates(window)
initialCoordinates = getCoordinates(window,reader)
rect = window.rectangle()
window_x = rect.left
window_y = rect.top
runTimes = 1
notPickedUp = 1


def stop_running(e):
    print("stopping...")
    print(e.name)
    global run
    if(e.name == 'esc' or e.name == "delete"):
        run = False
        
def run_kep_alive():
    global runTimes
    global initialCoordinates
    release_key()
    chatKeepAlive()
    time.sleep(0.2)
    press_key()
    time.sleep(1)
    currentCordinates = getCoordinates(window,reader)
    if(currentCordinates != None and initialCoordinates != None):
        moveRoad(initialCoordinates, currentCordinates)
    runTimes = 1

def running_process():
    global runTimes
    global notPickedUp
    
    if(runTimes == 150):
        run_kep_alive()
        time.sleep(1)
        return
    takeScreenShoot(window)
    items =  analizeImage(reader, window_x, window_y, middleCoordinates)
    if(len(items) > 0):
        for item in items:
            print(f"Levantando: {item['name']}")
            moveCursor(item["coords"]["x"], item["coords"]["y"])
            press_key()
            time.sleep(0.3)
            clickCursor(item["coords"]["x"], item["coords"]["y"])
    else: 
        notPickedUp = notPickedUp + 1
    time.sleep(1.7)
    runTimes = runTimes + 1

keyboard.on_press(stop_running)

while(run):
    if(notPickedUp >= 20):
        run_kep_alive()
        notPickedUp = 1
    else:
        running_process()

release_key()
print("finished")


