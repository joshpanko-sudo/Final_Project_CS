"""
Main Script for StoneKnight
Created by Josh and Allen
Version 1.0
"""

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




name = input("Choose your name: ")
slow_print("Mom: The village is under attack!!", delay=0.025)
slow_print("Mom: You must save the village!!", delay=0.05)
slow_print("*You walk out of your house*", delay=0.05)
slow_print("*You see monsters everwhere*", delay=0.05)
slow_print("*A monster approaches you*", delay=0.05)