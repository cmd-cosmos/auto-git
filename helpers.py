#pylint: disable=C0114
#pylint: disable=C0305

import time
import sys
import os
import pyttsx3
from art import bat3

def speak(lines):
    '''
    helper function to speak lines passed in.
    '''
    engine = pyttsx3.init()
    engine.say(lines)
    engine.runAndWait()


def show_art():
    '''
    print punchlines and show art at end.
    '''
    os.system("cls")
    print("Sequence complete...\n")
    time.sleep(1)
    print("I am Vengeance")
    time.sleep(1)
    print("I am the Night")
    time.sleep(1)
    print("I am Batman")
    time.sleep(1)
    print(bat3)
    time.sleep(4)
    sys.exit()

