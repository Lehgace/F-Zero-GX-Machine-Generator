# Joshua Erickson, joshmerickson19@gmail.com, F-Zero Machine Generator Python Implementation
"""Program that randomly generates a machine name, pilot name, pilot number, location, track, and cup title."""
from machine import AssembleMachine
from pilot import AssemblePilot, AssemblePilotNumber
from circuit import AssembleCircuit, AssembleLocation, AssembleTrack

"""Blender build scripts for terminal print usage"""
class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# To-Do: Fully finish text menu to be more streamlined
#        Integrate options menu
#        Full Circuit generation (5 courses instead of 1)
#        Machine and Pilot Stats menus (Pilot Profiles -> Machine Profiles)

def GenerateMachinePilot(nameselect, middleselect, lastselect, listselect):
    """Method to print a string containing the randomly-generated machine name, pilot number, and pilot name.
       
    Uses bcolors in terminal to emphasize titles from text.
    """
    print("\t\tYour machine is the {}{}{}, piloted by {}{}{}, {}{}{} ".format(bcolors.OKCYAN, 
                                                                     AssembleMachine(listselect), 
                                                                     bcolors.ENDC, 
                                                                     bcolors.WARNING, 
                                                                     AssemblePilotNumber(),
                                                                     bcolors.ENDC,
                                                                     bcolors.OKGREEN,
                                                                     AssemblePilot(nameselect, middleselect, lastselect),
                                                                     bcolors.ENDC))
    
def GenerateCircuit(circuitselect):
    """Method to print a string containing the randomly-generated location, track name, and cup title.
    
    Uses bcolors in terminal to distinguish titles from text.
    """
    print("\t\tYou will be racing in {}{}{}, on {}{}{}, from the {}{}{} ".format(bcolors.OKBLUE, 
                                                                     AssembleLocation(circuitselect), 
                                                                     bcolors.ENDC, 
                                                                     bcolors.OKCYAN, 
                                                                     AssembleTrack(circuitselect),
                                                                     bcolors.ENDC,
                                                                     bcolors.FAIL,
                                                                     AssembleCircuit(),
                                                                     bcolors.ENDC))

# Main Runtime Execution

reconfiguremachine = True
reconfigurepilot = True
reconfigurecircuit = True
init = True
print("Press any key to begin machine generation, p to edit pilot settings, m to edit machine settings, c to edit circuit settings, q to quit ")

while(True):
    """Endless while loop that will prompt user to randomly generate machine, pilot, and circuit content.
    
    Contains toggleable modifiers for machine, pilot, and circuit to determine list content and other features.
    """
    command = input()
    if (command == 'q'): break
    
    # Reconfiguration prompts for Pilot names
    reconfigurepilot = True if command == 'p' else False
    if (reconfigurepilot or init):
        nameselect = input("\tWould you like to pull from all available name lists? (y/n)" )
        nameselect = True if nameselect == 'y' else False
        middleselect = input("\tWould you like your pilot to have a middle name? (y/n) ")
        middleselect = True if middleselect == 'y' else False
        lastselect = input("\tWould you like your pilot to have a last name? (y/n) " )
        lastselect = True if lastselect == 'y' else False
        reconfigurepilot = False

    # Reconfiguration prompts for Machine morphemes
    reconfiguremachine = True if command == 'm' else False
    if (reconfiguremachine or init):
        listselect = input("\tWould you like to pull from all available machine suffixes and prefixes? (y/n)" )
        listselect = True if listselect == 'y' else False
        reconfiguremachine = False

    # Reconfiguration prompts for Circuit morphemes
    reconfigurecircuit = True if command == 'c' else False
    if (reconfigurecircuit or init):
        circuitselect = input("\tWould you like to pull from all available circuit suffixes and prefixes? (y/n)" )
        circuitselect = True if circuitselect == 'y' else False
        reconfigurecircuit = False

    GenerateMachinePilot(nameselect, middleselect, lastselect, listselect)
    GenerateCircuit(circuitselect)
    init = False