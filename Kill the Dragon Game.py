########
#import modules
#######
import time
########
#define functions
#######
#this prints the picture and starts the game
def start():

    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░")
    print("░░░░░░░░█░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░")
    print("░░░░░░░██░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░")
    print("░░░░░░░███░░██████████░░░░█░█░░░░░░░░░░░")
    print("░░░░░░░░█░████░▒▒░░░░░██░█░░█░░░░░░░░░░░")
    print("░░░░░░░░░██░░███▒▒░░░░░░█░░█░░░░░░░░░░░░")
    print("░░░░░░░░░█▒█░░██▒▒░░░░░░░██░░░░░░░░░░░░░")
    print("░░░░░░░░░█▒▒███░█████████▒░░░░░░░░░░░░░░")
    print("░░░░░░░░░░█▒▒▒▒░████████▒▒░░░░░░░░░░░░░░")
    print("░░░░░░░░░░█▒▒▒▒▒▒░░░██░░█░░░░░░░░░░░░░░░")
    print("░░░░░░░░░░░█▒▒▒▒▒▒░░██░░░█░░░░░░░░░░░░░░")
    print("░░░░░░░░░░░░███▒▒▒▒░░░░░██████░░░░░░░░░░")
    print("░░░░░░░░░███░▒██████████░░░░██░░░░░░░░░░")
    print("░░░░░░░██▒░░▒▒█▒▒▒░░░░░██████░░░░░░░░░░░")
    print("░░░░░░░███▒▒███▒▒▒▒░░░░░█▒█░░░░░░░░░░░░░")
    print("░░░░░██████████▒▒▒▒▒░░░██▒█░░░░░░░░░░░░░")
    print("░░░░░██▒░░░░░▒█▒▒▒▒▒▒░░█▒▒█░░░░░░░░░░░░░")
    print("░░░░░░█▒░░░░▒███▒▒▒▒▒░░█▒██░░░░░░░░░░░░░")
    print("░░░░░░█▒▒▒░░▒███████████▒█░█░░░░░░░░░░░░")
    print("░░░░░░███▒▒▒▒███▒░██▒░░███▒███████████░░")
    print("░░░░░░░░█████░░█▒█░██▒▒█░█▒█▒▒▒▒▒▒░░░░██")
    print("░░░░░░░░░░░░░░████░████████████████████░")
    print("░░░░░░░░░░░░░░█▒░█░█▒▒░█████░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░████░█████░░░░░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    Entrance()

#this defines the function entrance and allows the story to progress
def Entrance():
    print("You are a knight and need to find the mighty sword to slay the beast")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tmainroom\n\toutside\n")
    if move.lower() == "mainroom":
        mainroom()
    elif move.lower() == "outside":
        outside()
    else:
        print("You are confused... you do not do anything..")
        pass
#this defines mainroom which is also another room that leads toward the progression of the story.
def mainroom():
    print("You step foot into the main room.")
    #gives wait time between each printed thing
    time.sleep(1)
    print("CREAK")
    time.sleep(2)
    print("the floor creaked as you walk in.....")
    time.sleep(1)
    #allows the user to pick where they would like to go
    move = input("\nWhere would you like to go? Say one of these choices:\n\tentrance\n\toutside\n\thallway1\n\thallway2\n")
    if move.lower() == "entrance":
        Entrance()
    elif move.lower() == "outside":
        outside()
    elif move.lower() == "hallway1":
        hallway1()
    elif move.lower() == "hallway2":
        hallway2()
    else:
        print("You are confused and decide to do nothing... please re-enter your choice")
    
        #TODO: what should happen if they type something else?
        
        pass

def outside():
    print("You are outside..")
    time.sleep(1)
    print("...")
    time.sleep(0.5)
    print("You take a look at the beautiful castle")
    time.sleep(1)
    print('''     /\         /\                     /\
      /  \       /  \                   |@>        /  \
     /    \     / .  \                  |         /    \
    /      \   /  |@> \       /\       / \       /      \
   /     /\ \ /   |    \     /  \     /   \     /        \
  /     /  \ /  _ | _   \   /    \    | O |    /          _   _   _
 /     /    \  |_|_|_|   \ /      \   |___|   /          | |_| |_| |
/     /      \  | O |     /        \  | |_|  /      /\   |         |
    _   _   _ \ |___|    /          \ |__|| /      /  \  |  O   O  |
   | |_| |_| |  | |_|   /             | |_|       /    \ |   __ _  |
   |         |  |__||  /              |_| |      /       |     |   |
   | O  O  O |  | |_| /               |__ |     /        | O  O  O |
   |  _      |  _   _   _        ______   |   _   _   _  |  _      |
   | |__|_ | |_| |_| |_| |______|      |_____| |_| |_| |_| |__|_ |_|
   |  |   _| |        _  |  | _|  ____     _||        _  |  |    | |
   |   _| _  ||_|   _|_  | _|_   |||||| |_| _||_|   _|_  |   _| _| |
   |  __|  |_|  |_       | | |__ |++++|   |_||  |_      ||  __|  |_|
   |_________|___________|-------------------|___________|_________|
                                 /_/_/
                                /_/_/''')
                                #allows the user to make options on what they would like to do 
    move = input("\nWhere would you like to go? Say one of these choices:\n\tentrance\n\tmainroom\n")
    if move.lower() == "mainroom":
        mainroom()
    elif move.lower() == "Entrance":
        Entrance()
    elif move.lower() == "hallway1":
        hallway1()
    else:
        print("you are confused and decide to do nothing.. please re-enter your choice")
        #TODO: what should happen if they type something else?
        #tells the user to type in the choice correctly because they have typed it wrong or typed something completely different
        pass
#defines the room hallway so the story may progress
def hallway1():

    print("You have entered the hallway")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tbroomcloset\n\tmainroom\n")
    if move.lower() == "mainroom":
        mainroom()
    elif move.lower() == "broomcloset":
        broomcloset()
######## defines the broomcloset and allow the story to progress
def broomcloset():
    print("you are in the broom closet.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("what are you even doing in here?")
    move = input("\nYou find THE ULTIMATE SWORD! Do you take it? Say one of these choices:\n\ttake\n\tleave\n")
    if move.lower() == "take":
        TAKE()
    elif move.lower() == "leave":
        LEAVE()
    pass
    #allows the user to have the option to either take or leave the sword
    #defines hallway2 so the story may progress
def hallway2():

    print("You have entered the second hallway..")
    time.sleep(1)
    print("ROAAAR")
    time.sleep(1)
    print("You hear roaring coming from the room ahead..")
    move = input("\nIt's the dragons den... Do you enter? Say one of these choices:\n\tno\n\tyes\n")
    if move.lower() == "yes":
        YES()
    elif move.lower() == "no":
        NO()
#def take allows the user to take the sword
def TAKE():
    global sword
    sword = True
    print("you take the sword and leave the room..")
    hallway1()
# allows the user to have the option to leave the sword
def LEAVE():
    print("You decide not to take the sword")
#these are the choices the user can make when entering the dungeon
def YES():
    if sword == True:
        print("You decide to slay the beast with your mighty sword and save the princess...") 
    elif sword == False:
        print("You idiotically enter the dungeon and get burned to a crisp by the dragon...")
def NO():
    print("You decided not to enter the dungeon, you weren't prepared...")
    time.sleep(1)
    print("You go back to the mainroom..")
    mainroom()

    

#main
#######
#TODO: Add some global variables
sword = False
start()