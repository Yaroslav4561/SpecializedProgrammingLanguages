class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        print(f"Car engine started")

class Motorcycle(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

    def start_engine(self):
        print(f"Motorcycle engine started")

class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def charge_battery(self):
        print("Battery charging")

class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.vehicles.append(vehicle)

    def start_all_engines(self):
        for vehicle in self.vehicles:
            vehicle.start_engine()


car1 = Car("Toyota", "Corolla")
motorcycle1 = Motorcycle("Yamaha", "Sport")
electric_car1 = ElectricCar("Tesla", "Model S")

garage = Garage()
garage.add_vehicle(car1)
garage.add_vehicle(motorcycle1)
garage.add_vehicle(electric_car1)

garage.start_all_engines()

electric_car1.charge_battery()
