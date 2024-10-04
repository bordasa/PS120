class Cat:

    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError('Name must be a string.')
        
        self._name = new_name.title()
    
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        if not isinstance(new_color, str):
            raise ValueError('Color must be a string.')

        self._color = new_color.casefold()

    def greet(self):
        print(f"Hello! My name is {self.name} and I'm a {self.color} cat!")

sophie = Cat('Sophie', 'purple')
sophie.greet()