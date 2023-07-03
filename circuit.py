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
circuits = ["Ruby", "Sapphire", "Emerald", "Diamond", "AX", "Jade", "Opal", "Amber", "Amethyst"]

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
    circuitpick = circuits[random.randrange(len(circuits))]
    return circuitpick

# Method to assemble location, track, and circuit
def AssembleLocation(listselect):
    """Return string containing the location prefix and suffix combined."""
    locationtitle = pickLocPrefix(listselect) + ' ' + pickLocSuffix(listselect)
    return locationtitle

def AssembleTrack(listselect):
    """Return string containing the track prefix and suffix combined."""
    tracktitle = pickTrackPrefix(listselect) + ' ' + pickTrackSuffix(listselect)
    return tracktitle

def AssembleCircuit():
    """Return string containing the circuit title."""
    circuittitle = pickCircuitTitle() + " Cup"
    return circuittitle