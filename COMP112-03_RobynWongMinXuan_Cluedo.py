"""
Robyn Wong Min Xuan
COMP112-03 Introduction to Programing
Final Project: Cluedo
"""

# # # # # # # # # # # # # # # # # # QUESTIONS # # # # # # # # # # # # # # # # # # # 

#1. What were the 3 goals for your project?
"""
My first goal was the use of flow control.
My second goal was the use of object oriented programming.
My third goal was the use of lists. 
I also had optional goals for the use of turtles and file I/O.
(Though honestly, my main goal was just to make it functional!)
"""
#2. Were the goals met?
"""
The first three were, and the use of turtles (albeit for a different purpose).
I did not use file I/O.
"""
#3. How does this project illustrate your mastery of Python?
"""
Translating Cluedo from a multiplayer physical board game to a text-based Python
version with computer players tested my analytical and problem-solving skills.
The ability to dissect elements of the original game, adapt it for Python, and
reorganise it in a sensible manner required not only an understanding of Cluedo,
but also a familiarity with Python to determine which, why, and how Cluedo
features can be translated into Python code.

In a more technical sense, I have illustrated my ability to use most of the
Python skills/techniques we learned in class, including: flow control, modules,
object oriented programming, lists, dictionaries, and accumulators.

Moreover, I have used defensive programming to eliminate bugs and minimise the
ways in which my code to go wrong. e.g. input_validity(number,human_input)
checks for user input validity, and my code for determining turn order ensures
that players do not roll the same number.
"""
#4. What have you learned from doing this project?
"""
There are multiple possible solutions to a programming problem. In doing this
project, I have learnt the importance of paring down code to what is most
essential, and picking the most efficient and effective coding technique to
fulfil a task. Removing repetitive code and keeping the programme lean also
makes the code neater, and easier for me or others to understand. 

I have also learned about the importance of organising code. Creating a coded,
text-based version of a complicated board game has required lots of reverse
engineering and a clearly structured code, and I have given more thought than
usual into the organisation of my code in the script, and the neatness of its
presentation when run in the shell.
"""

# # # # # # # # # # # # # # # # # # # CLUEDO # # # # # # # # # # # # # # # # # # 

#welcome message

input('• WELCOME TO CLUEDO: THE GREAT DETECTIVE GAME •' +
          '\n(PRESS ENTER TO CONTINUE)')

#setting the scene

input('\n• SETTING THE SCENE •' +
      '\nHampshire, New England. 1926.' +
      '\nA terrible crime has been committed in the Tudor Mansion.' +
      '\nDR. BLACK has been brutally murdered.' +
      '\nIt is your job to deduce the details of the case.' +
      '\nCan you solve the mystery?'
      '\n(PRESS ENTER)')

#instructions *modified from original versions of Cluedo 

input('\n• HOW TO PLAY •' +
      '\n*modified for a three-player online version' +
      '\n- The case details -- ONE SUSPECT, ONE WEAPON, ONE ROOM -- are chosen at random and contained in an ENVELOPE. The remaining identities are distributed amongst the players.' +
      '\n- ROLL THE DIE to move into a room. Either MAKE A SUGGESTION or MAKE AN ACCUSATION.' +
      '\n- If you MAKE A SUGGESTION, name a SUSPECT, WEAPON, and the ROOM you are in. If your suggestion is SUCCESSFUL, it means ANOTHER PLAYER has one or more of your suggested details, and they will REVEAL it to you. If not, the detail is either UNASSIGNED or one of the CASE DETAILS.' +
      '\n- If you MAKE AN ACCUSATION, name a SUSPECT, WEAPON, and ROOM. You will know how many details you guessed match that of the CASE DETAILS. If your accusation matches ALL of the case details in the envelope, YOU WIN.' +
      '\n- There are six characters, six murder weapons and six rooms, leaving you with 216 possibilities.' +
      '\n(PRESS ENTER)')
    
#tips and recording details
#*NOTE: if I had more time, I would have used a file instead of a turtle

