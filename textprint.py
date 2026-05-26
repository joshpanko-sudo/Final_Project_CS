# class TextScript:
#     def __init__(self, text, delimiter="|"):
#         self.chunks = text.split(delimiter)
#         self.index = 0

#     def __rshift__(self, _):
#         if self.index < len(self.chunks):
#             chunk = self.chunks[self.index].strip()
#             self.index += 1
#             print(chunk)
#         else:
#             print("[End of script]")
#         return self


# class Character:
#     def __init__(self, name):
#         self.name = name

#     def say(self, text):
#         print(f"{self.name}:")
#         return TextScript(text)


# akira = Character("Akira")

# akira.say("""
# You finally arrived.|
# I've been waiting for you.|
# ...Did you miss me?
# """) >> None >> None >> None >> None


VN("""
[Akira] You're late.|
[You] S-sorry!|
[Akira] Heh. Cute.
""") >> 0 >> 0 >> 0


class VN:
    def __init__(self, text):
        self.lines = [l.strip() for l in text.split("|")]
        self.i = 0

    def __rshift__(self, _):
        if self.i < len(self.lines):
            print(self.lines[self.i])
            self.i += 1
        return self

    def say(self, text):
        return TextScript(text)