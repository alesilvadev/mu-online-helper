import pywinauto.findwindows as findwindows
from config import CHARACTER_NAME, COORDINATES_SCREEN_SIZE, WINDOW_SCREEN_SIZE
from PIL import Image
import pywinauto
import os
import time
from PIL import ImageGrab


def getHwnd():
    hwnd = findwindows.find_windows(title_re=f".*{CHARACTER_NAME}.*", visible_only=True)
    return hwnd[0]

def getWindow():
    hwnd = getHwnd()
    app = pywinauto.Application().connect(handle=hwnd)
    window = app.top_window()
    return window

def takeScreenShoot(window):
    img = window.capture_as_image()
    width, height = img.size
    img = img.crop((COORDINATES_SCREEN_SIZE[WINDOW_SCREEN_SIZE]["CROPPED_IMAGE"]["x"], COORDINATES_SCREEN_SIZE[WINDOW_SCREEN_SIZE]["CROPPED_IMAGE"]["y_start"], width, COORDINATES_SCREEN_SIZE[WINDOW_SCREEN_SIZE]["CROPPED_IMAGE"]["y_end"]))    
    img.save(os.path.join(os.getcwd(), "images/screen.jpg"), quality=25)
    time.sleep(0.1)

def takeCustomScreenShoot(window, x , y, width, height,  filename):
    sector = window.capture_as_image().crop((x, y, x + width, y + height))
    sector.save(os.path.join(os.getcwd(), f"images/{filename}.jpg"))
    time.sleep(0.1)

def getMiddleCoordinates(window):
    rect = window.rectangle()
    coord_x = int(rect.left + rect.width() / 2) -230
    coord_y = int(rect.top + rect.height() / 2) - 180
    return {"x": coord_x, "y": coord_y, "width": rect.width(), "height": rect.height()}

def resizeCropped(coords):
    orginalCoords = [(x+ COORDINATES_SCREEN_SIZE[WINDOW_SCREEN_SIZE]["CROPPED_IMAGE"]["x"] , y + COORDINATES_SCREEN_SIZE[WINDOW_SCREEN_SIZE]["CROPPED_IMAGE"]["y_start"]) for x, y in coords]
    return orginalCoords
