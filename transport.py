class Transport:
    
    def __init__(self, passangers_num=None, speed=None):
        self.passangers_num = passangers_num
        self.speed = speed

    def count_trip_time(self, km=None):
        trip_time = km / self.speed
        print(f'Trip for {km} will take {trip_time} hours.')
        return trip_time

    def move(self):
        print(f'Transport is moving with speed {self.speed} km/h.')

    @property
    def get_speed(self):
        return self.speed

    @property
    def get_passangers_num(self):
        return self.passangers_num

    def __str__(self):
        return f'Transport with {self.passangers_num} passengers and {self.speed} km/h speeed.'

    
class AirTransport(Transport):
    
    def __init__(self, passangers_num=None, speed=None, max_height=None):
        super().__init__(passangers_num, speed)
        self.max_height = max_height

    def move(self):
        print(f'Aircraft is flying with speed {self.speed} km/h.')

    @property
    def get_max_height(self):
        return self.max_height

    def __str__(self):
        return f'Aircraft with {self.passangers_num} passengers and {self.speed} km/h speeed.'

    
class Helicopter(AirTransport):

    def hang_in_air(self):
        print('Helicopter is hanging in the air.')

    def __str__(self):
        return f'Helicopter with {self.passangers_num} passengers and {self.speed} km/h speeed.'

    
class Airplane(AirTransport):
    
    def __init__(self, passangers_num=None, speed=None, max_height=None):
        super().__init__(passangers_num, speed, max_height)
        self.chassis_status = None

    def change_status(self):
        if self.chassis_status:
            self.chassis_status = None
            print('Chassis off.')
        else:
            self.chassis_status = True
            print('Chassis on.')

    @property
    def get_chassis_status(self):
        return self.chassis_status

    def __str__(self):
        return f'Helicopter with propeller mode = {self.chassis_status}.'

    
class WaterTransport(Transport):
    
    def __init__(self, passangers_num=None, speed=None, max_dist_from_coast=None):
        super().__init__(passangers_num, speed)
        self.max_dist_from_coast = max_dist_from_coast

    def move(self):
        print(f'Watercraft is swimming with speed {self.speed} km/h.')

    @property
    def get_max_dist_from_coast(self):
        return self.max_dist_from_coast

    def __str__(self):
        return f'A watercraft with {self.passangers_num} passengers and {self.speed} km/h speeed.'

    
class Submarine(WaterTransport):
    
    def __init__(self, passangers_num=None, speed=None, max_dist_from_coast=None, max_depth=None):
        super().__init__(passangers_num, speed, max_dist_from_coast)
        self.max_depth = max_depth
        self.current_depth = 0

    def dive(self, metres):
        if (self.current_depth + metres) <= self.max_depth:
            self.current_depth += metres
            print(f'Now submarine is on depth = {self.current_depth} metres.')
        else:
            print(f'Cannot dive so deep, max depth = {self.max_depth}')

    @property
    def get_current_depth(self):
        return self.current_depth

    @property
    def get_max_depth(self):
        return self.max_depth

    def __str__(self):
        return f'Submarine on depth = {self.current_depth} metres, while max depth = {self.max_depth}.'

    
class OilTanker(WaterTransport):
    
    def __init__(self, passangers_num=None, speed=None, max_dist_from_coast=None, max_oil_amount=None):
        super().__init__(passangers_num, speed, max_dist_from_coast)
        self.max_oil_amount = max_oil_amount

    @property
    def get_max_oil_amount(self):
        return self.max_oil_amount

    def __str__(self):
        return f'Oil tanker with maximum possible oil amount = {self.max_oil_amount}.'

    
class SailingYacht(WaterTransport):
    
    def __init__(self, passangers_num=None, speed=None, max_dist_from_coast=None):
        super().__init__(passangers_num, speed, max_dist_from_coast)
        self.sails_status = None

    def change_status(self):
        if self.sails_status:
            self.sails_status = None
            print('Closing sails.')
        else:
            self.sails_status = True
            print('Opening sails.')

    @property
    def get_sails_status(self):
        return self.sails_status

    def __str__(self):
        return f'Sailing yacht with sails mode = {self.sails_status}.'

    
class LandTransport(Transport):

    def move(self):
        print(f'Landcraft is driving with speed {self.speed} km/h.')

    def __str__(self):
        return f'Landcraft with {self.passangers_num} passengers and {self.speed} km/h speeed.'

    
class Train(LandTransport):
    
    def __init__(self, passangers_num=None, speed=None, carriages_num=None):
        super().__init__(passangers_num, speed)
        self.carriages_num = carriages_num

    @property
    def get_carriages_num(self):
        return self.carriages_num

    def __str__(self):
        return f'Train with {self.carriages_num} carriages.'

    
class Truck(LandTransport):
    
    def __init__(self, passangers_num=None, speed=None, max_load_kg=None):
        super().__init__(passangers_num, speed)
        self.max_load_kg = max_load_kg
        self.current_kg = 0

    def load_up(self, kg):
        if (self.current_kg + kg) <= self.max_load_kg:
            self.current_kg += kg
            print(f'Now truck is loaded for {self.current_kg} kg. You can load {self.max_load_kg-self.current_kg} kg more.')
        else:
            print('Cannot load such weight.')

    @property
    def get_max_load_kg(self):
        return self.max_load_kg

    def __str__(self):
        return f'Truck with {self.current_kg} kg, while maximum load kg = {self.max_load_kg}.'

