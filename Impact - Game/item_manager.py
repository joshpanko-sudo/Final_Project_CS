
class Backpack:
    def __init__(self, gems, capacity=10):
        self.capacity = capacity
        self.items = []
        self.gems = gems 
        
    def add_item(self, item_name, weight):
        if len(self.items) >= self.capacity:
            print("Backpack is full!")
        else:
            self.items.append({"name": item_name, "weight": weight})
            print(f"Added {item_name} to your backpack.")

    def remove_item(self, item_name):
        for item in self.items:
            if item["name"].lower() == item_name.lower():
                self.items.remove(item)
                print(f"Removed {item_name} from your backpack.")
                return
        print(f"{item_name} not found in backpack.")

    def checkGems(self):
        return self.gems
    
    def removeGems(self, remove):
        self.gems -= remove

    def get_total_weight(self):
        return sum(item["weight"] for item in self.items)

    def show_inventory(self):
        print("\n------BACKPACK INVENTORY------")
        if not self.items:
            print("Your backpack is empty.")
        else:
            for index, item in enumerate(self.items, 1):
                print(f"{index}. {item['name']} ({item['weight']}kg)")
            
            print(f"{self.checkGems()} Gems")
            print(f"Total Weight: {self.get_total_weight()}kg")
        print("----------------------------------\n")


