'''
Legend:
- Name: DialogueManager

Highlight Codes:
- Red: Error
- Green: Working
- Blue: Action being done

Error template:
- Warning: DialogueManager could not {Error Here}. {e}. Please {Possible Solution Here}


'''
try:
    import sys
except ImportError as e:
    print(f"Warning: DialogueManager could not load sys. {e}. Perhaps you have not installed it?")
    quit()

try:
    import time
except ImportError as e:
    print(f"Warning: DialogueManager could not load time. {e}. Perhaps you have not installed it?")
    quit()

class slow_print_system():
    @staticmethod
    def slow_print(text:str, delay = 0.1):
        '''
        Takes in a text string and can print out lines for dialogue
        Delay can be adjusted or defualts to 0.
        '''
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()


class character_say():
    '''
    A more advanced systen for printing out character dialogue. You can specify character name and what they should say
    The printing system uses the slow print above and lines print out with a delay that defaults to 0.75
    '''
    def __init__(self, name:str, delay = 0.75):
        self.name = name # Character name
        self.delay = delay # Line print delay

    def say(self, text:str, special_character = "|<><>|"): # Special character that allows for one long string to be broken up and print out seperatly as lines
        print(f"{self.name}")

        text_chunks = text.split(special_character) # Splits the string

        for chunk in text_chunks:
            purged_chunk = chunk.strip()
            if purged_chunk:
                time.sleep(self.delay) # Delay the print
                slow_print_system.slow_print(purged_chunk, 0.125)
                








# akira = character_say("Akira")

# akira.say("""
# You finally arrived.|<><>|
# I've been waiting for you.|
# ...Did you miss me?
# """)