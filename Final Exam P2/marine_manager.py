# -----------------------------------------------------------------------------
# Created By: Allen
# Created Date: 05/19/2026
# Version 1.0 (Fully working)
# -----------------------------------------------------------------------------
"""
A code to make the names for the sea creatures and put them into a report.
"""
# -----------------------------------------------------------------------------
class marineVessel():
    def __init__(self, name:str, speed:int, x:int, 
                 y:int, tracking:list):
        self.name = name
        self.speed = speed #km/h
        self.x = x
        self.y = y
        self.tracking = tracking


class seaCreature():
    def __init__(self, name:str, tag_number:str, 
                 x:int, y:int):
        self.name = name
        self.tag_number = tag_number
        self.x = x
        self.y = y

    def __str__(self):
        return self.name

orca = seaCreature("Orca", "10BDOF5", 250, 250)
blue_whale = seaCreature("Blue Whale", "20A7SB5", 100, 100)
pacific_dolphin = seaCreature("Pacific Dolphin", "30A82A6V", 800, 800)
humpback_whale = seaCreature("Humpback Whale", "5OK90A2D", 700, 700)
sea_turtle = seaCreature("TURT", "THISISATRUTLE", 50, 50)

marine_tracker = marineVessel("Marine Tracker", 25, 0, 0, 
                              [blue_whale, pacific_dolphin, orca])
ocean_explorer = marineVessel("Ocean Explorer", 20, 100, 100, 
                              [blue_whale, pacific_dolphin, sea_turtle])
deep_current = marineVessel("Deep Crrent", 18, 400, 400, 
                            [blue_whale, humpback_whale, sea_turtle])

class reportMaker():
    def __init__(self):
        pass

    def get_data(self, input):
        name = input.name
        speed = input.speed
        coordinates = (input.x, input.y)
        for _ in input.tracking:
            distance = pow((((_.x - input.x) ** 2) + 
                            ((_.y - input.y) ** 2)),(1/2))
            print(f"Name: {_}\n Location: "
                  f"({_.x}, {_.y})\n Tag: {_.tag_number}")
            print(f"Distance from {name} to {_}: {distance} km")
            print(name)
            print(speed)
            print(coordinates)
    
    def load_report(self, report_name:str, input, make_name):
        try:
            with open(report_name, "r") as file:
                full_text = file.read()
            full_text = full_text.replace("_V_E_S_S_E_L_1_", input.name)
            full_text = full_text.replace("_S_P_E_E_D_1_", 
                                          f"{input.speed} km/h")
            for i in range(3):
                full_text = full_text.replace(f"_C_R_E_A_T_U_R_E_{i}_", 
                                            str(input.tracking[i]))
                full_text = full_text.replace(f"_D_S_T_A_N_C_E_{i}_", 
                            str(pow((((input.x - input.tracking[i].x) ** 2) + 
                            ((input.y - input.tracking[i].y) ** 2)),(1/2))))
                full_text = full_text.replace(f"_T_I_M_E_{i}_", 
                        str((pow((((input.x - input.tracking[i].x) ** 2) 
                                + ((input.y - input.tracking[i].y) ** 2)),
                                (1/2))/input.speed)*60))
            # print(input.tracking)
            print(full_text)
            report_name = make_name
            with open(report_name + ".txt", "a") as _:
                _.write(full_text)
        except:
            print("ERROR")
            quit()

report1 = reportMaker()
report1.load_report("marine_report.txt", marine_tracker, "Report#1")
report1.load_report("marine_report.txt", deep_current, "Report#1")
report1.load_report("marine_report.txt", ocean_explorer, "Report#1")