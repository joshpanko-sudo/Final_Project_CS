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

class slow_print():
    def __init__(self, text:str, delay:float = 0.1) -> None:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()




import time
from slow_print import slow_print as SP

class Character:
    def __init__(self, name, delay=0.75):
        self.name = name
        self.delay = delay

    def say(self, text, delimiter="|"):
        print(f"{self.name}:")
        
        # Split the text into individual lines/chunks
        chunks = text.split(delimiter)
        
        # Automatically loop through and print each chunk with a delay
        for chunk in chunks:
            cleaned_chunk = chunk.strip()
            if cleaned_chunk: # Ensures we don't print empty whitespace lines
                time.sleep(self.delay)
                SP(cleaned_chunk, 0.125)
                
        print("[End of script]")

# --- How to use it ---

akira = Character("Akira")

akira.say("""
You finally arrived.|
I've been waiting for you.|
...Did you miss me?
""")