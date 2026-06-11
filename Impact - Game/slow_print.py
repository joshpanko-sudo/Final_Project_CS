'''
Legend:
- Name: SlowPrint

Highlight Codes:
- Red: Error
- Green: Working
- Blue: Action being done

Error template:
- Warning: SlowPrint could not {Error Here}. {e}. Please {Possible Solution Here}


'''
try:
    import sys
except ImportError as e:
    print(f"Warning: SlowPrint could not load sys. {e}. Perhaps you have not installed it?")
    quit()

try:
    import time
except ImportError as e:
    print(f"Warning: SlowPrint could not load time. {e}. Perhaps you have not installed it?")
    quit()

class slow_print_system():
    def __init__(self) -> None:
        pass

    def slow_print(self, text:str, delay:float = 0.1):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()


class character_say():
    def __init__(self, name, delay = 0.75):
        self.name = name
        self.delay = delay

    def say(self, text, special_character = "|<><>|"):
        print(f"{self.name}")

        text_chunks = text.split(special_character)

        for chunk in text_chunks:
            purged_chunk = chunk.strip()
            if purged_chunk:
                time.sleep(self.delay)
                slow_print_system.slow_print(purged_chunk, 0.125)
                






# --- How to use it ---

akira = character_say("Akira")

akira.say("""
You finally arrived.|
I've been waiting for you.|
...Did you miss me?
""")