# Joshua Erickson, joshmerickson19@gmail.com, F-Zero Machine Generator Python Implementation
"""Contains all method and list declarations used for generation of pilot names."""
import random
from methods import readNames, chooseContent

# To-Do: add fields for additional pilot data (sex, age, bio?)

# Methods to populate name lists
# Populate First Names
firstnames = []
firstnames = readNames(firstnames, 'first names.txt')

# Populate Middle Names
middlenames = []
middlenames = readNames(middlenames, 'middle names.txt')

# Populate Last Names
lastnames = []
lastnames = readNames(lastnames, 'last names.txt')

# Populate All Pilot Names
allnames = sorted(firstnames + middlenames + lastnames)


# Methods to pick Pilot first name, middle name, last name
def pickPilotFName(nameselect):
    """Return randomly picked pilot first name."""
    fnamepick = chooseContent(nameselect, firstnames, allnames)
    return fnamepick

def pickPilotMName(nameselect):
    """Return randomly picked pilot middle name."""
    mnamepick = chooseContent(nameselect, middlenames, allnames)
    return mnamepick

def pickPilotLName(nameselect):
    """Return randomly picked pilot last name."""
    lnamepick = chooseContent(nameselect, lastnames, allnames)
    return lnamepick

def pickPilotNumber():
    """Return randomly picked pilot number."""
    pnumpick = random.randrange(0, 100)
    return pnumpick

# Methods to assemble full pilot information
def AssemblePilot(nameselect, middleoption, lastoption):
    """Return string containing pilot first name, middle name, and last name combined.
    
    Uses user input from main.py to decide whether or not to include middle name/last name."""
    if (middleoption == True):
        pilotname = pickPilotFName(nameselect) + ' ' + pickPilotMName(nameselect) + ' ' + pickPilotLName(nameselect)
    elif(lastoption == True):
        pilotname = pickPilotFName(nameselect) + ' ' + pickPilotLName(nameselect)
    else:
        pilotname = pickPilotFName(nameselect)
    return pilotname

def AssemblePilotNumber():
    """Return string containing pilot number, 00 zero padding."""
    pilotnumber = "NO. " + str(pickPilotNumber()).zfill(2)
    return pilotnumber