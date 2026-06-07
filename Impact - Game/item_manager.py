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
try:
    from tabulate import tabulate
except ImportError as e:
    print(f"Warning: ItemManager could not load tabulate. {e}. Perhaps you have not installed it?")
    quit()

try:
    import questionary
except ImportError as e:
    print(f"Warning: ItemManager could not load questionary. {e}. Perhaps you have not installed it?")
    quit()

class ItemManager():
    def __init__(self, inventory_name:str) -> None:
        '''
        Intialize the class
        '''
        self.item_capacity = 0 # Inventory capacity
        self.items =  [] # Inventory
        self.inventory_name = inventory_name # Inventory name
        self.custom_headers = {"name": "Item Name", "amount": "Quantity", "stack": "Max Stack"}


    def set_capacity(self, inventory_capacity:int):
        '''
        Sets the capacity of the inventory
        '''
        self.item_capacity = inventory_capacity
        

    def add_item(self, item_name:str, item_amount:int, max_stack:int):
        '''
        Adds an item to the inventory. User can specify name, amount to add, and a stack size for them item to stack.
        '''
        for item in self.items: # Loop through the items
            if item["name"] == item_name and item["amount"] < item["stack"]: # Finds if the item the user wants to add already exists
                available_space = item["stack"] - item["amount"] # Finds avaliable space in item stack
                if item_amount <= available_space: # If amount to add is smaller than avaliable space
                    item["amount"] += item_amount # Add item
                    item_amount = 0
                    break # Exit loop
                else:
                    item["amount"] = item["stack"]
                    item_amount -= available_space
        while item_amount > 0:
            if len(self.items) >= self.item_capacity:
                print(f"{self.inventory_name} is full! Could not add remaining {item_amount}x {item_name}.") # Inventory is full
                break
            amount_to_add = min(item_amount, max_stack)
            self.items.append({
                "name": item_name, 
                "amount": amount_to_add, 
                "stack": max_stack
            }) # Add a new stack
            print(f"Items: {item_amount}x {item_name} has been added to {self.inventory_name}") # Summary of items added
            item_amount -= amount_to_add
    
    def remove_item(self, item_name:str, item_amount:int):
        '''
        Remove items from the inventory
        '''
        for i in range(len(self.items) - 1, -1, -1): #Start -1, stop -1, step -1
            item = self.items[i]
            if item["name"] == item_name:
                if item["amount"] <= item_amount:
                    item_amount -= item["amount"] #Item stack is less than requested item removal
                    self.items.pop(i) #Remove stack
                else:
                    item["amount"] -= item_amount 
                    item_amount = 0 #Everything removed
                    break #Leave loop
        print(f"Removed {item_amount}x {item_name} from {self.inventory_name}")
        if item_amount > 0:
            print(f"Could not remove {item_amount}x {item_name} from {self.inventory_name}.")

    def see_item(self, item_name:str):
        '''
        See if a certain item exists within the inventory
        '''
        for item in self.items:
            if item.get("name") == item_name:
                print(f'The item "{item_name}" is in the {self.inventory_name}!')
                return True
            else:
                print(f'The item "{item_name}" is not in the {self.inventory_name}!')
                return False


    def see_inventory(self):
        '''
        See the full contents of the inventory
        '''
        print(f"\n{self.inventory_name.center(40, '-')}")
        if not self.items:
            print(f"{self.inventory_name} is empty.")
        else:
            print(f"\nInventory capacity: {self.item_capacity}")
            print(tabulate(self.items, headers=self.custom_headers, tablefmt="fancy_grid"))
        print("-" * 40)
        
    def gameloopItemManager(self):
        command = questionary.select(f"{self.inventory_name} menu:",choices=[f"View {self.inventory_name}", "Find item"]).ask()
        if command == f"View {self.inventory_name}":
            self.see_inventory()
        else: 
            match command:
                case "Find item":
                    self.see_item(questionary.text("Item to find: ").ask())
                case _:
                    print("Warning: ItemManager has encountered a fatal error")
                    quit()
                        


backpack = ItemManager("Allen's Inventory")
backpack.set_capacity(4)
# backpack.add_item("Banana", 10)
backpack.add_item("Apple", 20, 5)
backpack.add_item("Banana", 20, 64)
backpack.see_item("Apple")
backpack.see_item("jirvnkjr4vgnk")
while True:
    backpack.gameloopItemManager()


# inventory = [
#     {"name": "Apple", "amount": 10, "stack": 64},
#     {"name": "Apple", "amount": 10, "stack": 64},
#     {"name": "Apple", "amount": 10, "stack": 64},
#     {"name": "Apple", "amount": 10, "stack": 64},
#     {"name": "Apple", "amount": 10, "stack": 64},
# ]