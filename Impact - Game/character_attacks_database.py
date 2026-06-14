power_data_list = {}
def figure_out_attacks_(character:str):
    power_data_list.clear()

    if (character == "Spider Droid"):
        power_data_list["club swing"] = {
            "strength": 30,
            "power": "slams ground with a club!",
            "description": "massive club",
            "stun": True } 
    elif (character == "Player"):
        power_data_list["punch"] = {
            "strength": 30,
            "power": "puches!",
            "description": "uses your fists",
            "stun": False } 
        power_data_list["kick"] = {
            "strength": 20,
            "power": "kicks!",
            "description": "uses your feet!",
            "stun": True }
    elif (character == "Pikachu"):
        power_data_list["punch"] = {
            "strength": 25,
            "power": "puches!",
            "description": "uses your fists",
            "stun": False } 
    elif(character == "Helper Robot"):
        power_data_list["Zap"] = {
            "strength": 40,
            "power": "ZAPS",
            "description": "Zaps you with lightning",
            "stun": True } 
        
    