# Joshua Erickson, joshmerickson19@gmail.com, F-Zero Machine Generator Python Implementation
"""Saves settings for modifiers used by randomizer."""

class Settings:
    """Contains all settings related to element randomization."""
    def __init__(self, useMiddleName = False, 
                 useLastName = True, 
                 useAllNames = False, 
                 useAllMorphemes = False, 
                 useAllCircuits = False,
                 batches = 1):
        
        self.useMiddleName = useMiddleName
        self.useLastName = useLastName
        self.useAllNames = useAllNames
        self.useAllMorphemes = useAllMorphemes
        self.useAllCircuits = useAllCircuits
        self.batches = batches
    
    def toggleMiddle(self, option):
        """Changes useMiddleName setting to option specified (True/False)."""
        self.useMiddleName = option 
    
    def toggleLast(self, option):
        """Changes useLastName setting to option specified (True/False)."""
        self.useLastName = option

    def toggleAllNames(self, option):
        """Changes useAllNames setting to option specified (True/False)."""
        self.useAllNames = option 

    def toggleAllMorphemes(self, option):
        """Changes useAllMorphemes setting to option specified (True/False)."""
        self.useAllMorphemes = option

    def toggleAllCircuits(self, option):
        """Changes useAllCircuits setting to option specified (True/False)."""
        self.useAllCircuits = option

    def changeBatches(self, number):
        """Changes batches setting to number specified."""
        self.batches = number