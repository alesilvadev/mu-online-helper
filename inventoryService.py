

import time
import random
from mouseService import moveCursor, clickCursor
from keyboardService import touchSystemCharacter, keepDownKey, releaseKey
from config import CLEAN_INVENTORY, WINDOW_SCREEN_SIZE, COORDINATES_SCREEN_SIZE

START_POINT_INVENTORY_X = COORDINATES_SCREEN_SIZE[WINDOW_SCREEN_SIZE]["START_ANALYZE_INVENTORY"]["x"]
START_POINT_INVENTORY_Y = COORDINATES_SCREEN_SIZE[WINDOW_SCREEN_SIZE]["START_ANALYZE_INVENTORY"]["y"]
DROP_POINT_INVENTORY_X = COORDINATES_SCREEN_SIZE[WINDOW_SCREEN_SIZE]["DROP_ITEM"]["x"]
DROP_POINT_INVENTORY_Y = COORDINATES_SCREEN_SIZE[WINDOW_SCREEN_SIZE]["DROP_ITEM"]["y"]
MOVE_DISTANCE = COORDINATES_SCREEN_SIZE[WINDOW_SCREEN_SIZE]["MOVE_CELL_DISTANCE"] * 2
TOTAL_SPACES_PER_ROW = 4
TOTAL_SPACES = 64

#Random Drops
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
    if(CLEAN_INVENTORY == True):
        for result in texts:
            text = result[1]
            if("Inventory is full" in text):
                return True
    return False

def isFullZen(texts):
    for result in texts:
        text = result[1]
        if("exceeded the amount of Zen" in text):
            return True
    return False

def dropItem(x, y):
    moveCursor(x, y)
    time.sleep(0.4)
    clickCursor(x, y)
    time.sleep(0.8)
    moveCursor(DROP_POINT_INVENTORY_X, DROP_POINT_INVENTORY_Y)
    time.sleep(0.5)
    clickCursor(DROP_POINT_INVENTORY_X, DROP_POINT_INVENTORY_Y)
    
def garbageCollector():
    print("start garbage collector")
    MOVE_POINT_X = START_POINT_INVENTORY_X
    MOVE_POINT_Y = START_POINT_INVENTORY_Y

    for x in range(0, TOTAL_SPACES_PER_ROW - 1):
        for x in range(0, TOTAL_SPACES_PER_ROW):
            dropItem(MOVE_POINT_X, MOVE_POINT_Y)
            MOVE_POINT_X = MOVE_POINT_X + MOVE_DISTANCE
        MOVE_POINT_X = START_POINT_INVENTORY_X
        MOVE_POINT_Y = MOVE_POINT_Y + MOVE_DISTANCE
        time.sleep(0.5)
    print("end garbage collector")

def cleanInventory():
    time.sleep(0.3)
    touchSystemCharacter(0x56)
    time.sleep(0.3)
    garbageCollector()
    time.sleep(0.3)
    touchSystemCharacter(0x56)

def depositZen():
    pass
