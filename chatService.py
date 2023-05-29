from keyboardService import touchSystemCharacter, typeWords
from timeService import executeSleep
from config import WRITE_MESSAGES_TEXTS,WRITE_MESSAGES
import random

def chatKeepAlive():
    if(WRITE_MESSAGES == True):
        touchSystemCharacter(0x0D)
        typeWords(random.choice(WRITE_MESSAGES_TEXTS))
        executeSleep("typping")
        touchSystemCharacter(0x0D)