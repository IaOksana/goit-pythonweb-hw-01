# Завдання 1. Патерн фабрика

# Наступний код представляє просту систему для створення транспортних засобів.
# У нас є два класи: Car та Motorcycle. Кожен клас має метод start_engine(), який імітує запуск двигуна відповідного транспортного засобу.
# Наразі, щоб створити новий транспортний засіб, ми просто створюємо екземпляр відповідного класу з вказаними маркою (make) та моделлю (model).

from abc import ABC, abstractmethod
import logging

# init logger
logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    handlers=[logging.FileHandler("task_1.log"), logging.StreamHandler()],
)


# 1. Створити абстрактний базовий клас Vehicle з методом start_engine()
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        raise NotImplementedError()

    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec


# 2. Змінити класи Car та Motorcycle, щоб вони успадковувались від Vehicle.
# logs translateted to Engl because my Ukrainian is not supported (
class Car(Vehicle):
    def start_engine(self):
        str = f"{self.make} {self.model} {self.spec}: Engine is run"
        logging.info(str)


class Motorcycle(Vehicle):
    def start_engine(self):
        str = f"{self.make} {self.model}{self.spec}: Engine is started"
        logging.info(str)


# 3. Створити абстрактний клас VehicleFactory з методами create_car() та create_motorcycle()
class VehicleFactory:
    @abstractmethod
    def create_car(self, make, model):
        raise NotImplementedError()

    @abstractmethod
    def create_motorcycle(self, make, model):
        raise NotImplementedError()


# 4. Реалізувати два класи фабрики: USVehicleFactory та EUVehicleFactory.
# Ці фабрики повинні створювати автомобілі та мотоцикли з позначкою регіону наприклад, Ford Mustang (US Spec) відповідно для США.
class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")


# Usage
types = ["auto", "moto"]


def create_vehicle(veh: VehicleFactory, make, model, spec: str):
    if spec == types[0]:
        return veh.create_car(make, model)
    elif spec == types[1]:
        return veh.create_motorcycle(make, model)


factory_US = USVehicleFactory()
factory_EU = EUVehicleFactory()


create_vehicle(factory_US, "Ford", "Car", types[0]).start_engine()
create_vehicle(factory_US, "Harley Devidson", "Moto", types[1]).start_engine()
create_vehicle(factory_EU, "Toyota", "Car", types[0]).start_engine()
create_vehicle(factory_EU, "EU Moto", "Moto", types[1]).start_engine()
