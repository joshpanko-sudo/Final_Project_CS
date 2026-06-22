class marineManager():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class marineVessel():
    def __init__(self, name:str, speed:int, x:int, y:int, tracking:list):
        self.name = name
        self.speed = speed #km/h
        self.x = x
        self.y = y
        self.tracking = tracking

class seaCreature():
    def __init__(self, name:str, tag_number:str, x:int, y:int):
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

marine_tracker = marineVessel("Marine Tracker", 25, 0, 0, [blue_whale, pacific_dolphin, orca])


def get_data(input):
    name = input.name
    speed = input.speed
    coordinates = (input.x, input.y)
    for _ in input.tracking:
        distance = pow((((_.x - input.x) ** 2) + ((_.y - input.y) ** 2)),(1/2))
        print(f"Name: {_}\n Location: ({_.x}, {_.y})\n Tag: {_.tag_number}")
        print(f"Distance from {name} to {_}: {distance} km")

    
    print(name)
    print(speed)
    print(coordinates)
    # print(tracking)


get_data(marine_tracker)