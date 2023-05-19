from ctypes import *
from ctypes.wintypes import *
import time
import ctypes

#helpcode:
#ctypes.windll.user32.keybd_event(0x79, 0, 0, 0)  # Tecla F10


# Definir la estructura para el input del mouse
class MOUSEINPUT(Structure):
    _fields_ = [("dx", LONG),
                ("dy", LONG),
                ("mouseData", DWORD),
                ("dwFlags", DWORD),
                ("time", DWORD),
                ("dwExtraInfo", POINTER(ULONG))]

class KEYBDINPUT(Structure):
    _fields_ = [("wVk", WORD),
                ("wScan", WORD),
                ("dwFlags", DWORD),
                ("time", DWORD),
                ("dwExtraInfo", POINTER(ULONG))]

class HARDWAREINPUT(Structure):
    _fields_ = [("uMsg", DWORD),
                ("wParamL", WORD),
                ("wParamH", WORD)]

class INPUTunion(Union):
    _fields_ = [("mi", MOUSEINPUT),
                ("ki", KEYBDINPUT),
                ("hi", HARDWAREINPUT)]

class INPUT(Structure):
    _fields_ = [("type", DWORD),
                ("union", INPUTunion)]

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [("ki", ctypes.c_ulong * 3),
                    ("mi", MOUSEINPUT)]
    _anonymous_ = ("_input",)
    _fields_ = [("type", ctypes.c_ulong),
                ("_input", _INPUT)]
    

# Definir las constantes necesarias para la función
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040
MOUSEEVENTF_WHEEL = 0x0800
MOUSEEVENTF_VIRTUALDESK = 0x4000
MOUSEEVENTF_ABSOLUTE = 0x8000
INPUT_MOUSE = 0


# Funciones de ctypes necesarias para simular la pulsación de teclas
def press_key():
    ctypes.windll.user32.keybd_event(0x12, 0, 0, 0)
    
def release_key():
    ctypes.windll.user32.keybd_event(0x12, 0, 2, 0)

# Definir la función para mover el cursor y hacer clic
def clickMouse(x, y):
    # Crear el input para mover el cursor
    mouse_input = INPUT(INPUT_MOUSE, ctypes.c_ulong(0), (ctypes.c_ulong * 2)(x, y), ctypes.c_ulong(MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_MOVE))
    # Enviar el evento para mover el cursor
    ctypes.windll.user32.SendInput(1, ctypes.pointer(mouse_input), ctypes.sizeof(mouse_input))

    # Crear el input para el clic izquierdo
    mouse_input = INPUT(INPUT_MOUSE, ctypes.c_ulong(0), ctypes.c_ulong * 2, ctypes.c_ulong(MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_LEFTUP))
    # Enviar los eventos del clic
    ctypes.windll.user32.SendInput(2, ctypes.pointer(mouse_input), ctypes.sizeof(mouse_input))
    
def moveCursor(coord_x,coord_y):
    ctypes.windll.user32.SetCursorPos(int(coord_x), int(coord_y))

def moveCursor2(x, y):
    # Obtener el manejador de la ventana activa
    hnd = ctypes.windll.user32.GetForegroundWindow()
    
    # Obtener la posición de la ventana activa
    rect = ctypes.wintypes.RECT()
    ctypes.windll.user32.GetWindowRect(hnd, ctypes.byref(rect))
    
    # Calcular las coordenadas absolutas del cursor
    abs_x = int(rect.left) + x
    abs_y = int(rect.top) + y
    
    # Mover el cursor a las coordenadas absolutas
    ctypes.windll.user32.SetCursorPos(abs_x, abs_y)
    
def clickCursor(x, y):
    # Crear los inputs para el clic
    input_down = INPUT(INPUT_MOUSE, INPUT._INPUT(mi=MOUSEINPUT(x, y, 0, MOUSEEVENTF_LEFTDOWN, 0, None)))
    input_up = INPUT(INPUT_MOUSE, INPUT._INPUT(mi=MOUSEINPUT(x, y, 0, MOUSEEVENTF_LEFTUP, 0, None)))
    # Enviar los eventos del clic
    ctypes.windll.user32.SendInput(1, ctypes.pointer(input_down), ctypes.sizeof(INPUT))
    time.sleep(0.1)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(input_up), ctypes.sizeof(INPUT))
    
def maintainClickCursor(x, y):
    # Crear los inputs para el clic derecho
    input_down = INPUT(INPUT_MOUSE, INPUT._INPUT(mi=MOUSEINPUT(x, y, 0, MOUSEEVENTF_RIGHTDOWN, 0, None)))
    input_up = INPUT(INPUT_MOUSE, INPUT._INPUT(mi=MOUSEINPUT(x, y, 0, MOUSEEVENTF_RIGHTUP, 0, None)))
    
    # Enviar los eventos del clic
    ctypes.windll.user32.SendInput(1, ctypes.pointer(input_down), ctypes.sizeof(INPUT))
    # time.sleep(1)  # Pausa para mantener el botón presionado
    # ctypes.windll.user32.SendInput(1, ctypes.pointer(input_up), ctypes.sizeof(INPUT))
    
def turnOffMouse(x, y):
    input_up = INPUT(INPUT_MOUSE, INPUT._INPUT(mi=MOUSEINPUT(x, y, 0, MOUSEEVENTF_RIGHTUP, 0, None)))
    ctypes.windll.user32.SendInput(1, ctypes.pointer(input_up), ctypes.sizeof(INPUT))
    
def walkArround(center_x, center_y, coords):
    moveCursor(center_x, center_y - 20, coords["width"], coords["height"])
    time.sleep(1)
    clickCursor(center_x, center_y - 20)
    time.sleep(2)
    moveCursor(center_x, center_y + 40, coords["width"], coords["height"])
    time.sleep(1)
    clickCursor(center_x, center_y + 40)
    
def moveDown(screnWidth, screenHeight):
    moveCursor(300, 275, screnWidth, screenHeight)
    time.sleep(1)
    clickCursor(300, 300)
    clickCursor(300, 300)

def moveUp(screnWidth, screenHeight):
    moveCursor(255, 225, screnWidth, screenHeight)
    time.sleep(1)
    clickCursor(255, 225)
    clickCursor(255, 225)

def moveRight(screnWidth, screenHeight):
    moveCursor(305, 225, screnWidth, screenHeight)
    time.sleep(1)
    clickCursor(305, 225)
    time.sleep(0.1)
    clickCursor(305, 225)
    time.sleep(0.1)
    clickCursor(305, 225)

def moveLeft(screnWidth, screenHeight):
    moveCursor(250, 280, screnWidth, screenHeight)
    time.sleep(1)
    clickCursor(250, 280)
    time.sleep(0.1)
    clickCursor(250, 280)
    time.sleep(0.1)
    clickCursor(250, 280)