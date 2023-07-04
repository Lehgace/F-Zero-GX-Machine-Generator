# Joshua Erickson, joshmerickson19@gmail.com, F-Zero Machine Generator Python Implementation
"""Contains all method and list declarations used for generation of circuit titles."""
import random
from methods import readNames, chooseContent

# Methods to populate morpheme lists
# Populate Location Prefixes
locprefixes = []
locprefixes = readNames(locprefixes, 'locprefixes.txt')

# Populate Location Suffixes
locsuffixes = []
locsuffixes = readNames(locsuffixes, 'locsuffixes.txt')

# Populate Track Prefixes
trackprefixes = []
trackprefixes = readNames(trackprefixes, 'trackprefixes.txt')

# Populate Track Suffixes
tracksuffixes = []
tracksuffixes = readNames(tracksuffixes, 'tracksuffixes.txt')

# Populate All Track and Location morphemes
morphemes = sorted(locprefixes + locsuffixes + trackprefixes + tracksuffixes)

# Populate list of Circuit Titles
cups = ["Ruby", "Sapphire", "Emerald", "Diamond", "AX", "Jade", "Opal", "Amber", "Amethyst"]

class Circuit:
    """Prototype implementation of Circuit class"""
    def __init__(self, trackTitle = None, courseTitle = None, cupTitle = None, circuit=[]):
        self.trackTitle = trackTitle
        self.courseTitle = courseTitle
        self.cupTitle = cupTitle
        self.circuit = circuit
    pass

# Methods to pick prefixes and suffixes for location and track, pick circuit
def pickLocPrefix(listselect):
    """Return randomly picked location prefix"""
    prefixpick = chooseContent(listselect, locprefixes, morphemes)
    return prefixpick

def pickLocSuffix(listselect):
    """Return randomly picked location suffix"""
    suffixpick = chooseContent(listselect, locsuffixes, morphemes)
    return suffixpick

def pickTrackPrefix(listselect):
    """Return randomly picked track prefix"""
    prefixpick = chooseContent(listselect, trackprefixes, morphemes)
    return prefixpick

def pickTrackSuffix(listselect):
    """Return randomly picked track prefix"""
    suffixpick = chooseContent(listselect, tracksuffixes, morphemes)
    return suffixpick

def pickCircuitTitle():
    """Return randomly picked circuit title"""
    circuitpick = cups[random.randrange(len(cups))]
    return circuitpick

# Method to assemble location, track, and circuit
def assembleLocation(listselect):
    """Return string containing the location prefix and suffix combined."""
    locationtitle = pickLocPrefix(listselect) + ' ' + pickLocSuffix(listselect)
    return locationtitle

def assembleTrack(listselect):
    """Return string containing the track prefix and suffix combined."""
    tracktitle = pickTrackPrefix(listselect) + ' ' + pickTrackSuffix(listselect)
    return tracktitle

def assembleCircuit():
    """Return string containing the circuit title."""
    cuptitle = pickCircuitTitle() + " Cup"
    return cuptitle