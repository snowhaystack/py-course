from abc import abstractmethod, ABC


class Transport(ABC):
    @abstractmethod
    def start(self):
        ...

    @abstractmethod
    def stop(self):
        ...


class Vehicle(Transport):
    tank = 0
    __oil_viscosity = 0
    garage = 0

    @classmethod
    def battery_charge(cls):
        print(id(cls))

    @classmethod
    def add_garage(cls):
        cls.garage += 1

    def __init__(self, tire_num):
        self.tires = [Tire(2.5, 17) for i in range(0, tire_num)]
        # print("init class " + str(self.__class__))
        self.tire_num = tire_num
        self.add_garage()

    def start(self):
        print(id(self))

    def stop(self):
        print('Stop')

    def __del__(self):
        # print("delete class " + str(self.__class__))
        pass

    def __add__(self, other):
        new = Vehicle(self.tire_num + other.tire_num)
        return new

    def __str__(self) -> str:
        return f'Vehicle with {self.tire_num} tires'


class Tire:
    def __init__(self, pressure: float, diameter: int) -> None:
        self.pressure = pressure
        self.diameter = diameter

    def __str__(self) -> str:
        return f'Tier pressure is {self.pressure}\n'


class Truck(Vehicle):
    def __init__(self):
        super().__init__(10)

    def __str__(self) -> str:
        return f'Truck with {self.tire_num} tires'


scooter = Vehicle(2)
car = Vehicle(4)
car.tank = '100'
print(scooter.tank)  # 0
print(car.tank)  # 100
Vehicle.tank = 10
print(scooter.tank)  # 10
print(car.tank)  # 100 not 10 => assigned before


hybrid = scooter + car
print(hybrid.tire_num)
iveco = Truck()
iveco1 = Truck()
print(iveco)
print(*iveco.tires)
print(Truck.__mro__)  # resolution object
print(Vehicle.garage)
print(Truck.garage)

# Rich py
