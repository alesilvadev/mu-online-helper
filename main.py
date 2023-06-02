import easyocr
import time
from imageOCR import analizeImage, analizeImageAPI
from windowService import getWindow,takeScreenShoot, getMiddleCoordinates
from mouseService import moveCursor, clickCursor, release_key, press_key
from mapService import getCoordinates, moveRoad
from chatService import chatKeepAlive
from config import OCR_PROCESSOR, SEND_WINDOWS_ALERT, PRINTING_ITEMS
import keyboard

print("starting")
run = True
reader = None
window = getWindow()
initialCoordinates = getCoordinates(window,reader)
rect = window.rectangle()
window_x = rect.left
window_y = rect.top
runTimes = 1
notPickedUp = 1

if(OCR_PROCESSOR == "LOCAL"):
    print("GPU PROCESSING")
    reader = easyocr.Reader(['en'], gpu=True)
else:
    print("API PROCESSING")

def stop_running(e):
    global run
    print(e.name)
    if(e.name == "delete" or e.name == "insert"):
        print("stopping...")
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
    items = []
    if(OCR_PROCESSOR == "LOCAL"):
        items =  analizeImage(reader, window_x, window_y)
    else:
        items = analizeImageAPI(window_x, window_y)
    if(len(items) > 0):
        for item in items:
            if(PRINTING_ITEMS == True):
                print(f"Levantando: {item['name']}")
            if(SEND_WINDOWS_ALERT != True):
                moveCursor(item["coords"]["x"], item["coords"]["y"])
                press_key()
                time.sleep(0.1)
                clickCursor(item["coords"]["x"], item["coords"]["y"])
                time.sleep(1)
            else:
                time.sleep(4)
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


