from inventory import Backpack
from main_2 import Power, Player, Enemy, start_battle
from main_2 import start_battle
from slow_print_script import slow_print
import sys
import time
import random


print("-----------------------------------------")
print("             IMPACT GAME                 ")
print("         Created By Josh and Allen       ")
print("-----------------------------------------")



slow_print("You arrive home from studying at the highest science techology university",0.0625 )
slow_print("You see that you got mail. You open up your mail box", 0.0625)
slow_print("You have been selected as a researcher to try time travel!", 0.0625)

slow_print("The science team decided to fly you out first class.", 0.0625)
slow_print("You finally arrive and meet the leader, Jim Kalper", 0.0625)
slow_print("Jim: Welcome to the team!!", 0.0625)
slow_print("Jim: We are going to start testing tomorrow!", 0.0625)
slow_print("Jim: You should take some rest now..", 0.0625)

slow_print("The next day.....")
slow_print("Jim: Everything on?!?!", 0.0625)
slow_print("Mike: Red switch on!!", 0.0625)
slow_print("Lakrry: Green switch on!!", 0.0625)
slow_print("Loon: Black is blinking?????", 0.0625)
slow_print("Jim: Shut it down!!!!", 0.0225)
slow_print("Lakrry: ITS TO LATE, ITS FULL POWER!!", 0.0625)
slow_print("BLASTTTT!!!!!!!!", 0.0625)
slow_print("You appear in a strange new word", 0.0625)
slow_print("It looks like your world but......", 0.0625)
slow_print("Robots are taking over!!!", 0.0625)
slow_print("You: There is massive spider robots everywhere", 0.0625)
slow_print("A Spider Droid is going to attack you...", 0.0625)
slow_print("Helper: Hey there!", 0.0625)
slow_print("Helper: You are going to enter your first battle", 0.0625)
slow_print("Helper: Your current health is displayed after each attack", 0.0625)
slow_print("Helper: Your attacks are displayed in a list", 0.0625)
print("--------------------------------------------------------------")

Enemy1 = Enemy("Spider Droid", 20)
Player1 = Player("You", 50)
Stun = False
maxhealcooldown = 3
healcooldown = 0

start_battle(Enemy1, Player1,  Stun, maxhealcooldown, healcooldown)
slow_print("Helper: Great job defeating your first enemy!", 0.0625)
slow_print("Helper: As you find more weponds, you'll be able to do more attacks!", 0.0625)
slow_print("Massive spider robot approaches...", 0.0625)
slow_print("Helper: Hang on here! I'll take care of this guy! =D", 0.0625)
print("--------------------------------------------------------------")
slow_print("Massive Spider Droid Stabs Helper robot! strength: 50",  0.0625)
slow_print("Helper Robot is deciding which attack....",  0.0625)
slow_print("Helper Robot ZAPS! strength: 500",  0.0625)
slow_print("Massive Spider Droid was defeated.",  0.0625)
print("--------------------------------------------------------------")

slow_print("Helper: Wow that guy was easy!", 0.0625)
slow_print("Who are.... you?", 0.0625)
slow_print("Helper: I'm just here to help!", 0.0625)
slow_print("You: Ohhhhhhh..... okay I'll see you then!", 0.0625)
slow_print("Helper: I'm always here to help! Bye!", 0.0625)
slow_print("-------Helper Robot Flies Away---------", 0.0625)