input('\n• TIP: RECORD ACCUSATIONS AND SUGGESTIONS MADE ON A PIECE OF PAPER •' +
      '\n(PRESS ENTER TO VIEW SUGGESTED FORMAT)')

import turtle

turtle.write('              (USE A TABLE LIKE THIS)' +           
             '\n\n              |  SUSPECT  |  WEAPON  |   ROOM   |' +
             '\n<YOUR_NAME>   |           |          |          |' +
             '\nCOMPUTER_1    |           |          |          |' +
             '\nCOMPUTER_2    |           |          |          |' +
             '\nUNASSIGNED_1  |           |          |          |' +
             '\nUNASSIGNED_2  |           |          |          |' +
             '\nCASE_DETAILS  |           |          |          |' ,
             align = 'center',font = ('Monaco',16,'normal'))

#challenge

input('\n• CHALLENGE: TRY TO SOLVE THE MYSTERY IN AS FEW ROUNDS AS POSSIBLE •' +
      '\n(PRESS ENTER)')

#are you ready?

input('\n• ARE YOU READY? •' +
      '\n(PRESS ENTER)')

#get name

name_1 = 'COMPUTER_1'
name_2 = 'COMPUTER_2'

def get_name():
    #sig: () -> str
    #gets name of human player
    name = input('\n• YOUR NAME •' +
                 '\nENTER YOUR NAME: ')
    name = name.upper()
    input('Welcome, ' + name + '. You will be playing against ' + name_1 + ' and ' + name_2 + '.' +
          '\nLet us begin.' +
          '\n(PRESS ENTER)')
    return name

name = get_name()

#full lists of suspects, weapons, and rooms
    
suspects = ['MISS SCARLETT','MR. GREEN','COLONEL MUSTARD','PROFESSOR PLUM','MRS. PEACOCK','MRS WHITE']
weapons = ['CANDLESTICK','DAGGER','LEAD PIPE','REVOLVER','ROPE','WRENCH']
rooms = ['KITCHEN','BALLROOM','CONSERVATORY','DINING ROOM','CELLAR','LIBRARY']

#isolating details for the envelope, human, comp_1, and comp_2

import random

assigned_suspects = random.sample(suspects,4)
assigned_weapons = random.sample(weapons,4)
assigned_rooms = random.sample(rooms,4)

#preparing for assignment of details

class Identities(object):
    def __init__(self,name,suspect,weapon,room,position):
        #sig: self,str,str,str,str,int
        self.name = name
        self.suspect = suspect
        self.weapon = weapon
        self.room = room
        self.position = position
    def suspects(self):
        #sig: self -> list[Identities]
        #returns duplicate suspects list w/ player's suspect identity removed
        #used for making suggestions and accusations
        suspects_list = list(suspects)
        suspects_list.remove(self.suspect)
        return suspects_list
    def weapons(self):
        #sig: self -> list[Identities]
        #returns duplicate weapons list w/ player's weapon identity removed
        #used for making suggestions and accusations
        weapons_list = list(weapons)
        weapons_list.remove(self.weapon)
        return weapons_list
    def rooms(self):
        #sig: self -> list[Identities]
        #returns duplicate rooms list w/ player's room identity removed
        #used for making suggestions and accusations
        rooms_list = list(rooms)
        rooms_list.remove(self.room)
        return rooms_list

#assigning case details

envelope = Identities('ENVELOPE',assigned_suspects[0],assigned_weapons[0],assigned_rooms[0],0)

input('\n• THE CASE DETAILS •' +
      '\nThe case details have been chosen and placed in the envelope.' +
      '\n(PRESS ENTER)')

#assigning player identities

human = Identities(name,assigned_suspects[1],assigned_weapons[1],assigned_rooms[1],0)
comp_1 = Identities(name_1,assigned_suspects[2],assigned_weapons[2],assigned_rooms[2],0)
comp_2 = Identities(name_2,assigned_suspects[3],assigned_weapons[3],assigned_rooms[3],0)

