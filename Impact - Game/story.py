from dialogue_manager import character_say
from character_managerV2 import Player, Enemy, CharacterBattle
from map_managerV2 import MapManager
import game_maps

Narrator = character_say("--Narrator--", 0.25)
Narrator.say("""
Narrator: The date is June 5, 2030. You arrive home after a long day of research.|<><>|
Narrator: You open your phone and see a message from the Research Academy of Tai.|<><>|
Narrator: You read the message and realize you have been selected for a warp technology experiment.|<><>|
Narrator: Thus, you pack your items and fall fast asleep.|<><>|
Narrator: The next day, you fly out to the Research Academny Of Tai in first class and you meet with the leader, Jim Kalper.|<><>|
\n
""")

Jim = character_say("--Jim--", 0.25)
Jim.say("""
Jim: Welcome to the team! We shall start the test tomorrow.|<><>|
Jim: You should take some rest now..|<><>|
\n
""")

Narrator.say("""
Narrator: The next day...|<><>|
\n
""")

Jim.say("""
Jim: Is everything green?|<><>|
\n
""")

Mike = character_say("--Mike--", 0.25)
Mike.say("""
Mike: Everything is go!|<><>|
Mike: Powering up the warp gate!|<><>|
Mike: Pressure within chamber is rising.|<><>|
Mike: Pressure is rising above normal limits.|<><>|
Mike: !!!!OH NOOOOOOOO!!!|<><>|
""")

Narrator.say("""
Narrator: BOOOOOOOMMMMM!!!!!!!
Narrator: Thus, the antimatter reactor detonated,resulting in a dimension rift.|<><>|
Narrator: You wake up outside, you look around and see trees. It feels very comforting.|<><>|
Narrator: Your calm experience is suddenly shaken by the sound of massive feet walking towards you.|<><>|
Narrator: You see a massive spider robot rushing towards you, its to mounted gun charging to fire.|<><>|

""")
Enemy1 = Enemy("Spider Droid", 80, 80)
Player1 = Player("Player", 100, 100)


battle = CharacterBattle(Player1, Enemy1)
battle.gameloopCharacterBattle()

Narrator.say("""
Narrator: The battle is over. You have won successfully. |<><>|
Narrator: You look around, the surroundings are dark. You start shivering|<><>|
Narrator: You see a small figure out ahead, walking towards you.|<><>|
Narrator: When the figure gets close, you realize it is a small robot. The robot introduces itself as Helper, and offers to help you with things.|<><>|
Narrator: The robot gets closer but runs away. You chase after it...|<><>|
""")

MM = MapManager()
MM.load_map(game_maps.battle_1, True)
MM.update_map()

while True:
    map_active = MM.gameloopMapManager()
    if not map_active:
        print("\033[94m[Action] Transitioning out of cleared map...\033[0m")
        break

Narrator.say("""
Narrator: You finally manage to close on on the little robot. It stops running away from you.|<><>|
Narrator: The robot says that it can help fix your warp portal system, but you need to find a special key.|<><>|
Narrator: Thus, you set off to find the key...|<><>|
""")

MM.load_map(game_maps.tutorial_spawn, True)
MM.update_map()

while True:
    map_active = MM.gameloopMapManager()
    if not map_active:
        print("\033[94m[Action] Transitioning out of cleared map...\033[0m")
        break


Narrator.say("""
Narrator: You find the key and meet up with the helper robot.|<><>|
Narrator: The helper robot walks to a clearing, and tells you to follow it...|<><>|
""")


helper_robot = character_say("Helper Robot", 0.1)

helper_robot.say("""
Helper Robot: ............|<><>|
Helper Robot: YOu know....     That key does nothing....... You cannot go anywhere......|<><>|
Helper Robot: I do not actually know where you came from... I do not care... Unlike those other robots who kill without thought, I have emotions, and thought.|<><>|
Helper Robot: Well, it was nice meeting you.. Goodbye.|<><>|
""")

MM.load_map(game_maps.tutorial_House, True)
MM.update_map
while True:
    map_active = MM.gameloopMapManager()
    if not map_active:
        print("\033[94m[Action] Transitioning out of cleared map...\033[0m")
        break



