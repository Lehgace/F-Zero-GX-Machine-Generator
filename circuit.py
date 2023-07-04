# Joshua Erickson, joshmerickson19@gmail.com, F-Zero Machine Generator Python Implementation
"""Contains all function and list declarations used for generation of circuit titles."""
import random
from functions import readNames, chooseContent

# Functions to populate morpheme lists
# Populate Location Prefixes
loc_prefixes = []
loc_prefixes = readNames(loc_prefixes, 'locprefixes.txt')

# Populate Location Suffixes
loc_suffixes = []
loc_suffixes = readNames(loc_suffixes, 'locsuffixes.txt')

# Populate Track Prefixes
track_prefixes = []
track_prefixes = readNames(track_prefixes, 'trackprefixes.txt')

# Populate Track Suffixes
track_suffixes = []
track_suffixes = readNames(track_suffixes, 'tracksuffixes.txt')

# Populate All Track and Location morphemes
morphemes = sorted(loc_prefixes + loc_suffixes + track_prefixes + track_suffixes)

# Populate list of Circuit Titles
cups = ["Ruby", "Sapphire", "Emerald", "Diamond", "AX", "Jade", "Opal", "Amber", "Amethyst"]

class Circuit:
    """Prototype implementation of Circuit class"""
    def __init__(self, track_title = None, course_title = None, cup_title = None, circuit=[]):
        self.track_title = track_title
        self.course_title = course_title
        self.cup_title = cup_title
        self.circuit = circuit
    pass

# Functions to pick prefixes and suffixes for location and track, pick circuit
def pickLocPrefix(list_select):
    """Return randomly picked location prefix"""
    prefix_pick = chooseContent(list_select, loc_prefixes, morphemes)
    return prefix_pick

def pickLocSuffix(list_select):
    """Return randomly picked location suffix"""
    suffix_pick = chooseContent(list_select, loc_suffixes, morphemes)
    return suffix_pick

def pickTrackPrefix(list_select):
    """Return randomly picked track prefix"""
    prefix_pick = chooseContent(list_select, track_prefixes, morphemes)
    return prefix_pick

def pickTrackSuffix(list_select):
    """Return randomly picked track prefix"""
    suffix_pick = chooseContent(list_select, track_suffixes, morphemes)
    return suffix_pick

def pickCircuitTitle():
    """Return randomly picked circuit title"""
    circuit_pick = cups[random.randrange(len(cups))]
    return circuit_pick

# Function to assemble location, track, and circuit
def assembleLocation(list_select):
    """Return string containing the location prefix and suffix combined."""
    location_title = pickLocPrefix(list_select) + ' ' + pickLocSuffix(list_select)
    return location_title

def assembleTrack(list_select):
    """Return string containing the track prefix and suffix combined."""
    track_title = pickTrackPrefix(list_select) + ' ' + pickTrackSuffix(list_select)
    return track_title

def assembleCircuit():
    """Return string containing the circuit title."""
    cup_title = pickCircuitTitle() + " Cup"
    return cup_title