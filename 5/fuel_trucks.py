class Vehicle:
    def __init__(self, wheels, speed):
        self.wheels = wheels
        self.speed = speed

    def move(self):
        pass


class Tank:
    def __init__(self, capacity):
        self.capacity = capacity

    def fuel_fill_up(self):
        pass

    def fuel_distribute(self):
        pass


class Auto(Vehicle):
    def start_engine(self):
        pass


class Trailer(Vehicle):
    pass


class Car(Auto):
    pass


class Truck(Auto):
    pass


class TankTrailer(Tank, Trailer):
    pass


class FuelTruck(Tank, Truck):
    pass


class FuelTruckTrailer(Truck, TankTrailer):
    pass
