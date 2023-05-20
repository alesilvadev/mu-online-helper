from keyboardService import touchSystemCharacter, typeWords
from timeService import executeSleep
import random

texts = ["lg", "laaaag", "lggggg", "+", "laggg" "lllag" + "+++++++++", "lgg"]

def chatKeepAlive():
    touchSystemCharacter(0x0D)
    typeWords(random.choice(texts))
    executeSleep("typping")
    touchSystemCharacter(0x0D)