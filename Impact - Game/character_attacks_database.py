# -----------------------------------------------------------------------------
# Created By: Josh Panko
# Created Date: 05/25/2026
# Version 2 (Fully working)
# -----------------------------------------------------------------------------
"""
A system to find the power moves of characters and do things with it.
"""
# -----------------------------------------------------------------------------

power_data_list = {}


def figure_out_attacks_(character: str):
    """
    Input the character, gives out the moves and actions of said character.
    """
    power_data_list.clear()

    if (character == "Spider Droid"):
        power_data_list["club swing"] = {
            "strength": 30,
            "power": "slams ground with a club!",
            "description": "massive club",
            "stun": True}
        power_data_list["Spider Pounce"] = {
            "strength": 40,
            "power": "Jumps on top of you!",
            "description": "Gravity Ram",
            "stun": True}
    elif (character == "Player"):
        power_data_list["punch"] = {
            "strength": 30,
            "power": "puches!",
            "description": "uses your fists",
            "stun": False}
        power_data_list["kick"] = {
            "strength": 20,
            "power": "kicks!",
            "description": "uses your feet!",
            "stun": True}
    elif (character == "Pikachu"):
        power_data_list["punch"] = {
            "strength": 25,
            "power": "puches!",
            "description": "uses your fists",
            "stun": False}
    elif (character == "Helper Robot"):
        power_data_list["Zap"] = {
            "strength": 60,
            "power": "ZAPS",
            "description": "Zaps you with lightning",
            "stun": True}
        power_data_list["Bolt"] = {
            "strength": 70,
            "power": "Bolt!!!",
            "description": "Produces a pure bolt of energy",
            "stun": True}
        power_data_list["Kick"] = {
            "strength": 90,
            "power": "kickes",
            "description": "Kicks you",
            "stun": True}
