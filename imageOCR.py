import math
import cv2
import numpy as np
from inventoryService import isInventoryFull, cleanInventory
import numpy as np
from scipy.spatial import distance_matrix
from scipy.optimize import linear_sum_assignment
import re
NAME_ITEM_DIFFERENCE = 30

def calculateCoords(coords, window_x, window_y):
    # Calcula el promedio de los puntos x y
    x_values = [coord[0] for coord in coords]
    y_values = [coord[1] for coord in coords]
    center_x = sum(x_values) / len(x_values)
    center_y = sum(y_values) / len(y_values)
    return {
        "x": int(center_x) + window_x,
        "y": int(center_y) + window_y + NAME_ITEM_DIFFERENCE
    }
    
def analizeImage(reader, window_x, window_y, middleCoordinates, needZen):
    points = []
    priority = []
    results = reader.readtext('images/screen.jpg')
    if(isInventoryFull(results) == True):
        cleanInventory()
        return []
    for result in results:
        text = result[1]
        coords = result[0]
        item = { "name": text, "coords": calculateCoords(coords, window_x, window_y, )}
        if(":" not in text and "Obtained" not in text):
            if(needZen == True and "Zen" in text and len(text) > 3 and len(text) < 12):
                points.append(item)
            if(("Jewel" in text and "Obtained" not in text) or isExceItem(result) == True):
                priority.append(item)
                break
        
    if(len(priority) > 0):
        return priority
    else:
        if(len(points) > 0):
            points = orderFromDistance(points, middleCoordinates["x"], middleCoordinates["y"])
            return [points[0]]
            #return antRoad(np.array([middleCoordinates["x"], middleCoordinates["y"]]), points)
        return []

def calculateDistance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def orderFromDistance(items, x_medio, y_medio):
    distances = []
    for item in items:
        x, y = item["coords"]['x'], item["coords"]['y']
        distance = calculateDistance(x, y, x_medio, y_medio)
        distances.append((item, distance))
    
    ordered_distances = sorted(distances, key=lambda d: d[1])
    
    ordered_items = [item for item, _ in ordered_distances]
    return ordered_items

def simplify_color(rgb_color):
    lab_color = cv2.cvtColor(np.uint8([[rgb_color]]), cv2.COLOR_RGB2LAB)[0][0]
    # Obtener el componente de tonalidad (hue)
    a_value = lab_color[1]
    # Clasificar el color en categorías generales
    if a_value < -20:
        return "red"
    elif a_value < 119 and a_value >= 116:
        return "green"
    else:
        return "gray"
    
def isExceItem(text):
    if(text[1].isdigit() == False):
        image = cv2.imread('images/screen.jpg')
        box = text[0]
        currentText = text[1]
        x_min, y_min = np.min(box, axis=0)
        x_max, y_max = np.max(box, axis=0)
        # Extraer la región de texto de la imagen original
        text_region = image[int(y_min):int(y_max), int(x_min):int(x_max)]
        # Calcular el color dominante de la región de texto
        dominant_color = np.mean(text_region, axis=(0, 1))
        simplified_color = simplify_color(dominant_color)
        if(simplified_color == "green" and len(currentText) > 5 and isValid(currentText) == True):
            return True
        return False
    return False

def isValid(text):
    patron = r'[A-Za-z+]+'
    return re.match(patron, text) is not None


def antRoad(pj, items):
    coords = np.array([list(item['coords'].values()) for item in items])
    todos_puntos = np.vstack([pj, coords])
    distancias = distance_matrix(todos_puntos, todos_puntos)
    row_ind, col_ind = linear_sum_assignment(distancias)
    orden_items = col_ind[1:] - 1
    return [items[i] for i in orden_items]