input('\n• ASSIGNING IDENTITIES •' +
      '\nThe cards have been dealt.' +
      '\n' + human.name + ', you are ' + human.suspect + ', with the ' + human.weapon + ', in the ' + human.room + '.' +
      '\n' + comp_1.name + ' and ' + comp_2.name + ' have also been assigned identites.' +
      '\n(PRESS ENTER)')

#high roll and determining turn order

def roll():
    #sig: () -> int
    #returns sum of rolls from two six-faced dice
    roll = random.randint(1,6) + random.randint(1,6)
    return roll

while True:
    roll_human = roll()
    roll_comp_1 = roll()
    roll_comp_2 = roll()
    #avoiding duplicate rolls 
    if (roll_human != roll_comp_1
        and roll_human != roll_comp_2
        and roll_comp_1 != roll_comp_2):
        break

high_roll = [roll_human,roll_comp_1,roll_comp_2]
high_roll.sort(reverse=True)
roll_players = {roll_human:human,roll_comp_1:comp_1,roll_comp_2:comp_2}

turn_order = []

for roll_player in roll_players:
    if roll_player == high_roll[0]:
        turn_order.insert(0,roll_players[roll_player])
    elif roll_player == high_roll[1]:
        turn_order.insert(1,roll_players[roll_player])
    elif roll_player == high_roll[2]:
        turn_order.insert(2,roll_players[roll_player])

input('\n• TURN ORDER •' +
      '\nWe will roll dice to determing the order of turns.' +
      '\n' + comp_1.name + ' has rolled ' + str(roll_comp_1) + '.' +
      '\n' + comp_2.name + ' has rolled ' + str(roll_comp_2) + '.' +
      '\n(PRESS ENTER TO ROLL THE DICE)')

input('\n' + human.name + ' has rolled ' + str(roll_human) + '.' +
      '\n\n' + turn_order[0].name + ' will go first, ' +
      turn_order[1].name + ' will go second, ' +
      turn_order[2].name + ' will go last.' +
      '\n(PRESS ENTER)')
      
#taking turns

def which_room(player):
    #sig: Identities -> str
    #takes the sum of a player's rolls and returns the room they are in 
    if player.position%6 == 0:
        room = rooms[0]
    elif player.position%6 == 1:
        room = rooms[1]
    elif player.position%6 == 2:
        room = rooms[2]
    elif player.position%6 == 3:
        room = rooms[3]
    elif player.position%6 == 4:
        room = rooms[4]
    elif player.position%6 == 5:
        room = rooms[5]
    return room

def moving_rooms(player,turn_roll):
    #sig: Identities,int -> NoneType
    #roll and room input for human, print statement for comp_1 and comp_2
    if player == human:
        input('(PRESS ENTER TO ROLL THE DICE)')
        input(player.name + ' has rolled ' + str(turn_roll) + '.' +
              '\n' + player.name + ' has moved into the ' + which_room(player) + '.')
    elif player != human:
        print(player.name + ' has rolled ' + str(turn_roll) + '.' +
              '\n' + player.name + ' has moved into the ' + which_room(player) + '.')

def input_validity(number,human_input):
    #sig: int,str -> int
    #checks if the human input is valid 
    valid_inputs = []
    for n in range(number):
        valid_inputs.append(n)
    while True:
        if human_input.isdigit():
            if int(human_input) not in range(number):
                print('THAT IS NOT A VALID CHOICE. ENTER A NUMBER IN THE RANGE',valid_inputs)
                try_again = input('(TRY AGAIN) ')
                human_input = try_again
            else:
                return int(human_input)
        else:
            print('THAT IS NOT A VALID CHOICE. ENTER A NUMBER IN THE RANGE',valid_inputs)
            try_again = input('(TRY AGAIN) ')
            human_input = try_again
    
