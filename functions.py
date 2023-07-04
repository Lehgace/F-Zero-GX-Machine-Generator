# Joshua Erickson, joshmerickson19@gmail.com, F-Zero Machine Generator Python Implementation
"""Contains various functions used to streamline populatation of several lists and randomly picking elements from lists."""
import random

"""Blender build scripts for terminal print usage"""
class bcolors:
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    
def readNames(list, filename):
    """Return populated list containing content from an opened .txt file.
    
    Reads content line by line, removes newline character from entry.
    """
    filename = filename
    list = list
    with open('names/{}'.format(filename), 'r') as f:
        list = [line.strip() for line in f]
    return list

def chooseContent(boolean, list, all):
    """Return element picked from list.
    
    User specifies which list to use in main.py.
    Uses random randrange to randomly pick element from list."""
    if (boolean == False):
        list_pick = list[random.randrange(0, len(list))]
    else:
        list_pick = all[random.randrange(0, len(all))]
    return list_pick

def convertBool(command):
        """Takes a character and returns a boolean."""
        option = True if command == 'y' else False
        return option