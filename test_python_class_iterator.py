from __future__ import print_function

class IterableCar(type):
    def __iter__(cls):
        return iter(cls._registry)

class Car(metaclass=IterableCar):
    _registry = []

    def __init__(self, name):
        self._registry.append(self)
        self.name = name


if __name__=='__main__':

    car1 = Car('Mercedes')
    car2 = Car('Toyota')
    for cars in Car:
        print (cars.name)