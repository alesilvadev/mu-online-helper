import pywinauto.findwindows as findwindows
import pywinauto
import os
def getHwnd(player_name):
   # Conecta con la ventana del juego
    hwnd = findwindows.find_windows(title_re=f".*{player_name}.*", visible_only=True)
    return hwnd[0]

def getWindow(player_name):
   # Conecta con la ventana del juego
    hwnd = getHwnd(player_name)
    app = pywinauto.Application().connect(handle=hwnd)
    window = app.top_window()
    return window

def takeScreenShoot(window):
    img = window.capture_as_image()
    img.save(os.path.join(os.getcwd(), "images/screen.jpg"))

def getMiddleCoordinates(window):
    rect = window.rectangle()
    coord_x = int(rect.left + rect.width() / 2) -230
    coord_y = int(rect.top + rect.height() / 2) - 180
    return {"x": coord_x, "y": coord_y, "width": rect.width(), "height": rect.height()}