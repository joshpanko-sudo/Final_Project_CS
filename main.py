"""
Main Script for StoneKnight
Created by Josh and Allen
Version 1.0
"""
from backpack_system import Backpack




import time
import sys


print("-----------------------------------------")
print("           STONE KNIGHT                  ")
print("         Created By Josh and Allen       ")
print("-----------------------------------------")


def slow_print(text, delay=0.1):
    for char in text:
        # Use sys.stdout.write to print without adding a newline automatically
        sys.stdout.write(char)
        # Flush ensures the character appears immediately on the screen
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Final newline after the text is finished


my_backpack = Backpack(300, capacity=5)


name = input("Choose your name: ")
slow_print("Mom: The village is under attack!!", delay=0.025)
slow_print("Mom: You must save the village!!", delay=0.05)
slow_print("*You walk out of your house*", delay=0.05)
slow_print("*You see monsters everwhere*", delay=0.05)
slow_print("*A monster approaches you*", delay=0.05)


from combat_system import Belly_Badge_Care_Bear

slow_print("*Wow that was a close one*", delay=0.05)
slow_print("*Villager: Wow, I have never seen that before!*", delay=0.05)
slow_print("*Villager: Here you are, here is your very own wooden sword*", delay=0.05)
my_backpack.add_item("Wooden Sword", 1.0)
my_backpack.show_inventory()
