class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, new_width):
        if not isinstance(new_width, (int, float)):
            raise ValueError("Width must be an integer or float.")
        
        self._width = new_width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, new_height):
        if not isinstance(new_height, (int, float)):
            raise ValueError("Width must be an integer or float.")
        
        self._height = new_height
    
    @property
    def area(self):
        return self.width * self.height

rect = Rectangle(4, 5)

print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True