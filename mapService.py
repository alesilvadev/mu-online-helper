from windowService import takeCustomScreenShoot
from mouseService import moveUp, moveDown, moveLeft, moveRight
import time

def getCoordinates(window, reader):
    takeCustomScreenShoot(window, 15, 850, 130, 50, "coordinates")
    time.sleep(0.5)
    results = reader.readtext('images/coordinates.jpg')
    print(results)
    try:
        coordinates = (results[0][1], results[1][1])
        return coordinates
    except:
        return None


def moveRoad(initalCoordinates, currentCoordinates):
    camino = []
    dx = int(initalCoordinates[0]) - int(currentCoordinates[0])
    dy = int(initalCoordinates[1]) - int(currentCoordinates[1])
    
    print(dx)
    print(dy)

    while dx != 0:
        if dx > 0:      
            moveDown()
            time.sleep(0.5)
            dx -= 1
        else:
            moveUp()
            time.sleep(0.5)
            dx += 1

    while dy != 0:
        if dy > 0:
            moveRight()
            time.sleep(0.5)
            dy -= 1
        else:
            moveLeft()
            dy += 1

    return camino