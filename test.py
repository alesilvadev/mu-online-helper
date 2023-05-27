import time
import ctypes
import pygetwindow as gw

# Define las constantes necesarias para la función mouse_event de la API de Windows
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

# Espera 2 segundos antes de iniciar la acción
time.sleep(2)

# Obtiene la ventana activa
window = gw.getActiveWindow()

# Obtiene las coordenadas de la ventana activa
window_x, window_y, _, _ = window.left, window.top, window.width, window.height

# Define las coordenadas a las que se moverá el mouse (en este caso, 100 píxeles hacia la derecha y 100 píxeles hacia abajo)
target_x = window_x + 100
target_y = window_y + 100

# Mueve el mouse a las coordenadas especificadas
ctypes.windll.user32.SetCursorPos(target_x, target_y)

# Simula un clic izquierdo
ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)