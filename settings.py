# Joshua Erickson, joshmerickson19@gmail.com, F-Zero Machine Generator Python Implementation
"""Saves settings for modifiers used by randomizer."""
from functions import bcolors

class Settings:
    """Contains all settings related to element randomization."""
    def __init__(self, use_middle_name = False, 
                 use_last_name = True, 
                 use_all_names = False, 
                 use_all_morphemes = False, 
                 use_all_circuits = False,
                 batches = 1):
        
        self.use_middle_name = use_middle_name
        self.use_last_name = use_last_name
        self.use_all_names = use_all_names
        self.use_all_morphemes = use_all_morphemes
        self.use_all_circuits = use_all_circuits
        self.batches = batches
    
    # Mutator Functions Declarations
    def toggleMiddle(self, option):
        """Changes useMiddleName setting to option specified (True/False)."""
        self.use_middle_name = option 
    
    def toggleLast(self, option):
        """Changes useLastName setting to option specified (True/False)."""
        self.use_last_name = option

    def toggleAllNames(self, option):
        """Changes useAllNames setting to option specified (True/False)."""
        self.use_all_names = option 

    def toggleAllMorphemes(self, option):
        """Changes useAllMorphemes setting to option specified (True/False)."""
        self.use_all_morphemes = option

    def toggleAllCircuits(self, option):
        """Changes useAllCircuits setting to option specified (True/False)."""
        self.use_all_circuits = option

    def changeBatches(self, number):
        """Changes batches setting to number specified."""
        self.batches = number

    # Print Function
    def printSettings(self):
        print("""\tUse all pilot name lists: {}{}{}
        Include pilot middle name: {}{}{}
        Include pilot last name: {}{}{}
        Use all machine prefixes and suffixes: {}{}{}
        Use all circuit prefixes and suffixes: {}{}{}
        Batch size: {}{}{}
              """.format(bcolors.yellow,
                         self.use_all_names,
                         bcolors.end,
                         bcolors.yellow,
                         self.use_middle_name, 
                         bcolors.end,
                         bcolors.yellow,
                         self.use_last_name, 
                         bcolors.end,
                         bcolors.yellow,
                         self.use_all_morphemes, 
                         bcolors.end,
                         bcolors.yellow,
                         self.use_all_circuits,
                         bcolors.end, 
                         bcolors.cyan,
                         self.batches,
                         bcolors.end
                         ))
