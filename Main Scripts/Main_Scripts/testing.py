from inventory import Backpack
from main_2 import Power, Belly_Badge_Care_Bear, Belly_Badge_Evil_Bear, start_battle
from main_2 import start_battle
import sys
import time
import random
# All of the imports

Enemy = Belly_Badge_Evil_Bear("Spider Droid", 50)
Player = Belly_Badge_Care_Bear("You", 50)
# Setting the player and enemy in the fight
# The number after the names is the health

Stun = False
maxhealcooldown = 3
healcooldown = 0
Stun = False
maxhealcooldown = 3
healcooldown = 5
# Setting the variables for the fight sequence

start_battle(Enemy, Player, Stun, maxhealcooldown, healcooldown)
# Starting the battle