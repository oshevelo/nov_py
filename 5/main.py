class Furniture:
    def __init__(self, material=None, size=None, color=None, location=None):
        self.material = material
        self.size = size
        self.color = color
        self.location = location


class Table(Furniture):
    def __init__(self, material=None, size=None, color=None, location=None, form=None, content=None):
        super().__init__(material, size, color, location)
        self.form = form
        self.content = content

    def move(self, new_location):
        self.location = new_location

    def set(self, new_content):
        self.content = new_content


class Chair(Furniture):
    def __init__(self, material=None, size=None, color=None, location=None, form=None, back=None, taken=False):
        super().__init__(material, size, color, location)
        self.form = form
        self.back = back
        self.taken = taken

    def move(self, new_location):
        self.location = new_location

    def sit(self):
        self.taken = True


class Cupboard(Furniture):
    def __init__(self, material=None, size=None, color=None, location=None, content=None, shelves=None):
        super().__init__(material, size, color, location)
        self.content = content
        self.shelves = shelves

    def open(self):
        pass

    def close(self):
        pass


class Device:
    def __init__(self, material=None, size=None, color=None, power=None, content=None, power_status=None):
        self.material = material
        self.size = size
        self.color = color
        self.power = power
        self.content = content
        self.power_status = power_status

    def on(self):
        self.power_status = 'On'

    def off(self):
        self.power_status = 'Off'


class Oven(Device):
    status = None

    def start(self):
        self.status = 'Working'

    def stop(self):
        self.status = 'Not working'


class Microwave(Oven):
    mode = None

    @property
    def time_left(self):
        some_time = 42
        return some_time

    def pause(self):
        self.status = 'Paused'

    def change_mode(self, mode):
        self.mode = mode

    def open(self):
        pass

    def close(self):
        pass


class SimpleOven(Oven):
    max_temperature = None
    mode = None

    def change_mode(self, mode):
        self.mode = mode

    def open(self):
        pass

    def close(self):
        pass


class Hob(Oven):
    zones = None
    max_temperature = None

    def change_zone_temperature(self, zone, temperature):
        pass

    def start(self, zone):
        self.status[zone] = 'Working'

    def stop(self, zone):
        self.status[zone] = 'Not working'


class ElectricGrill(Oven):
    mode = None

    def change_mode(self, mode):
        self.mode = mode

    def open(self):
        pass

    def close(self):
        pass


class Dishwasher(Device):
    mode = None
    status = None

    def change_mode(self, mode):
        self.mode = mode

    def start(self):
        self.status = 'Working'

    def stop(self):
        self.status = 'Not working'

    def pause(self):
        self.status = 'Paused'

    def open(self):
        pass

    def close(self):
        pass


class Fridge(Device):
    temperature = None
    mode = None

    def change_mode(self, mode):
        self.mode = mode

    def open(self):
        pass

    def close(self):
        pass


class Freezer(Device):
    temperature = None
    mode = None

    def change_mode(self, mode):
        self.mode = mode

    def open(self):
        pass

    def close(self):
        pass

