import random


def get_random_direction():

    if random.randint(0, 1) == 0:
        direction = "North"
    else:
        direction = "West"
    return direction


class Vehicle:

    def __init__(self):
        self.direction = get_random_direction()

    def get_direction(self):
        return self.direction


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.time_cost = 2

    def get_time_cost(self):
        return self.time_cost


class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.time_cost = 5

    def get_time_cost(self):
        return self.time_cost


c = Car()
print(type(c.get_time_cost()))