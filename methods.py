# Joshua Erickson, joshmerickson19@gmail.com, F-Zero Machine Generator Python Implementation
"""Contains various methods used to streamline populatation of several lists and randomly picking elements from lists."""
import random

"""Blender build scripts for terminal print usage"""
class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    
def readNames(list, filename):
    """Return populated list containing content from an opened .txt file.
    
    Reads content line by line, removes \n from entry.
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
        listpick = list[random.randrange(0, len(list))]
    else:
        listpick = all[random.randrange(0, len(all))]
    return listpick

def convertBool(command):
        """Takes a character and returns a boolean."""
        option = True if command == 'y' else False
        return option