from tabulate import tabulate


# -------------------
# Room Class
# -------------------
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name


# -------------------
# Map Class
# -------------------
class Map:
    def __init__(self, name, start_row, start_col, rooms):
        self.name = name
        self.start_row = start_row
        self.start_col = start_col
        self.rooms = rooms

    def view_map(self):
        print(f"\n{self.name}")
        print(tabulate(self.rooms, tablefmt="grid"))


# -------------------
# Player Class
# -------------------
class Player:
    def __init__(self, name, game_map):
        self.name = name
        self.map = game_map
        self.location = [game_map.start_row, game_map.start_col]

    def move(self, direction):
        row = self.location[0]
        col = self.location[1]

        if direction == "north":
            if row > 0:
                self.location[0] -= 1
            else:
                print("You cannot move north.")
                return

        elif direction == "south":
            if row < len(self.map.rooms) - 1:
                self.location[0] += 1
            else:
                print("You cannot move south.")
                return

        elif direction == "east":
            if col < len(self.map.rooms[0]) - 1:
                self.location[1] += 1
            else:
                print("You cannot move east.")
                return

        elif direction == "west":
            if col > 0:
                self.location[1] -= 1
            else:
                print("You cannot move west.")
                return

        current_room = self.get_current_room()
        print(f"\nYou moved {direction}.")
        print(f"You are now in the {current_room.name}.")
        print(current_room.description)

    def get_current_room(self):
        row = self.location[0]
        col = self.location[1]
        return self.map.rooms[row][col]

    def change_map(self, new_map):
        self.map = new_map
        self.location = [new_map.start_row, new_map.start_col]

        print(f"\nYou traveled to {new_map.name}!")
        room = self.get_current_room()
        print(f"You arrive in the {room.name}.")


# -------------------
# Haunted House Map
# -------------------
haunted_house = Map(
    "Haunted House",
    0,
    0,
    [
        [
            Room("Entrance Hall", "The front door creaks behind you."),
            Room("Living Room", "Dust covers the furniture."),
            Room("Dining Room", "A long table sits abandoned."),
            Room("Kitchen", "Old dishes are scattered around.")
        ],
        [
            Room("Library", "Ancient books line the shelves."),
            Room("Ghost Room", "A cold breeze chills the air."),
            Room("Staircase", "The stairs groan loudly."),
            Room("Bathroom", "A cracked mirror hangs on the wall.")
        ],
        [
            Room("Bedroom", "A bed is covered in cobwebs."),
            Room("Attic", "Strange noises come from above."),
            Room("Storage Room", "Boxes are stacked everywhere."),
            Room("Secret Chamber", "A hidden room full of mysteries.")
        ],
        [
            Room("Basement", "The room smells damp."),
            Room("Boiler Room", "Old machinery rumbles."),
            Room("Tunnel", "A dark tunnel stretches ahead."),
            Room("Portal", "A magical portal glows here.")
        ]
    ]
)

# -------------------
# Underwater Map
# -------------------
underwater_world = Map(
    "Underwater World",
    0,
    0,
    [
        [
            Room("Coral Reef", "Colorful fish swim around you."),
            Room("Sea Cave", "The cave walls sparkle."),
            Room("Kelp Forest", "Tall kelp waves in the water."),
            Room("Sunken Ship", "A shipwreck rests on the seabed.")
        ],
        [
            Room("Pearl Bed", "Pearls cover the ocean floor."),
            Room("Shark Zone", "You spot fins nearby."),
            Room("Deep Trench", "The water becomes very dark."),
            Room("Mermaid Lagoon", "A peaceful lagoon appears.")
        ],
        [
            Room("Whirlpool", "The current pulls strongly."),
            Room("Crystal Cavern", "Crystals glow underwater."),
            Room("Octopus Den", "An octopus watches you."),
            Room("Portal", "A portal leads back home.")
        ]
    ]
)

# -------------------
# Create Player
# -------------------
player = Player("Explorer", haunted_house)


# -------------------
# Movement Menu
# -------------------
def movement_menu():
    while True:
        print("\n--- Movement Menu ---")
        print("1. North")
        print("2. South")
        print("3. East")
        print("4. West")
        print("5. Quit")

        choice = input("Choice: ").lower()

        if choice in ["1", "north"]:
            player.move("north")
        elif choice in ["2", "south"]:
            player.move("south")
        elif choice in ["3", "east"]:
            player.move("east")
        elif choice in ["4", "west"]:
            player.move("west")
        elif choice in ["5", "quit"]:
            break
        else:
            print("Invalid action.")


# -------------------
# Main Menu
# -------------------
while True:
    current_room = player.get_current_room()

    print(f"\nMap: {player.map.name}")
    print(f"Current Room: {current_room.name}")

    print("\n--- Main Menu ---")
    print("1. Move")
    print("2. View Map")
    print("3. Travel to Other Map")
    print("4. Quit")

    choice = input("Choice: ")

    if choice == "1":
        movement_menu()

    elif choice == "2":
        player.map.view_map()

    elif choice == "3":
        if player.map == haunted_house:
            player.change_map(underwater_world)
        else:
            player.change_map(haunted_house)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid action.")