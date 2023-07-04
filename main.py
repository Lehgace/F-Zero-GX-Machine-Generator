# Joshua Erickson, joshmerickson19@gmail.com, F-Zero Machine Generator Python Implementation
"""Program that randomly generates a machine name, pilot name, pilot number, location, track, and cup title."""
from machine import assembleMachine
from pilot import assemblePilot, assemblePilotNumber
from circuit import assembleCircuit, assembleLocation, assembleTrack
from settings import Settings
from methods import convertBool, bcolors


def generateMachinePilot(nameselect, middleselect, lastselect, listselect):
    """Method to print a string containing the randomly-generated machine name, pilot number, and pilot name.
       
    Uses bcolors in terminal to emphasize titles from text.
    """
    print("\n\t\tYour machine is the {}{}{}, piloted by {}{}{}, {}{}{}".format(bcolors.OKCYAN, 
                                                                     assembleMachine(listselect), 
                                                                     bcolors.ENDC, 
                                                                     bcolors.WARNING, 
                                                                     assemblePilotNumber(),
                                                                     bcolors.ENDC,
                                                                     bcolors.OKGREEN,
                                                                     assemblePilot(nameselect, middleselect, lastselect),
                                                                     bcolors.ENDC))
    
def generateCircuit(circuitselect):
    """Method to print a string containing the randomly-generated location, track name, and cup title.
    
    Uses bcolors in terminal to distinguish titles from text.
    """
    print("\t\tYou will be racing in {}{}{}, on {}{}{}, from the {}{}{}\n".format(bcolors.OKBLUE, 
                                                                     assembleLocation(circuitselect), 
                                                                     bcolors.ENDC, 
                                                                     bcolors.OKCYAN, 
                                                                     assembleTrack(circuitselect),
                                                                     bcolors.ENDC,
                                                                     bcolors.FAIL,
                                                                     assembleCircuit(),
                                                                     bcolors.ENDC))


def randomizer(settings):
    """Used to create multiple combinations at a time."""
    for _ in range(settings.batches):
        generateMachinePilot(settings.useAllNames, settings.useMiddleName, settings.useLastName, settings.useAllMorphemes)
        generateCircuit(settings.useAllCircuits)

# Main Runtime Execution
settings = Settings()

while(True):
    """Endless while loop that will prompt user to randomly generate machine, pilot, and circuit content."""
    command = input("Press Enter to begin machine generation, m to view modifiers, q to quit ")
    """Menu for user navigation of program.
    
    case 'q': Quit program and exit
    case 'm': Settings menu that contains the various modifiers.
    """
    match command:
        
        case 'q':
            break
        case 'm':
            settings.printSettings()
            edit = input("Press Enter to exit modifiers, e to edit modifiers ")
            if edit == 'e':
                settings.toggleAllNames(convertBool(input("\tWould you like to pull from all available name lists? (y/n)" )))
                settings.toggleMiddle(convertBool(input("\tWould you like your pilot to have a middle name? (y/n) ")))
                settings.toggleLast(convertBool(input("\tWould you like your pilot to have a last name? (y/n) " )))
                settings.toggleAllMorphemes(convertBool(input("\tWould you like to pull from all available machine suffixes and prefixes? (y/n) " )))
                settings.toggleAllCircuits(convertBool(input("\tWould you like to pull from all available circuit suffixes and prefixes? (y/n) " )))
                settings.changeBatches(int(input("\tEnter number of batches to print: ")))
        case _:
            
            randomizer(settings)