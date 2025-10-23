#pylint: disable=C0114
#pylint: disable=C0305

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
    pass

