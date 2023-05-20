import random
import time

typesTime = {
    "typping": {
        "max": 2,
        "min": 0.5
    }
}

def executeSleep(type):
    randomTime = random.uniform(typesTime[type]["min"], typesTime[type]["min"])
    time.sleep(randomTime)