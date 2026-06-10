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
    def __init__(self, text:str, delay:float) -> None:
        delay = delay or 0.1
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()