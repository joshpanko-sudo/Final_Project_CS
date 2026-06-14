# from inventory import Backpack
# from main_2 import Power, Player, Enemy, start_battle
# from main_2 import start_battle

# import sys
# import time
# import random
import game_maps
from map_managerV2 import MapManager
MM = MapManager()
from slow_print import slow_print_system
SP = slow_print_system()
from slow_print import character_say as CS

print("-----------------------------------------")
print("             IMPACT GAME                 ")
print("         Created By Josh and Allen       ")
print("-----------------------------------------")


SP.slow_print("June 5, 2090", 0.0625)
SP("6:00PM, the sun is setting", 0.0625)

SP("You arrive home from studying at the highest science techology university",0.0625 )
SP("You see that you got mail. You open up your mail box", 0.0625)
SP("You have been selected as a researcher to try time travel!", 0.0625)

SP("The science team decided to fly you out first class.", 0.0625)
SP("You finally arrive and meet the leader, Jim Kalper", 0.0625)
SP("Jim: Welcome to the team!!", 0.0625)
SP("Jim: We are going to start testing tomorrow!", 0.0625)
SP("Jim: You should take some rest now..", 0.0625)

SP("The next day.....")
SP("Jim: Everything on?!?!", 0.0625)
SP("Mike: Red switch on!!", 0.0625)
SP("Lakrry: Green switch on!!", 0.0625)
SP("Loon: Black is blinking?????", 0.0625)
SP("Jim: Shut it down!!!!", 0.0225)
SP("Lakrry: ITS TO LATE, ITS FULL POWER!!", 0.0625)
SP("BLASTTTT!!!!!!!!", 0.0625)
SP("You appear in a strange new word", 0.0625)
SP("It looks like your world but......", 0.0625)
SP("Robots are taking over!!!", 0.0625)
SP("You: There is massive spider robots everywhere", 0.0625)
SP("A Spider Droid is going to attack you...", 0.0625)
SP("Helper: Hey there!", 0.0625)
SP("Helper: You are going to enter your first battle", 0.0625)
SP("Helper: Your current health is displayed after each attack", 0.0625)
SP("Helper: Your attacks are displayed in a list", 0.0625)
print("--------------------------------------------------------------")

Enemy1 = Enemy("Spider Droid", 20)
Player1 = Player("You", 50)
Stun = False
maxhealcooldown = 3
healcooldown = 0

start_battle(Enemy1, Player1,  Stun, maxhealcooldown, healcooldown)
SP("Helper: Great job defeating your first enemy!", 0.0625)
SP("Helper: As you find more weponds, you'll be able to do more attacks!", 0.0625)
SP("Massive spider robot approaches...", 0.0625)
SP("Helper: Hang on here! I'll take care of this guy! =D", 0.0625)
print("--------------------------------------------------------------")
SP("Massive Spider Droid Stabs Helper robot! strength: 50",  0.0625)
SP("Helper Robot is deciding which attack....",  0.0625)
SP("Helper Robot ZAPS! strength: 500",  0.0625)
SP("Massive Spider Droid was defeated.",  0.0625)
print("--------------------------------------------------------------")

SP("Helper: Wow that guy was easy!", 0.0625)
SP("Who are.... you?", 0.0625)
SP("Helper: I'm just here to help!", 0.0625)
SP("You: Ohhhhhhh..... okay I'll see you then!", 0.0625)
SP("Helper: I'm always here to help! Bye!", 0.0625)
SP("-------Helper Robot Flies Away---------", 0.0625)












MM.load_map(game_maps.tutorial_spawn, True)
MM.update_map()

while True:
    MM.gameloopMapManager()


