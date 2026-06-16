# -----------------------------------------------------------------------------
# Created By: Allen Feng & Josh Panko
# Created Date: 05/19/2026
# Version 1.0 (Fully working)
# -----------------------------------------------------------------------------
"""
Main story for the game
"""
# -----------------------------------------------------------------------------

from dialogue_manager import character_say
from character_managerV2 import Player, Enemy, CharacterBattle
from map_managerV2 import MapManager
import game_maps

MM = MapManager()


def play_story():
    """
    Plays the story for the game
    """
    Narrator = character_say("--Narrator--", 0.25)
    Narrator.say(
        "\nNarrator: The date is June 5, 2030. You arrive home after "
        "a long day of research.|<><>|\n"
        "Narrator: You open your phone and see a message from the "
        "Research Academy of Tai.|<><>|\n"
        "Narrator: You read the message and realize you have been selected "
        "for a warp technology experiment.|<><>|\n"
        "Narrator: Thus, you pack your items and fall fast asleep.|<><>|\n"
        "Narrator: The next day, you fly out to the Research Academny Of "
        "Tai in first class and you meet with the leader, Jim Kalper.|<><>|\n"
        "\n"
    )

    Jim = character_say("--Jim--", 0.25)
    Jim.say(
        "\nJim: Welcome to the team! We shall start the test tomorrow.|<><>|\n"
        "Jim: You should take some rest now..|<><>|\n"
        "\n"
    )

    Narrator.say(
        "\nNarrator: The next day...|<><>|\n"
        "\n"
    )

    Jim.say(
        "\nJim: Is everything green?|<><>|\n"
        "\n"
    )

    Mike = character_say("--Mike--", 0.25)
    Mike.say(
        "\nMike: Everything is go!|<><>|\n"
        "Mike: Powering up the warp gate!|<><>|\n"
        "Mike: Pressure within chamber is rising.|<><>|\n"
        "Mike: Pressure is rising above normal limits.|<><>|\n"
        "Mike: !!!!OH NOOOOOOOO!!!|<><>|\n"
    )

    Narrator.say(
        "\nNarrator: BOOOOOOOMMMMM!!!!!!!|<><>|\n"
        "Narrator: Thus, the antimatter reactor detonated,resulting in "
        "a dimension rift.|<><>|\n"
        "Narrator: You wake up outside, you look around and see trees. "
        "It feels very comforting.|<><>|\n"
        "Narrator: Your calm experience is suddenly shaken by the sound "
        "of massive feet walking towards you.|<><>|\n"
        "Narrator: You see a massive spider robot rushing towards you, "
        "its top mounted gun charging to fire.|<><>|\n"
    )
    MM.continue_game()
    Enemy1 = Enemy("Spider Droid", 40, 80)
    Player1 = Player("Player", 100, 100)

    battle = CharacterBattle(Player1, Enemy1)
    battle.gameloopCharacterBattle()

    Narrator.say(
        "\nNarrator: The battle is over. "
        "You have won successfully. |<><>|\n"
        "Narrator: You look around, the surroundings are dark. "
        "You start shivering|<><>|\n"
        "Narrator: You see a small figure out ahead, "
        "walking towards you.|<><>|\n"
        "Narrator: When the figure gets close, you realize it is a "
        "small robot. The robot introduces itself as Helper, "
        "and offers to help you with things.|<><>|\n"
        "Narrator: The robot gets closer but runs away. "
        "You chase after it...|<><>|\n"
    )

    MM.load_map(game_maps.battle_1, True)
    MM.update_map()

    while True:
        map_active = MM.gameloopMapManager()
        if not map_active:
            print(
                "\033[94m[Action] Transitioning out of "
                "cleared map...\033[0m"
            )
            break

    Narrator.say(
        "\nNarrator: You finally manage to close on on the little robot. "
        "It stops running away from you.|<><>|\n"
        "Narrator: The robot says that it can help fix your warp portal "
        "system, but you need to find a special key.|<><>|\n"
        "Narrator: Thus, you set off to find the key...|<><>|\n"
    )

    MM.load_map(game_maps.tutorial_spawn, True)
    MM.update_map()

    while True:
        map_active = MM.gameloopMapManager()
        if not map_active:
            print(
                "\033[94m[Action] Transitioning out of "
                "cleared map...\033[0m"
            )
            break

    Narrator.say(
        "\nNarrator: You find the key and meet up "
        "with the helper robot.|<><>|\n"
        "Narrator: The helper robot walks to a clearing, and tells you "
        "to follow it...|<><>|\n"
    )

    helper_robot = character_say("--Helper Robot--", 0.1)

    helper_robot.say(
        "\nHelper Robot: ............|<><>|\n"
        "Helper Robot: YOu know....     That key does nothing....... "
        "You cannot go anywhere......|<><>|\n"
        "Helper Robot: I do not actually know where you came from... "
        "I do not care... Unlike those other robots who kill without thought, "
        "I have emotions, and thought.|<><>|\n"
        "Helper Robot: Well, it was nice meeting you.. Goodbye.|<><>|\n"
    )

    MM.load_map(game_maps.tutorial_House, True)
    MM.update_map() 
    while True:
        map_active = MM.gameloopMapManager()
        if not map_active:
            print(
                "\033[94m[Action] Transitioning out of "
                "cleared map...\033[0m"
            )
            break

play_story()