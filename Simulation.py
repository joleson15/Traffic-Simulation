from Queue import Queue
import random
import Vehicle
from Vehicle import Car, Truck


class Simulation(object):
    north = Queue()
    west = Queue()

    def populate_north(self):
        if random.randint(0, 9) == 0:
            self.north.enqueue(Car())

    def populate_west(self):
        if random.randint(0, 20) == 0:
            self.west.enqueue(Car())

    def process_north(self):
        for i in range(5):
            if not (self.north.is_empty()):
                c = self.north.dequeue()
                i += c.get_time_cost()
            i += 1


    def simulate(self):
        time = 0
        light = "green"
        while time < 3600:
            self.populate_north()
            self.populate_west()
            if time % 10 == 0:
                if light == "green":
                    light = "red"
                else:
                    light = "green"
            if light == "green":
                self.north.dequeue()

            time += 1


s = Simulation()
s.north.enqueue(Car())
s.north.enqueue(Car())
s.north.enqueue(Car())
s.north.enqueue(Car())
s.north.enqueue(Car())
s.north.enqueue(Car())
s.north.enqueue(Car())
s.north.enqueue(Car())
s.north.enqueue(Car())
s.north.enqueue(Car())
print(s.north.size())

s.process_north()
print(s.north.size())