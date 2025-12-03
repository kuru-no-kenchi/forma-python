from abc import ABC, abstractmethod


# ------------------------------------------------------------
# Stage 1 – Base Class: Vehicle (Abstract)
# ------------------------------------------------------------

class Vehicle(ABC):
    def __init__(self, brand, model, year, base_price):
        self.brand = brand
        self.model = model
        self.year = year
        self.base_price = base_price

    def describe(self):
        return f"{self.__class__.__name__} - {self.brand} {self.model} ({self.year})"

    @abstractmethod
    def compute_value(self):
        pass

    @abstractmethod
    def maintenance_cost(self):
        pass


# ------------------------------------------------------------
# Stage 2 – Car, Motorcycle, Truck
# Depreciation logic:
#   Car: 5% per year
#   Motorcycle: 7% per year
#   Truck: 3% per year
# ------------------------------------------------------------

class Car(Vehicle):
    def compute_value(self):
        age = 2025 - self.year
        return max(0, self.base_price * ((1 - 0.05) ** age))

    def maintenance_cost(self):
        return 2000   # simple fixed estimate


class Motorcycle(Vehicle):
    def compute_value(self):
        age = 2025 - self.year
        return max(0, self.base_price * ((1 - 0.07) ** age))

    def maintenance_cost(self):
        return 1000


class Truck(Vehicle):
    def compute_value(self):
        age = 2025 - self.year
        return max(0, self.base_price * ((1 - 0.03) ** age))

    def maintenance_cost(self):
        return 3000


# ------------------------------------------------------------
# Stage 3 – Polymorphism: total fleet value
# ------------------------------------------------------------

def calculate_total_fleet_value(fleet_list):
    total = 0
    for v in fleet_list:
        total += v.compute_value()
    return total


# ------------------------------------------------------------
# Stage 4 – Advanced: ElectricCar subclass
# Depreciation: normal car depreciation + battery factor
# ------------------------------------------------------------

class ElectricCar(Car):
    def __init__(self, brand, model, year, base_price, battery_health):
        super().__init__(brand, model, year, base_price)
        self.battery_health = battery_health    # from 0 to 100

    def compute_value(self):
        base_value = super().compute_value()
        battery_factor = self.battery_health / 100
        return base_value * battery_factor

    def maintenance_cost(self):
        return 1500   # EV maintenance is lower


# ------------------------------------------------------------
# Stage 5 – Optional Extension: FleetManager
# ------------------------------------------------------------

class FleetManager:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        if vehicle in self.vehicles:
            self.vehicles.remove(vehicle)

    def list_fleet(self):
        for v in self.vehicles:
            print(v.describe())

    def search(self, brand):
        return [v for v in self.vehicles if v.brand.lower() == brand.lower()]

    def total_value(self):
        return calculate_total_fleet_value(self.vehicles)


# ------------------------------------------------------------
# Test Code
# ------------------------------------------------------------

if __name__ == "__main__":
    # Vehicles
    car1 = Car("Toyota", "Corolla", 2020, 150000)
    moto1 = Motorcycle("Yamaha", "R3", 2022, 70000)
    truck1 = Truck("Volvo", "FH16", 2018, 500000)
    ev1 = ElectricCar("Tesla", "Model 3", 2021, 300000, battery_health=85)

    # Fleet manager
    fm = FleetManager()
    fm.add_vehicle(car1)
    fm.add_vehicle(moto1)
    fm.add_vehicle(truck1)
    fm.add_vehicle(ev1)

    print("Fleet list:")
    fm.list_fleet()

    print("\nTotal fleet value:", fm.total_value())

    print("\nSearch for 'Tesla':")
    for v in fm.search("Tesla"):
        print(v.describe())

    print("\nMaintenance costs:")
    for v in fm.vehicles:
        print(v.describe(), "->", v.maintenance_cost())
