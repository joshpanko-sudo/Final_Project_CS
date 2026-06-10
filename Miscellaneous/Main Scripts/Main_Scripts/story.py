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


slow_print("You arrive home from studying at the highest science techology university", delay=0.0225)
slow_print("You see that you got mail. You open up your mail box", 0.0225)
slow_print("You have been selected as a researcher to try time travel!", 0.0225)

slow_print("The science team decided to fly you out first class.", 0.0225)
slow_print("You finally arrive and meet the leader, Jim Kalper")
slow_print("Jim: Welcome to the team!!", 0.0225)
slow_print("Jim: We are going to start testing tomorrow!", 0.0225)
slow_print("Jim: You should take some rest now..", 0.0225)

slow_print("The next day.....", 0.0625)
slow_print("Jim: Everything on?!?!", 0.0525)
slow_print("Mike: Red switch on!!", 0.0225)
slow_print("Lakrry: Green switch on!!", 0.0225)
slow_print("Loon: Black is blinking?????", 0.0225)
slow_print("Jim: Shut it down!!!!", 0.0225)
slow_print("Lakrry: ITS TO LATE, ITS FULL POWER!!", 0.0225)
slow_print("BLASTTTT!!!!!!!!", 0.00225)
slow_print("You appear in a strange new word", 0.0225)
slow_print("It looks like your world but......", 0.0225)
slow_print("Robots are taking over!!!", 0.0225)
slow_print("You: There is massive spider robots everywhere", 0.0225)

