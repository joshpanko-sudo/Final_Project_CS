from inventory import Backpack
from main_2 import Power, Belly_Badge_Care_Bear, Belly_Badge_Evil_Bear


print("-----------------------------------------")
print("           STONE KNIGHT                  ")
print("         Created By Josh and Allen       ")
print("-----------------------------------------")

my_backpack = Backpack(300, capacity=5)

name = input("Choose your name: ")

def start():
    slow_print("Mom: The village is under attack!!", delay=0.025)
    slow_print("Mom: You must save the village!!", delay=0.05)
    slow_print("*You walk out of your house*", delay=0.05)
    slow_print("*You see monsters everwhere*", delay=0.05)
    slow_print("*A monster approaches you*", delay=0.05)

Pikachu = Belly_Badge_Evil_Bear("Pikachu", 20)
Charizard = Belly_Badge_Care_Bear(name, 50)
Stun = False
maxhealcooldown = 3
healcooldown = 0

start_battle()
