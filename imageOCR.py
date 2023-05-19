import math

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
    
def analizeImage(reader, window_x, window_y, middleCoordinates):
    points = []
    results = reader.readtext('images/screen.jpg')
    for result in results:
        text = result[1]
        coords = result[0]
        if(("Jewel" in text and "Obtained" not in text) or "Zen" in text):
            points.append({
                "name": text,
                "coords": calculateCoords(coords, window_x, window_y, )
            })
    response = []
    points = orderFromDistance(points, middleCoordinates["x"], middleCoordinates["y"])
    for point in points:
        if("Jewel" in point["name"]):
            response.append(point)
    if(len(response) == 0 and len(points) > 0):
        response.append(points[0])
    return response


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