def accusation(player,accusation_list):
    #sig: Identities,list[Identities] -> NoneType or str
    #checks for matches between accusation details and case details
    #prints the number of detail(s) guessed correctly
    #if the player's accusation matches the case details, returns game status
    correct = 0
    for accusation_detail in accusation_list:
        if accusation_detail == envelope.suspect:
            correct += 1
        elif accusation_detail == envelope.weapon:
            correct += 1
        elif accusation_detail == envelope.room:
            correct += 1
    if correct == 1:
        print(player.name + ' guessed ' + str(correct) + ' detail correctly.')
    else:
        print(player.name + ' guessed ' + str(correct) + ' details correctly.')
        if correct == 3:
            print(player.name + ' solved the murder mystery in ' + str(rounds) + ' ROUNDS.' +
                  '\n' + player.name + ' WINS.' +
                  '\n\n• THE MYSTERY HAS BEEN SOLVED! (END OF GAME) •')
            game_status = 'end'
            return game_status

def suggestion_suspect(player,other_players,suggestion_list):
    #sig: Identities,list(Identities),list(Identities) -> NoneType
    #checks for matches between suggested suspect and other player's suspect identities
    #prints if the suggestion was successful or unsuccessful
    #if it was successful, prints the player and identity suggested successfully
    none = 0
    for other_player in other_players:
        if other_player.suspect == suggestion_list[0]:
            print(player.name + ' SUCCESSFULLY suggested a suspect: ' +
                  other_player.name + ' is ' + other_player.suspect + '.')
            return
        else:
            none += 1
    if none == 2:
        print(player.name + ' UNSUCCESSFULLY suggested a suspect.')

def suggestion_weapon(player,other_players,suggestion_list):
    #sig: Identities,list(Identities),list(Identities) -> NoneType
    #checks for matches between suggested suspect and other player's weapon identities
    #prints if the suggestion was successful or unsuccessful
    #if it was successful, prints the player and identity suggested successfully 
    none = 0
    for other_player in other_players:
        if other_player.weapon == suggestion_list[1]:
            print(player.name + ' SUCCESSFULLY suggested a weapon: ' +
                  other_player.name + ' has the ' + other_player.weapon + '.')
            return
        else:
            none += 1
    if none == 2:
        print(player.name + ' UNSUCCESSFULLY suggested a weapon.')

def suggestion_room(player,other_players,suggestion_list):
    #sig: Identities,list(Identities),list(Identities) -> NoneType
    #checks for matches between suggested suspect and other player's room identities
    #prints if the suggestion was successful or unsuccessful
    #if it was successful, prints the player and identity suggested successfully
    none = 0
    for other_player in other_players:
        if other_player.room == suggestion_list[2]:
            print(player.name + ' SUCCESSFULLY suggested a room: ' +
                  other_player.name + ' is in the ' + other_player.room + '.')
            return
        else:
            none += 1
    if none == 2:
        print(player.name + ' UNSUCCESSFULLY suggested a room.')
            
def suggestion(player,suggestion_list):
    #sig: Identities,list[Identities] -> NoneType
    #duplicates list of players and removes player whose turn it is
    #checks for matches between suggested details and other player's identities
    other_players = list(turn_order)
    other_players.remove(player)
    suggestion_suspect(player,other_players,suggestion_list)
    suggestion_weapon(player,other_players,suggestion_list)
    suggestion_room(player,other_players,suggestion_list)

player_actions = ['a SUGGESTION','an ACCUSATION']

