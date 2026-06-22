# from tabulate import tabulate

class marineVessel():
    def __init__(self, name:str, speed:int, x:int, y:int, tracking:list):
        self.name = name
        self.speed = speed #km/h
        self.x = x
        self.y = y
        self.tracking = tracking

    def tracking_description(self, details:str):
        # print(self.tracking)
        match details:
            case "Tracking0":
                return self.tracking[0]
                # for _ in self.tracking:
                #     print(_)
                #     return _
            case "Tracking1":
                return self.tracking[1]
            case "Tracking2":
                return self.tracking[2]
            case "Speed":
                print(self.speed)
                return self.speed
            case "Name":
                print(self.name)
                return self.name
            case "x":
                return self.x
            case "y":
                return self.y


class seaCreature():
    def __init__(self, name:str, tag_number:str, x:int, y:int):
        self.name = name
        self.tag_number = tag_number
        self.x = x
        self.y = y

    def __str__(self):
        return self.name
    
    def details(self, details_to_use):
        match details_to_use:
            case "x":
                return self.x
            case "y":
                return self.y



class get_distances_times():
    def __init__(self, sea_creature_x, sea_creature_y, vessel_x, vessel_y):
        self.sea_creature_x = sea_creature_x
        self.sea_creature_y = sea_creature_y
        self.vessel_x = vessel_x
        self.vessel_y = vessel_y

    def calculate(self):
        distance = pow(((self.sea_creature_x - self.vessel_x) ** 2) + ((self.sea_creature_y - self.vessel_y) ** 2), (1/2))
        return distance


# marine_tracker = marineVessel("Marine Tracker", 25, 0, 0, [blue_whale, pacific_dolphin, orca])
    # def solve_for_distance(self):


    
        

class generateReport():
    def __init__(self, name, speed, creature_index:list, distance_index:list):
        self.vessel_name = name
        self.vessel_speed = speed
        self.creature_index = creature_index
        self.distance_index = distance_index

    def load_report(self, report_name:str):
        with open(report_name, "r") as file:
            full_text = file.read()
        
        full_text = full_text.replace("_V_E_S_S_E_L_1_", self.vessel_name)
        full_text = full_text.replace("_S_P_E_E_D_1_", str(self.vessel_speed) + " km\h")
        full_text = full_text.replace("_C_R_E_A_T_U_R_E_1_", str(self.creature_index[0]))
        full_text = full_text.replace("_C_R_E_A_T_U_R_E_2_", str(self.creature_index[1]))
        full_text = full_text.replace("_C_R_E_A_T_U_R_E_3_", str(self.creature_index[2]))
        full_text = full_text.replace("_D_I_S_T_A_N_C_E_1_", str(self.distance_index[0]))
        print(full_text)
        report_name = input("Title your report: ")
        with open(report_name + ".txt", "w") as _:
            _.write(full_text)





orca = seaCreature("Orca", "10BDOF5", 250, 250)
blue_whale = seaCreature("Blue Whale", "20A7SB5", 100, 100)
pacific_dolphin = seaCreature("Pacific Dolphin", "30A82A6V", 800, 800)
humpback_whale = seaCreature("Humpback Whale", "5OK90A2D", 700, 700)
sea_turtle = seaCreature("TURT", "THISISATRUTLE", 50, 50)
# print(orca)

marine_tracker = marineVessel("Marine Tracker", 25, 0, 0, [blue_whale, pacific_dolphin, orca])
ocean_explorer = marineVessel("Ocean Explorer", 20, 100, 100, [blue_whale, pacific_dolphin, sea_turtle])
deep_current = marineVessel("Deep Crrent", 18, 400, 400, [blue_whale, humpback_whale, sea_turtle])
# marine_tracker.tracking_description()

# for i in range(3):
    # get_distances_times(orca.details("x"), marine_tracker.tracking_description("x"), orca.details("y"), marine_tracker.tracking_description("y"))

marine_database = generateReport(marine_tracker.tracking_description("Name"), marine_tracker.tracking_description("Speed"), [blue_whale, pacific_dolphin, orca], [get_distances_times(orca.details("x"), marine_tracker.tracking_description("x"), orca.details("y"), marine_tracker.tracking_description("y"))])
marine_database.load_report("marine_report.txt")
