from backpack_system import Backpack


power_data = {"heavy amor" : {"stat": "best amor in the game", "cost": 50, "trade": "15 bones", "item": "bone", "amount": 15},
            "sword" : {"stat": "iron sword with 30 damage", "trade": 50 },
            "totem of life" : {"stat": "gives you one extra life", "trade": 500}}

print("Hello would you like to trade")

keys = ["a", "b", "c", "d", "e", "f", "g", "h"]

second_key = list(power_data.keys())





for i in range(len(list(power_data.keys()))):
    item = list(power_data.keys())[i]
    print("- ", item, "for:", power_data[item]["trade"], "press: ", keys[i], "to trade")


    #print(item,"- ", power_data[item]["stat"], ", Cost: ", power_data[item]["cost"], " Gems" )


