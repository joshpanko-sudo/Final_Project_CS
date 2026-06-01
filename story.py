# Researchers have managed to create warp technology, and you are 
# selected as a researcher to warp in. You emerge in a advanced world that is under attack by a 
# robot reveloution. You vessel is damaged, and you will need to repair it. You blend into this world as 
# a "knight" (Hired by the united government to fight the robots). You defend your base while also finding 
# parts to fix your vessel.
import sys
import time
import random

def slow_print(text, delay=0.1):
    for char in text:
        # Use sys.stdout.write to print without adding a newline automatically
        sys.stdout.write(char)
        # Flush ensures the character appears immediately on the screen
        sys.stdout.flush()
        time.sleep(delay)
    print()  


slow_print("You arrive home from studying at the highest science techology university", delay=0.125)
slow_print("You see that you got mail. You open up your mail box", 0.125)
slow_print("You have been selected as a researcher to try time travel!", 0.125)