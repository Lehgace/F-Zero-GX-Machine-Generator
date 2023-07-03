# F-Zero GX Machine Generator - Version (0.0.2)

## What is F-Zero GX Machine Generator?
This application acts as a random name generator for various F-Zero GX related content. Ever wanted to see a randomly generated F-Zero GX machine name, pilot name, or track title? This application aims to satisfy that curiosity.

### Example Generations (strict modifers)
![strict](https://github.com/Lehgace/F-Zero-GX-Machine-Generator/assets/122835808/670bb722-a955-4e7d-89de-2ff1b93fae63)
![7strict](https://github.com/Lehgace/F-Zero-GX-Machine-Generator/assets/122835808/6f994686-c951-4606-be67-afe03e904844)
### Example Generations (unrestricted modifers)
![free](https://github.com/Lehgace/F-Zero-GX-Machine-Generator/assets/122835808/ca39279f-e132-4409-a703-490df90dba39)
![7free](https://github.com/Lehgace/F-Zero-GX-Machine-Generator/assets/122835808/40640bdd-42cb-484b-afbe-ed3a82796a70)


## How does it work?
The program contains text files which hold the original names of various F-Zero machines, pilots, tracks, etc. The text files are read by the application to generate lists of potential combinations for a random number generator to randomly select elements from the populated lists. This leads to the creation of random mix-and-match combinations of F-Zero GX objects that are different from the original lists. For instance, there are more than 3000 possible combinations possible from mixing and matching the prefixes and suffixes of the original 41 machines! Let's look at a specific example. 

Consider the following original machine titles: 
* Blue Falcon
* Spark Moon
* Rainbow Phoenix

The application splits the names into two categories: prefixes and suffixes. The available prefixes would be Blue, Spark, and Rainbow. The available suffixes would be Falcon, Moon, and Phoenix.
Next the program randomly selects a prefix and suffix to create a new machine title (or the original title if it happens to pick those elements by chance). Below would be some example generations from the provided machine list. This is if we don't include duplicates (Phoenix Phoenix, Blue Blue, etc.) or the original titles:
* Blue Moon
* Blue Phoenix
* Spark Falcon
* Spark Phoenix
* Rainbow Falcon
* Rainbow Moon

The application can do this for pilot names, pilot numbers, track locations, track names, as well as other current and planned additions. It also contains options for various modifiers, such as creating a machine using two prefixes/suffixes instead of a pair of prefixes and suffixes.

## What is the goal of this project?
The goal of this project is to eventually create an interactie website that people can use to randomly mix-and-match the names of various F-Zero GX machines and pilots. Not only just the names, but as well as show a fusion of the machines and potentially pilots and courses. The application would mainly serve as a form of entertainment, something to satisfy your boredom. 

The idea comes from my fascination of F-Zero GX. I thought the different names for the machines and pilots in the game was cool. So I thought it would be interesting to create an application where you can randomly mix-and-match the names of various machines and pilot names to see what Frankenstein creations are possible.

### Planned Future Additions and WIP
* Overhauling the UI to be more streamlined and user friendly _(In-Progress)_
* Overhauling the UI to include various menus and displays for toggleable and viewable content instead of being terminal-based
* Addition of Custom Machines titles from the game
* Option to add custom prefixes, suffixes, etc.
* Duplicate prevention modifier (no more Wonder Wonder, Stingray Stingray)
* Adding settings menu to edit available modifiers _(In-Progress)_
* Adding additional machine stats such as weight, boost, grip; viewable from machine profile
* Adding additional pilot information such as sex and age (idea of custom bios entertained but on the backburner for now); viewable from pilot profile
* Ability to generate batches of custom machines, pilots, courses by a user specified amount _(In-Progress)_
* Log history that shows a history of your randomly generated content
* Option to write history or user-specified content to files
* Overhaul to web based application

## This sounds great! How can I try it out for myself?
As of right now, a functional prototype is available for use. To replicate the original experience, run the application in Visual Studio Code. Download the project files, run main.py, follow the onscreen instructions and you should be good to go!

![falconsalute](https://github.com/Lehgace/F-Zero-GX-Machine-Generator/assets/122835808/2850884b-28fe-41bc-a28a-a54f7b4066ae)
