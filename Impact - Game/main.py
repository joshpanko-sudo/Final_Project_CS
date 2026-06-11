# from inventory import Backpack
# from main_2 import Power, Player, Enemy, start_battle
# from main_2 import start_battle

# import sys
# import time
# import random
import game_maps
from map_managerV2 import MapManager
MM = MapManager()

print("-----------------------------------------")
print("             IMPACT GAME                 ")
print("         Created By Josh and Allen       ")
print("-----------------------------------------")



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