def human_action(player):
    #sig: Identities -> NoneType or str
    #human chooses to make a suggestion or an accusation
    #if suggesting, human chooses suspect and weapon to suggest
    #if accusing, human chooses suspect, weapon, and room to accuse
    human_choice = player_actions[input_validity(2,input('\nWHAT WILL YOU DO?' +
                                                         '\n0 : MAKE A SUGGESTION' +
                                                         '\n1 : MAKE AN ACCUSATION' +
                                                         '\n(ENTER 0 OR 1) '))]
    print('\n' + player.name + ' has chosen to make ' + human_choice + '.')
    if human_choice == 'a SUGGESTION':
        print('\nCHOOSE A SUSPECT TO SUGGEST:')
        for count,item in enumerate(human.suspects()):
            print(count,':',item)
        suggest_suspect_human = input_validity(5,input('(ENTER 0, 1, 2, 3, OR 4) '))
        print('\nCHOOSE A WEAPON TO SUGGEST:')
        for count,item in enumerate(human.weapons()):
            print(count,':',item)
        suggest_weapon_human = input_validity(5,input('(ENTER 0, 1, 2, 3, OR 4) '))
        suggestion_human = [human.suspects()[suggest_suspect_human],human.weapons()[suggest_weapon_human],which_room(human)]
        print(human.name + ' suggests that ' + suggestion_human[0] +
              ' committed the crime in the ' + which_room(human) +
              ' with the ' + suggestion_human[1] + '.')
        suggestion(human,suggestion_human)
    elif human_choice == 'an ACCUSATION':
        print('\nCHOOSE A SUSPECT TO ACCUSE:')
        for count,item in enumerate(human.suspects()):
            print(count,':',item)
        accuse_suspect = input_validity(5,input('(ENTER 0, 1, 2, 3, OR 4) '))
        print('\nCHOOSE A WEAPON TO ACCUSE:')
        for count,item in enumerate(human.weapons()):
            print(count,':',item)
        accuse_weapon = input_validity(5,input('(ENTER 0, 1, 2, 3, OR 4) '))
        print('\nCHOOSE A ROOM TO ACCUSE:')
        for count,item in enumerate(human.rooms()):
            print(count,':',item)
        accuse_room = input_validity(5,input('(ENTER 0, 1, 2, 3, OR 4) '))
        accusation_human = [human.suspects()[accuse_suspect],human.weapons()[accuse_weapon],human.rooms()[accuse_room]]
        print('\n' + human.name + ' accuses ' + accusation_human[0] +
              ' of committing the crime in the ' + accusation_human[2] +
              ' with the ' + accusation_human[1] + '.')
        return accusation(human,accusation_human)

def comp_action(player):
    #sig: Identities -> NoneType or str
    #randomly chooses for comp_1 or comp_2 to make a suggestion or an accusation
    #if suggesting, randomly chooses suspect and weapon to suggest
    #if accusing, randomly chooses suspect, weapon, and room to accuse
    comp_choice = random.choice(player_actions)
    print(player.name + ' has chosen to make ' + comp_choice + '.')
    if comp_choice == 'a SUGGESTION':
        suggest_suspect_comp = random.choice(player.suspects())
        suggest_weapon_comp = random.choice(player.weapons())
        suggestion_comp = [suggest_suspect_comp,suggest_weapon_comp,which_room(player)]
        print(player.name + ' suggests that ' + suggest_suspect_comp +
              ' committed the crime in the ' + which_room(player) +
              ' with the ' + suggest_weapon_comp + '.')
        suggestion(player,suggestion_comp)
    elif comp_choice == 'an ACCUSATION':
        accusation_comp = [random.choice(player.suspects()),random.choice(player.weapons()),random.choice(player.rooms())]
        print(player.name + ' accuses ' + accusation_comp[0] +
              ' of committing the crime in the ' + accusation_comp[2] +
              ' with the ' + accusation_comp[1] + '.')
        return accusation(player,accusation_comp)

#playing the game

print('\n• PLAY •')

game = 'ongoing'
rounds = 0 #accumulator

#print(envelope.suspect,envelope.weapon,envelope.room)

while True:
    if game == 'end':
        break
    rounds += 1
    print('\n• ROUND ' + str(rounds) + ' •') 
    for player in turn_order:
        if game == 'end':
            break
        input('\n(PRESS ENTER TO BEGIN ' + player.name + "'S TURN)")
        print('\n• ' + player.name + "'S TURN •")
        turn_roll = roll()
        player.position += turn_roll
        moving_rooms(player,turn_roll)
        if player == human:
            game = human_action(player)
        elif player != human:
            game = comp_action(player)

#• CREDITS •
#Originally created by ANTHONY E. PRATT in 1943
#Adapted for Python by ROBYN WONG MIN XUAN in 2020
