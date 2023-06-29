from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel <= 0:
                raise LowFuelError('Закончилось топливо')
            self.started = True

    def move(self, distance):
        required_fuel = self.fuel_consumption * distance
        if required_fuel > self.fuel:
            raise NotEnoughFuel()
        self.fuel -= required_fuel
