class Backpack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.items = []

    def add_item(self, item_name, item_amount):
        if len(self.items) >= self.capacity:
            print("Backpack is full!")
        else:
            self.items.append({"name": item_name, "amount": item_amount})
            print(f"Added {item_name} amount: {item_amount} to your backpack.")
    def see_item(self, target_name):
        for item in self.items:
            if item.get("name") == target_name:
                print("The Item is in the backpack!")
                return True
                break 
            else:
                print("The Item is in the backpack!")
                return False




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