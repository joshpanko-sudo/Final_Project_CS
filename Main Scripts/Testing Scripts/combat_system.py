import random
from backpack_system_2 import Backpack
from main import Send_Backpack
wild_pokemon = ['Pikachu', 'Charizard', 'Arceus', 'Greninja']

random_item = random.choice(wild_pokemon)
my_backpack = Backpack(capacity=5)

my_backpack.show_inventory()
#print(f"You encountered a wild Pikachu!")




    #self.items.append({"name": item_name, "amount": item_amount})




power_data = {
    "thundershock": {
        "strength": 10,
        "power": "uses thundershock!",
        "description": "red apple",
        "stun": True
    },
    "star": {
        "strength": 10,
        "power": "creates a shooting stars.",
        "description": "yellow star",
        "stun": False
    },
    "thunderwave": {
        "strength": 10,
        "power": "uses thunderwave!",
        "description": "yellow star",
        "stun": False
    },
    "kill": {
        "strength": 300,
        "power": "kills quickly",
        "description": "yellow star",
        "stun": False
    }
}

def print_attacks():
    for i in range(len(list(power_data.keys()))):
        item = list(power_data.keys())[i]
        print("- ", item,"- ", power_data[item]["strength"], ", Power: ", power_data[item]["power"])
              
class Power:
    def __init__(self, power_type):
        self.name = power_type
        self.strength = power_data[power_type]["strength"]
        self.power = power_data[power_type]["power"]
        self.description = power_data[power_type]["description"]

    def __str__(self):
        return f"{self.name.title()} gives you the power to {self.power}."
    
    def stare(self):
        return f"projects a {self.description}"

class Care_Bear:
    def __init__(self, name):
        self.name = name
        self.health = 40
        self.life = True
        
    def __str__(self):
        return f"Care Bear {self.name}"
    
    def help_(self):
        print(f"{self.name} gives moral support.")
        
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.life = False
            print(f"{self.name} was defeated.")
        else:
            print(f"{self.name} took damaged. Current health: {self.health}")
    def heal(self, healing):
        if not self.life:
            print(f"{self.name} is no longer with us, you can't heal the dead")

        else:
            self.health += healing
            print(f"{self.name} is healed. Current health: {self.health}")

            if self.health >= 50:
                self.health = 50
                print(f"{self.name} is at full health.")
                
    def get_string(self):
        print(self.power)

    
class Belly_Badge_Care_Bear(Care_Bear):
    def __init__(self, name, power):
        Care_Bear.__init__(self, name)
        self.power = Power(power)
        print("self power:",self.power.strength)
        
    def help_(self):
        print(f"{self.name} joins in for the Care Bear Stare and "
              + f"{self.power.stare()}")
        
        
    def get_strength(self):
        print(self.power.strength)
        
    def inflict_damage(self, enemy, used_power):
        self.power.strength = power_data[used_power]["strength"]
        #print("self.power:", self.power.strength)
        attack = random.randint(self.power.strength-5,self.power.strength+5)
        print(f"{self.name}",power_data[used_power]["power"], f"strength: {attack}")

        
        #print(f"{self.name} strikes a powerful blow. strength: {attack}")
        enemy.take_damage(attack)
        

class Belly_Badge_Evil_Bear(Belly_Badge_Care_Bear):
    def __init__(self, name, power):
        Care_Bear.__init__(self, name)
        self.power = Power(power)
    def inflict_damage(self, hero, used_power):
        attack = random.randint(self.power.strength-5,self.power.strength+2)
        if attack < 0:
            attack = 0        
        
        print(f"{self.name}",power_data[used_power]["power"], f"strength: {attack}")

        hero.take_damage(attack)

        

Pikachu = Belly_Badge_Evil_Bear("Small Troll", "thundershock")
Charizard = Belly_Badge_Care_Bear("You", "star")
Stun = False
maxhealcooldown = 3
healcooldown = 0

while True:
    if Pikachu.life:
        if Stun:
            print(f"{Pikachu.name} is stunned!")
            Stun = False
        else:
            if Pikachu.health <= 20 and healcooldown >= 3:
                healcooldown = 0
                Pikachu.heal(5)
            else:
                healcooldown += 1
                pikachu_attack = random.choice(list(power_data.keys()))
                print(pikachu_attack) 

                if(pikachu_attack == "thundershock"):
                    Pikachu.inflict_damage(Charizard, pikachu_attack)
                    Stun = True

                else:
                    healcooldown += 1

                    Pikachu.inflict_damage(Charizard, pikachu_attack)
            
    if Charizard.life:
        if Stun:
            print(f"{Charizard.name} is stunned!")
            Stun = False
        else:
            print("Your attacks:")
            print_attacks()
            attack_ = input("What attack do you use? ")
            if (attack_ == "heal"):
                Charizard.heal(5)
            elif(attack_ == "thundershock"):
                Stun = True
                Charizard.inflict_damage(Pikachu, attack_)
            else:
                Charizard.inflict_damage(Pikachu, attack_)
        
    input("next.....")
    if not Pikachu.life or not Charizard.life:
        break
if Charizard.life:
    print(f"Congrats you defeated {Pikachu.name}!")
else:
    print(f"{Pikachu.name} defeated you.")