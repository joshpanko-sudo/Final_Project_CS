'''
Legend:
- Name: ItemManager

Highlight Codes:
- Red: Error
- Green: Working
- Blue: Action being done

Error template:
- Warning: ItemManager could not {Error Here}. {e}. Please {Possible Solution Here}


'''
from tabulate import tabulate

class ItemManager():
    def __init__(self, inventory_name:str) -> None:
        self.item_capacity = 0
        self.items =  []
        self.inventory_name = inventory_name


    def set_capacity(self, inventory_capacity:int):
        self.item_capacity = inventory_capacity
        

    def add_item(self, item_name:str, item_amount:int, max_stack:int):
        for item in self.items:
            if item["name"] == item_name and item["amount"] < item["stack"]:
                available_space = item["stack"] - item["amount"]
                if item_amount <= available_space:
                    item["amount"] += item_amount
                    item_amount = 0
                    break
                else:
                    item["amount"] = item["stack"]
                    item_amount -= available_space
        while item_amount > 0:
            if len(self.items) >= self.item_capacity:
                print(f"{self.inventory_name} is full! Could not add remaining {item_amount}x {item_name}.")
                break
            amount_to_add = min(item_amount, max_stack)
            self.items.append({
                "name": item_name, 
                "amount": amount_to_add, 
                "stack": max_stack
            })
            print(f"Items: {item_amount}x {item_name} has been added to {self.inventory_name}")
            item_amount -= amount_to_add
    
    def remove_item

    def see_item(self, item_name:str):
        for item in self.items:
            if item.get("name") == item_name:
                print(f'The item "{item_name}" is in the {self.inventory_name}!')
                return True
            else:
                print(f'The item "{item_name}" is not in the {self.inventory_name}!')
                return False


    def see_inventory(self):
            print(f"\nInventory capacity: {self.item_capacity}")
            print(tabulate(self.items, headers="keys", tablefmt="fancy_grid"))
        


backpack = ItemManager("Allen's Inventory")
backpack.set_capacity(4)
# backpack.add_item("Banana", 10)
backpack.add_item("Apple", 20, 5)
backpack.add_item("Banana", 20, 64)
backpack.see_item("Apple")
backpack.see_item("jirvnkjr4vgnk")
backpack.see_inventory()
# backpack.add_item("Apple", 10)
        # else:
        #     self.items.append()

# Our list of dictionaries
# users = [
#     {"name": "Alice", "role": "Admin"},
#     {"name": "Bob", "role": "Developer"},
#     {"name": "Charlie", "role": "Designer"}
# ]

# # Loop through the list and extract the names
# for user in users:
#     print(user["name"])

# inventory = [
#     {"name": "Apple", "amount": 10, "stack": 64},
#     {"name": "Apple", "amount": 10, "stack": 64},
#     {"name": "Apple", "amount": 10, "stack": 64},
#     {"name": "Apple", "amount": 10, "stack": 64},
#     {"name": "Apple", "amount": 10, "stack": 64},
# ]






class Backpack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = []




    def add_amount(self, target_name, value_to_add):
        for item in self.items:
            if item.get("name") == target_name:
                item["amount"] = item.get("amount", 0) + value_to_add
                break 
#        print(next((item["amount"] for item in self.items if item.get("name") == target_name), 0))\
    def remove_amount(self, target_name, value_to_add):
        for item in self.items:
            if item.get("name") == target_name:
                item["amount"] = item.get("amount", 0) - value_to_add
                break 
    def show_inventory(self):
        print("\n------BACKPACK INVENTORY------")
        if not self.items:
            print("Your backpack is empty.")
        else:
            for index, item in enumerate(self.items, 1):
                print(f"{index}. {item['name']}  {item['amount']}")
                pass
            
        print("----------------------------------\n")

#my_backpack = Backpack(capacity=5)

#my_backpack.add_item("Healing Potion", 2)
#my_backpack.add_item("Iron Sword", 1)

#my_backpack.remove_item("Healing Potion")
#my_backpack.add_amount("Iron Sword", 3)
#my_backpack.remove_amount("Iron Sword", 2)
#my_backpack.show_inventory()