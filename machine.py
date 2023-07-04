# Joshua Erickson, joshmerickson19@gmail.com, F-Zero Machine Generator Python Implementation
"""Contains all function and list declarations used for generation of machine names."""
from functions import readNames, chooseContent

# To-Do: Add additional machine info (Body, Boost, Grip, Weight, Made By)

# Functions to populate morpheme lists
# Populate Prefixes
prefixes = []
prefixes = readNames(prefixes, 'prefixes.txt')

# Populate Suffixes
suffixes = []
suffixes = readNames(suffixes, 'suffixes.txt')

# Populate All Machine morphemes
morphemes = sorted(prefixes + suffixes)


# Functions to pick Machine Prefix and Suffix
def pickMachinePrefix(list_select):
    """Return randomly picked machine prefix."""
    prefix_pick = chooseContent(list_select, prefixes, morphemes)
    return prefix_pick

def pickMachineSuffix(list_select):
    """Return randomly picked machine suffix."""
    suffix_pick = chooseContent(list_select, suffixes, morphemes)
    return suffix_pick


# Function to assemble full machine name
def assembleMachine(list_select):
    """Return string containing machine prefix and suffix combined."""
    machine_title = pickMachinePrefix(list_select) + ' ' + pickMachineSuffix(list_select)
    return machine_title