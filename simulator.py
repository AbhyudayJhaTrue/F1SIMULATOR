import random
from dataclasses import dataclass
from prettytable import PrettyTable


@dataclass
class Driver:
    name : str
    skill : int
    aggression : float
    consistency : float
    manufacturer: str

    car_fuel_usage: int

    laps_completed : int = 0
    total_time : float  = 0.0
    pitstops : int = 0
    tyre_wear : int = 0

    car_fuel : int = 0

    in_race: bool = True


@dataclass
class Manufacturer:
    name : str
    car_ability : int
    car_topspeed : int
    cornering_ability : float
    striaghts_ability : float
    sponsor : str
    pitstops_ability : float

@dataclass
class Track:
    name: str
    length : float
    corners : int
    baselap : int
    altitude_effect : float


class racing:

    def __init__(self, drivers, track, laps):
        self.track = track
        self.drivers = drivers
        self.laps = laps
        self.finaltimes = {}
        self.dnf = {}

        for d in self.drivers:
            d.car_fuel = 75

        for lap in range(laps):
            self.lap()

        print(f"RACE WEEKEND!\nTrack: {self.track.name}")

        for d in self.drivers:
            if d.in_race:
                self.finaltimes[d.name] = d.total_time
            else:
                self.dnf[d.name] = d.laps_completed

        self.finaltimes = dict(sorted(self.finaltimes.items(), key=lambda x: x[1]))

        table = PrettyTable(["Driver", "Total Time", "Average Time Per Lap", "Laps Completed", "Pitstops", "Manufacturer", "Sponsor"])

        for key in self.finaltimes:
            d = next(driver for driver in self.drivers if driver.name == key)
            avlap = d.total_time/d.laps_completed
            table.add_row([d.name, round(d.total_time, 3), round(avlap,3), d.laps_completed, d.pitstops, d.manufacturer.name, d.manufacturer.sponsor])

        for key in self.dnf:
            d = next(driver for driver in self.drivers if driver.name == key)
            table.add_row([d.name, "DNF", "N/A", d.laps_completed, d.pitstops, d.manufacturer.name,d.manufacturer.sponsor])

        print(table)




    def lap(self):
        for d in self.drivers:
            manufacturer = d.manufacturer
            if d.in_race:
                d.laps_completed += 1
                lap_time = (
                        self.track.baselap * self.track.altitude_effect
                        - (
                                (d.skill * 0.005)
                                + (d.aggression * 0.02)
                                + (d.consistency * 0.01)
                                + (manufacturer.car_ability * 0.01)
                                + (manufacturer.cornering_ability * (0.004 + 0.0002 * self.track.corners))
                                + (manufacturer.striaghts_ability * 0.003)
                                + (manufacturer.car_topspeed * 0.002)
                        )
                        + (d.car_fuel_usage * 0.08)
                        + (d.tyre_wear * 0.05)
                )

                lap_time = round(lap_time, 3)

                if random.uniform(0, 4) < 0.3:
                    d.tyre_wear += 5.5
                else:
                    d.tyre_wear += 3.5

                if random.uniform(0, 15) <= 0.1:
                    d.in_race = False

                d.car_fuel -= d.car_fuel_usage

                if d.tyre_wear >=100:
                    d.tyre_wear = 0
                    lap_time += 2 - manufacturer.pitstops_ability
                    lap_time += 3 #time taken to exit pit lane
                    d.pitstops += 1

                elif d.car_fuel <= d.car_fuel_usage:
                    d.car_fuel = 90
                    d.pitstops += 1
                    lap_time += 2 - manufacturer.pitstops_ability
                    lap_time += 3  # time taken to exit pit lane

                d.total_time += lap_time

            else:
                pass

def makemanufacturer(name, ability, top_speed, ca, sa, sponsor, pa):
    return Manufacturer(name, ability, top_speed, ca, sa, sponsor, pa)

def makedriver(name, skill, agression, consistency, manufacturer, fuelusage):
    return Driver(name, skill, agression, consistency, manufacturer, fuelusage)
