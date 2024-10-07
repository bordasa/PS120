class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(Vehicle):

    def __init__(self, year):
        super().__init__(year)
        self.start_engine()

    def start_engine(self):
        print('Ready to go!')

class Car(Vehicle):
    pass


# Comments show expected output
truck1 = Truck(1994)
print(truck1.year)            # 1994

# car1 = Car(2006)
# print(car1.year)              # 2006