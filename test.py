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
rect = window.rectangle()
window_x = rect.left
window_y = rect.top
runTimes = 1

#getCoordinates(window, reader)
#moveRoad((188,28), (196,34))
moveRoad((196,34), (188,28))
