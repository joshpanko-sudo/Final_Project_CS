# from tabulate import tabulate

class marineVessel():
    def __init__(self, name:str, speed:int, x:int, y:int, tracking:list):
        self.name = name
        self.speed = speed #km/h
        self.x = x
        self.y = y
        self.tracking = tracking

    def tracking_description(self):
        # print(self.tracking)
        for _ in self.tracking:
            print(_)


class seaCreature():
    def __init__(self, name:str, tag_number:str, x:int, y:int):
        self.name = name
        self.tag_number = tag_number
        self.x = x
        self.y = y

    def __str__(self):
        return self.name


class generateReport():
    def __init__(self):
        pass

    def load_report(self, report_name:str):
        with open(report_name, "r") as file:
            full_text = file.read()
        
        full_text = full_text.replace("")





orca = seaCreature("Orca", "10BDOF5", 250, 250)
blue_whale = seaCreature("Blue Whale", "20A7SB5", 100, 100)
pacific_dolphin = seaCreature("Pacific Dolphin", "30A82A6V", 800, 800)
humpback_whale = seaCreature("Humpback Whale", "5OK90A2D", 700, 700)
sea_turtle = seaCreature("TURT", "THISISATRUTLE", 50, 50)
# print(orca)

marine_tracker = marineVessel("Marine Tracker", 25, 0, 0, [blue_whale, pacific_dolphin, orca])
ocean_explorer = marineVessel("Ocean Explorer", 20, 100, 100, [blue_whale, pacific_dolphin, sea_turtle])
deep_current = marineVessel("Deep Crrent", 18, 400, 400, [blue_whale, humpback_whale, sea_turtle])
marine_tracker.tracking_description()
