power_data_list = []
def figure_out_attacks_(character):
    power_data_list.clear()

    if(character == "Spider Droid"):
        power_data_list["club swing"] = {
            "strength": 30,
            "power": "slams ground with a club!",
            "description": "massive club",
            "stun": True } 
        
    if(character == "Player"):
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
        

    if(character == "Pikachu"):
        power_data_list["punch"] = {
            "strength": 25,
            "power": "puches!",
            "description": "uses your fists",
            "stun": False } 
    if(character == "Helper Robot"):
        power_data_list["Zap"] = {
            "strength": 500,
            "power": "ZAPS",
            "description": "uses your fists",
            "stun": False } 
