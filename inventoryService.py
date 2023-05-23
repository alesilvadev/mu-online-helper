

import time
import random
from mouseService import moveCursor, clickCursor
from keyboardService import touchSystemCharacter, keepDownKey, releaseKey

START_POINT_INVENTORY_X = 1068
START_POINT_INVENTORY_Y = 390
MOVE_DISTANCE = 44 * 2
TOTAL_SPACES_PER_ROW = 8
TOTAL_SPACES = 64

MAXIMUM_X = 975
MINIMUM_X = 34
MAXIMUM_Y = 690
MINIMUM_Y = 154

def getCoordsToDrop():
    return{
        "x": random.randint(MINIMUM_X, MAXIMUM_X),
        "y": random.randint(MINIMUM_Y, MAXIMUM_Y),
    } 
    
def isInventoryFull(texts):
    for result in texts:
        text = result[1]
        if("Inventory is full" in text):
            return True
    return False

def dropItem(x, y):
    moveCursor(x, y)
    time.sleep(0.4)
    clickCursor(x, y)
    time.sleep(0.8)
    moveCursor(763, 863)
    time.sleep(0.5)
    clickCursor(763, 863)
    
def garbageCollector():
    print("start garbage collector")
    MOVE_POINT_X = START_POINT_INVENTORY_X
    MOVE_POINT_Y = START_POINT_INVENTORY_Y

    for x in range(0, TOTAL_SPACES_PER_ROW - 1):
        for x in range(0, TOTAL_SPACES_PER_ROW):
            dropItem(MOVE_POINT_X, MOVE_POINT_Y)
            MOVE_POINT_X = MOVE_POINT_X + 44
        MOVE_POINT_X = START_POINT_INVENTORY_X
        MOVE_POINT_Y = MOVE_POINT_Y + 44
        time.sleep(0.5)
    print("end garbage collector")

def cleanInventory():
    time.sleep(0.3)
    touchSystemCharacter(0x56)
    time.sleep(0.3)
    garbageCollector()
    time.sleep(0.3)
    touchSystemCharacter(0x56)

