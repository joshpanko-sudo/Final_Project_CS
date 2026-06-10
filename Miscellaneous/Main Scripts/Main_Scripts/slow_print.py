import sys
import time

class slow_print():
    def __init__(self, text:str, delay:float) -> None:
        delay = delay or 0.1
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()