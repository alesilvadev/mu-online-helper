import easyocr
import time
from imageOCR import analizeImage
from windowService import getWindow,takeScreenShoot, getMiddleCoordinates
from mouseService import moveCursor, clickCursor, release_key, press_key
import keyboard
import torch
print(torch.cuda.is_available())