# Joshua Erickson, joshmerickson19@gmail.com, F-Zero Machine Generator Python Implementation
"""Contains all method and list declarations used for generation of machine names."""
from methods import readNames, chooseContent

# To-Do: Add additional machine info (Body, Boost, Grip, Weight, Made By)

# Methods to populate morpheme lists
# Populate Prefixes
prefixes = []
prefixes = readNames(prefixes, 'prefixes.txt')

# Populate Suffixes
suffixes = []
suffixes = readNames(suffixes, 'suffixes.txt')

# Populate All Machine morphemes
morphemes = sorted(prefixes + suffixes)


# Methods to pick Machine Prefix and Suffix
def pickMachinePrefix(listselect):
    """Return randomly picked machine prefix."""
    prefixpick = chooseContent(listselect, prefixes, morphemes)
    return prefixpick

def pickMachineSuffix(listselect):
    """Return randomly picked machine suffix."""
    suffixpick = chooseContent(listselect, suffixes, morphemes)
    return suffixpick


# Method to assemble full machine name
def AssembleMachine(listselect):
    """Return string containing machine prefix and suffix combined."""
    machinetitle = pickMachinePrefix(listselect) + ' ' + pickMachineSuffix(listselect)
    return machinetitle