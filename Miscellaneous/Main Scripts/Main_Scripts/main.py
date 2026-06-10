from inventory import Backpack
from main_2 import Power, Belly_Badge_Care_Bear, Belly_Badge_Evil_Bear, start_battle
from main_2 import start_battle
# import random
from slow_print import slow_print as SP



print("-----------------------------------------")
print("             IMPACT GAME                 ")
print("         Created By Josh and Allen       ")
print("-----------------------------------------")




SP("You arrive home from studying at the highest science techology university", delay=0.0225)
SP("You see that you got mail. You open up your mail box", 0.0225)
SP("You have been selected as a researcher to try time travel!", 0.0225)

SP("The science team decided to fly you out first class.", 0.0225)
SP("You finally arrive and meet the leader, Jim Kalper", 0.0225)
SP("Jim: Welcome to the team!!", 0.0225)
SP("Jim: We are going to start testing tomorrow!", 0.0225)
SP("Jim: You should take some rest now..", 0.0225)

SP("The next day.....", 0.0625)
SP("Jim: Everything on?!?!", 0.0525)
SP("Mike: Red switch on!!", 0.0225)
SP("Lakrry: Green switch on!!", 0.0225)
SP("Loon: Black is blinking?????", 0.0225)
SP("Jim: Shut it down!!!!", 0.0225)
SP("Lakrry: ITS TO LATE, ITS FULL POWER!!", 0.0225)
SP("BLASTTTT!!!!!!!!", 0.00225)
SP("You appear in a strange new word", 0.0225)
SP("It looks like your world but......", 0.0225)
SP("Robots are taking over!!!", 0.0225)
SP("You: There is massive spider robots everywhere", 0.0225)

Enemy = Belly_Badge_Evil_Bear("Spider Droid", 20)
Player = Belly_Badge_Care_Bear("You", 50)
Stun = False
maxhealcooldown = 3
healcooldown = 0

start_battle(Enemy, Player)
