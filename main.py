"""
Main Script for StoneKnight
Created by Josh and Allen
Version 1.0
"""
from backpack_system import Backpack

import time
import sys
import random




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
power_data["iron_tail"] = {
    "strength": 50,
    "power": "slams with an iron tail!",
    "description": "metallic glow",
    "stun": True
}




def figure_out_attacks(character):
    power_data.clear()

    if(character == "Troll with club"):
        power_data["club swing"] = {
            "strength": 50,
            "power": "slams ground with a club!",
            "description": "massive club",
            "stun": True } 
        
    if(character == "Player"):
        power_data["punch"] = {
            "strength": 50,
            "power": "puches!",
            "description": "uses your fists",
            "stun": False } 
    if(character == "Pikachu"):
        power_data["punch"] = {
            "strength": 50,
            "power": "puches!",
            "description": "uses your fists",
            "stun": False } 










class Power:
    def __init__(self, power_type):
        pass

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
            time.sleep(1)  
        else:
            print(f"{self.name} took damaged. Current health: {self.health}")
            time.sleep(1)  
    def heal(self, healing):
        if not self.life:
            print(f"{self.name} is no longer with us, you can't heal the dead")
            time.sleep(1)  
        else:
            self.health += healing
            print(f"{self.name} is healed. Current health: {self.health}")
            if self.health >= 50:
                self.health = 50
                print(f"{self.name} is at full health.")
                time.sleep(1)  
    def get_string(self):
        return(self.power)

    
class Belly_Badge_Care_Bear(Care_Bear):
    def __init__(self, name, power):
        Care_Bear.__init__(self, name)
        self.power = Power(power)
        #print("self power:",self.power.strength)
        
    def help_(self):
        print(f"{self.name} joins in for the Care Bear Stare and "
              + f"{self.power.stare()}")
        
        
    def get_strength(self):
        return(self.power.strength)
        
    def inflict_damage(self, enemy, used_power):
        self.power.strength = power_data[used_power]["strength"]
        #print("self.power:", self.power.strength)
        attack = random.randint(self.power.strength-5,self.power.strength+5)
        print(f"{self.name}",power_data[used_power]["power"], f"strength: {attack}")
        time.sleep(1)          
        #print(f"{self.name} strikes a powerful blow. strength: {attack}")
        enemy.take_damage(attack)
        

class Belly_Badge_Evil_Bear(Belly_Badge_Care_Bear):
    def __init__(self, name, power):
        Care_Bear.__init__(self, name)
        self.power = Power(power)
    def inflict_damage(self, hero, used_power):
        self.power.strength = power_data[used_power]["strength"]

        attack = random.randint(self.power.strength-5,self.power.strength+2)
        if attack < 0:
            attack = 0        
        
        print(f"{self.name}",power_data[used_power]["power"], f"strength: {attack}")
        time.sleep(1)        

        hero.take_damage(attack)

        

print("-----------------------------------------")
print("           STONE KNIGHT                  ")
print("         Created By Josh and Allen       ")
print("-----------------------------------------")


def slow_print(text, delay=0.1):
    for char in text:
        # Use sys.stdout.write to print without adding a newline automatically
        sys.stdout.write(char)
        # Flush ensures the character appears immediately on the screen
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Final newline after the text is finished

my_backpack = Backpack(300, capacity=5)

name = input("Choose your name: ")
slow_print("Mom: The village is under attack!!", delay=0.025)
slow_print("Mom: You must save the village!!", delay=0.05)
slow_print("*You walk out of your house*", delay=0.05)
slow_print("*You see monsters everwhere*", delay=0.05)
slow_print("*A monster approaches you*", delay=0.05)

Pikachu = Belly_Badge_Evil_Bear("Pikachu", "thundershock")
Charizard = Belly_Badge_Care_Bear(name, "star")
Stun = False
maxhealcooldown = 3
healcooldown = 0
def start_battle():
    global Stun, maxhealcooldown, healcooldown
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
                    figure_out_attacks(Pikachu.name)
                    healcooldown += 1
                    pikachu_attack = random.choice(list(power_data.keys()))
                    time.sleep(1)

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
                time.sleep(1)          

            else:
                figure_out_attacks("Player")
                print("---Here are your attacks----")
                for attack, details in power_data.items():
                    print(f"Attack: {attack} | Strength: {details['strength']}")          
                    time.sleep(1)  



                attack_ = input("What attack do you use? ")
                if (attack_ == "heal"):
                    Charizard.heal(5)
                elif(attack_ == "thundershock"):
                    Stun = True
                    Charizard.inflict_damage(Pikachu, attack_)
                else:
                    Charizard.inflict_damage(Pikachu, attack_)
            
        slow_print("Next....", delay=0.05)
        if not Pikachu.life or not Charizard.life:
            break
    if Charizard.life:
        print(f"Congrats you defeated {Pikachu.name}!")
        time.sleep(1)  
    else:
        print(f"{Pikachu.name} defeated you.")
        time.sleep(1)  

start_battle()

slow_print("*Wow that was a close one*", delay=0.05)
slow_print("*Villager: Wow, I have never seen that before!*", delay=0.05)
slow_print("*Villager: Here you are, here is your very own wooden sword*", delay=0.05)
my_backpack.add_item("Wooden Sword", 1.0)
my_backpack.show_inventory()
time.sleep(2)  

slow_print("Oh no here come another monster!!", delay=0.05)
Pikachu = Belly_Badge_Evil_Bear("Troll with club", "thundershock")
Charizard = Belly_Badge_Care_Bear(name, "star")
Stun = False
maxhealcooldown = 3
healcooldown = 0
start_battle()


