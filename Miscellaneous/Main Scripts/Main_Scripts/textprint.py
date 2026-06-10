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


# VN("""
# [Akira] You're late.|
# [You] S-sorry!|
# [Akira] Heh. Cute.
# """) >> 0 >> 0 >> 0


# class VN:
#     def __init__(self, text):
#         self.lines = [l.strip() for l in text.split("|")]
#         self.i = 0

#     def __rshift__(self, _):
#         if self.i < len(self.lines):
#             print(self.lines[self.i])
#             self.i += 1
#         return self

#     def say(self, text):
#         return TextScript(text)