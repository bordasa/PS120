class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

square = Square(5)
print(square.area == 25)      # True