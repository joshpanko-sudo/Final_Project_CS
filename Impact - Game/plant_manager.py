# try:
#     from tabulate import tabulate
# except ImportError as e:
#     print(f"Warning: MapManager could not load tabulate. {e}. Perhaps you have not installed it?")
#     quit()

# try:
#     import questionary
# except ImportError as e:
#     print(f"Warning: MapManager could not load questionary. {e}. Perhaps you have not installed it?")
#     quit()


# class Plant():
#     def __init__(self, plant_name:str, plant_type:str, plant_description:str):
#         self.name = plant_name
#         self.type = plant_type
#         self.description = plant_description

#     def print_data(self, data_to_print):
#         try:
#             match data_to_print.strip().lower():
#                 case "name":
#                     print(self.name)
#                 case "type":
#                     print(self.type)
#                 case "description":
#                     print(self.description)
#                 case _:
#                     print("Error detected")
#                     quit()
#         except NameError as e:
#             print(f"You may have enetered the wrong data to find. {e}")

# class Garden():
#     def __init__(self, name_for_garden:str, garden:list):
#         self.name_garden = name_for_garden
#         self.garden = garden

#     def view_garden(self, input_garden):
#         try:
#             print(tabulate(input_garden, stralign="center", disable_numparse=True, tablefmt="fancy_grid"))
#         except Exception as e:
#             print(f"Warning: Garden cannot print out your garden. {e}")
#             quit()

        



# class Player():
#     def __init__(self, input_garden):
#         self.player_location = {"row": 0, "col": 0}
#         self.active_garden = input_garden

#     def move_player(self, command):
#         rows, cols = self.player_location["row"], self.player_location["col"]
#         new_row, new_col = rows, cols
#         match command:
#             case "w":
#                 new_row -= 1
#             case "a":
#                 new_col -= 1
#             case "s":
#                 new_row += 1
#             case "d":
#                 new_col += 1
            
#         if self.active_garden[new_row][new_col] is not None:
#             self.player_location["row"] = new_row
#             self.player_location["col"] = new_col

#     def gameloop(self):
#         while (command := input("W, A, S, D, E, F: ").strip().lower()) not in {"w", "a", "s", "d", "e", "f"}:
#                 print("Wrong Move")
#         else:
#                 self.move_player(command)




# carrot = Plant("Carrot", "Vegetable", "Very yummy and commonly associated with rabbits")
# lily = Plant("Lily", "Flower", "Very beautiful and refreshing to look at")
# tulip = Plant("Tulip", "Flower", "Very beautiful to look at and very calming to the mind")
# tomoto = Plant("Tomoto", "Vegetable", "Sour and yummy to eat")
# apple = Plant("Apple", "fruit", "A tech company. Recently did WWDC 26")

# garden1 = Garden("I love me", [[carrot, carrot, carrot],[lily, tulip, carrot],[apple, lily, tomoto]])
# player1 = Player(garden1)
# player1.gameloop()


class Plant():
    def __init__(self, plant_name:str, plant_type:str, plant_description:str):
        self.name = plant_name
        self.type = plant_type
        self.description = plant_description

    def print_data(self, data_to_print):
        try:
            match data_to_print.strip().lower():
                case "name":
                    print(self.name)
                case "type":
                    print(self.type)
                case "description":
                    print(self.description)
                case _:
                    print("Error detected")
                    quit()
        except NameError as e:
            print(f"You may have enetered the wrong data to find. {e}")

    def __str__(self):
        return self.name



#  current_plant = self.active_map[rows][cols]
#                 planet = questionary.select("View Plant: ", choices=["name", "type", "description"]).ask()
#                 current_plant.print_data(planet)


# class Garden():
#     def __init__(self, name_for_garden:str, garden:list):
#         self.name_garden = name_for_garden
#         self.garden = garden
#         self.garden_data = None

#     def generate_garden(self):
#         self.garden_data = {"location_name": self.name_garden,"maps": self.garden}
#         return self.garden_data

# carrot = Plant("Carrot", "Vegetable", "Very yummy and commonly associated with rabbits")
# lily = Plant("Lily", "Flower", "Very beautiful and refreshing to look at")
# tulip = Plant("Tulip", "Flower", "Very beautiful to look at and very calming to the mind")
# tomoto = Plant("Tomoto", "Vegetable", "Sour and yummy to eat")
# apple = Plant("Apple", "fruit", "A tech company. Recently did WWDC 26")

# garden1 = Garden("I love me", [[carrot, carrot, carrot],[lily, tulip, carrot],[apple, lily, tomoto]])
# # garden1.generate_garden