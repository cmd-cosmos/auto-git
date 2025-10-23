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


def show_art(mode=None):
    '''
    print punchlines and show art at end.
    '''

    if mode == 0:
        # set mode 0 when clean_flag == 'y'
        os.system("cls")
        print("\n#### Running complete cleanup routine ####\n")
        print("Showing cool art before complete cleanup...")
        time.sleep(2)
        os.system("cls")
        time.sleep(1)
        print("I am Vengeance")
        time.sleep(1)
        print("I am the Night")
        time.sleep(1)
        print("I am Batman")
        time.sleep(1)
        print(bat3)
        time.sleep(4)
        print("\nCleaning screen...")
        time.sleep(2)
        os.system("cls")
        sys.exit()
    else:
        # no mode signifies screen cleanup and then display art
        os.system("cls")
        print("\n#### Running standard cleanup routine ####\n")
        print("Showing cool art before repo status display...")
        time.sleep(2)
        os.system("cls")
        time.sleep(1)
        print("I am Vengeance")
        time.sleep(1)
        print("I am the Night")
        time.sleep(1)
        print("I am Batman")
        time.sleep(1)
        print(bat3)
        time.sleep(4)
        print("Fetching repo status...")
        time.sleep(2)
        os.system("git status")
        print()
        time.sleep(1)
        sys.exit()

if __name__ == "__main__":
    show_art()
