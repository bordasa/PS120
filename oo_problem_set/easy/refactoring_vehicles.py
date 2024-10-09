class Vehicle:
    def __init__(self, make, model, wheels):
        self._make = make
        self._model = model
        self._wheels = wheels

    @property
    def make(self):
        return self._make
    
    @property
    def model(self):
        return self._model
    
    @property
    def wheels(self):
        return self._wheels

    def get_wheels(self):
        return self.wheels
    
    def info(self):
        return f"{self.make} {self.model}"
    
class Car:
    def __init__(self, make, model):
        super().__init__(make, model, 4)

class Motorcycle:
    def __init__(self, make, model):
        super().__init__(make, model, 2)

class Truck:
    def __init__(self, make, model, payload):
        super().__init__(make, model, 6)
        self._payload = payload
    
    @property
    def payload(self):
        return self._paload