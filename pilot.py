# Joshua Erickson, joshmerickson19@gmail.com, F-Zero Machine Generator Python Implementation
"""Contains all function and list declarations used for generation of pilot names."""
import random
from functions import readNames, chooseContent

# Functions to populate name lists
# Populate First Names
first_names = []
first_names = readNames(first_names, 'firstnames.txt')

# Populate Middle Names
middle_names = []
middle_names = readNames(middle_names, 'middlenames.txt')

# Populate Last Names
last_names = []
last_names = readNames(last_names, 'lastnames.txt')

# Populate All Pilot Names
all_names = sorted(first_names + middle_names + last_names)

class PilotData:
    """Contains data for a pilot
    
    Planned for future integration."""
    def __init__(self, f_name, age, sex, m_name=None, l_name=None):
        self.age = age
        self.sex = sex
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name


# Functions to pick Pilot first name, middle name, last name
def pickPilotFName(name_select):
    """Return randomly picked pilot first name."""
    f_name_pick = chooseContent(name_select, first_names, all_names)
    return f_name_pick

def pickPilotMName(name_select):
    """Return randomly picked pilot middle name."""
    m_name_pick = chooseContent(name_select, middle_names, all_names)
    return m_name_pick

def pickPilotLName(name_select):
    """Return randomly picked pilot last name."""
    l_name_pick = chooseContent(name_select, last_names, all_names)
    return l_name_pick

def pickPilotNumber():
    """Return randomly picked pilot number."""
    p_num_pick = random.randrange(100)
    return p_num_pick

def pickPilotAge():
    """Return randomly picked pilot age."""
    age_pick = random.randrange(100)
    return age_pick

def pickPilotSex():
    "Return randomly picked pilot sex"
    sex_pick = "Male" if random.randrange(2) == 0 else "Female"
    return sex_pick

# Functions to assemble full pilot information
def assemblePilot(name_select, middle_option, last_option):
    """Return string containing pilot first name, middle name, and last name combined.
    
    Uses user input from main.py to decide whether or not to include middle name/last name."""
    if (middle_option == True):
        pilot_name = pickPilotFName(name_select) + ' ' + pickPilotMName(name_select) + ' ' + pickPilotLName(name_select)
    elif(last_option == True):
        pilot_name = pickPilotFName(name_select) + ' ' + pickPilotLName(name_select)
    else:
        pilot_name = pickPilotFName(name_select)
    return pilot_name

def assemblePilotNumber():
    """Return string containing pilot number, 00 zero padding."""
    pilot_number = "NO. " + str(pickPilotNumber()).zfill(2)
    return pilot_number