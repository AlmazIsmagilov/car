from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def car_desc(self):
        pass


class ElectricCar(Car):
    def car_desc(self):
        return "Electric car class"


class PetrolCar(Car):
    def car_desc(self):
        return "Petrol car class"


class HybridCar(Car):
    def car_desc(self):
        return "Hybrid car class"


class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass


class ElectricCarFactory(CarFactory):
    def create_car(self):
        return ElectricCar()


class PetrolCarFactory(CarFactory):
    def create_car(self):
        return PetrolCar()


class HybridCarFactory(CarFactory):
    def create_car(self):
        return HybridCar()


def create_car(factory: CarFactory):
    car = factory.create_car()
    print(car.car_desc())


electric_factory = ElectricCarFactory()
petrol_factory = PetrolCarFactory()
hybrid_factory = HybridCarFactory()

create_car(electric_factory)
create_car(petrol_factory)
create_car(hybrid_factory)