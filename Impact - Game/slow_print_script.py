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
