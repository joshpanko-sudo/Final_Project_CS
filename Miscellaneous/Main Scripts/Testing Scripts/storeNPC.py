from backpack_system import Backpack


power_data = {"steak" : {"stat": "heals 50 hp", "cost": 50},
            "sword" : {"stat": "iron sword with 30 damage", "cost": 50 },
            "totem of life" : {"stat": "gives you one extra life", "cost": 500}}
print("Shop Keeper: Welcome to my shop")
print("I have:")


for i in range(len(list(power_data.keys()))):
    item = list(power_data.keys())[i]
    print(item,"- ", power_data[item]["stat"], ", Cost: ", power_data[item]["cost"], " Gems" )

my_backpack = Backpack(300, capacity=5)

print(f"You have {my_backpack.checkGems()} Gems")
choice = input("What do you want to buy: ")


second_key = list(power_data.keys())
if choice in second_key:
    if (power_data[choice]["cost"] <= my_backpack.checkGems()):
        print(my_backpack.checkGems())
        my_backpack.removeGems(power_data[choice]["cost"])
        print("You bought :", choice, "!")
        my_backpack.add_item(choice, 3.0)

    else:
        print("You don't have enough money")
else:
    print("Sorry that is not an option")

my_backpack.show_inventory()