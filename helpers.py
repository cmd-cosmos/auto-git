#pylint: disable=C0114
#pylint: disable=C0303
#pylint: disable=C0305
#pylint: disable=C0411

import time
import sys
import os
import pyttsx3
import threading
import pygame
from art import bat3

def speak(lines):
    '''
    helper function to speak lines passed in.
    '''
    engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    engine.setProperty('rate', 180)
    if isinstance(lines, int):
        lines = str(lines)

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
        time.sleep(2)
        print("I am Vengeance")
        time.sleep(2)
        print("I am the Night")
        time.sleep(3)
        print("I am Batman")
        time.sleep(2)
        print(bat3)
        time.sleep(4)
        print("\nCleaning screen...")
        time.sleep(1)
        os.system("cls")
        sys.exit()
    elif mode == 1:
        print("Debug mode...")
        print("skipping art sequence...")
    else:
        # no mode signifies screen cleanup and then display art
        os.system("cls")
        print("\n#### Running standard cleanup routine ####\n")
        print("Showing cool art before repo status display...")
        time.sleep(2)
        os.system("cls")
        time.sleep(2)
        print("I am Vengeance")
        time.sleep(2)
        print("I am the Night")
        time.sleep(3)
        print("I am Batman")
        time.sleep(2)
        print(bat3)
        time.sleep(4)
        print("Fetching repo status...")
        time.sleep(2)
        os.system("git status")
        print()
        time.sleep(1)
        sys.exit()

def play_outro():
    '''
    helper function to play outro clip
    '''
    pygame.mixer.init()
    pygame.mixer.music.load('batman_soundtrack.mp3')
    pygame.mixer.music.play()

def conc_outro(mode_bit):
    '''
    concurrent show art and play outro sequence.
    '''
    t1 = threading.Thread(target=play_outro, daemon=True)
    t2 = threading.Thread(target=show_art, args=(mode_bit,))
    t2.start()
    time.sleep(2)
    t1.start()
    t2.join()

if __name__ == "__main__":
    
    show_art(mode=1)

    # speak("hello there")
    # speak("prerequisite routines executed")
    # speak("Target directory set")

    # test_lines = ["I am Vengeance",
    #               "I am the Night",
    #               "I am Batman"]
    # for line in test_lines:
    #     speak(line)

    # t1 = threading.Thread(target=play_outro, daemon=True)
    # t2 = threading.Thread(target=show_art)

    # t2.start()
    # time.sleep(2)
    # t1.start()

    # t2.join()

    conc_outro(mode_bit=None)
    conc_outro(mode_bit=0)
    # time.sleep(15)


