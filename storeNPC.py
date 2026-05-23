gems_ = 150

#def printshop():

power_data = {"steak" : {"stat": "heals 50 hp", "cost": 50},
            "sword" : {"stat": "iron sword with 30 damage", "cost": 50 },
            "totem of life" : {"stat": "gives you one extra life", "cost": 500}}
print("Shop Keeper: Welcome to my shop")
print("I have:")


for i in range(len(list(power_data.keys()))):
    item = list(power_data.keys())[i]
    print(item,"- ", power_data[item]["stat"], ", Cost: ", power_data[item]["cost"], " Gems" )

choice = input("What do you want to buy: ")


second_key = list(power_data.keys())

if choice in second_key:
    if (power_data[choice]["cost"] <= gems_):
        gems_ -= power_data[choice]["cost"]
        print("You bought :", choice, "!")
        print(" You have: ", gems_, "Gems left")
    else:
        print("You don't have enough money")
else:
    print("Sorry that is not an option")
