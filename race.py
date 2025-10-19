import json
from sim import *
with open("F1_Drivers.json", "r") as file:
    drivers = json.load(file)

with open("Manufactuers.json", "r") as file:
    manufacturers = json.load(file)

racedrivers = []

singapore = Track("Singapore", 4.9, 19, 98, 1)


class takeinput:
    def __init__(self):
        self.done = False
        while self.done == False:
            try:
                self.takedriverinput()
                self.done = True
            except:
                print("Wrong input")


        for i in range(self.number):
            self.chosedriver()

        sim = racing(racedrivers, singapore, 20)




    def takedriverinput(self):
        self.number = int(input("Enter the number of drivers: "))

    def chosedriver(self):
        done = False
        while done == False:
            try:
                driver = str(input("Enter the driver name: "))
                if driver in drivers:
                    self.choosemanufacturer()
                    racedrivers.append(Driver(driver, drivers[driver]["skill"], drivers[driver]["aggression"], drivers[driver]["consistency"], self.man, drivers[driver]["fuel_usage"]))
                    done = True
                else:
                    print("Wrong input")

            except:
                print("Wrong input")



    def choosemanufacturer(self):
        done = False
        while done == False:
            try:
                self.manufacturer = str(input("Enter the manufacturer name: "))
                if self.manufacturer in manufacturers:
                    self.man = Manufacturer(self.manufacturer, manufacturers[self.manufacturer]["ability"], manufacturers[self.manufacturer]["top_speed"],
                                       manufacturers[self.manufacturer]["cornering_ability"], manufacturers[self.manufacturer]["straights_ability"],
                                       manufacturers[self.manufacturer]["sponsor"], manufacturers[self.manufacturer]["pitstops_ability"])
                    done = True
                else:
                    print("Wrong input")

            except:
                print("Wrong input ")


inp = takeinput()
