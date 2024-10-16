# # #Problem 1
# # """
# # __gt__
# # __mul__
# # __le__
# # __ne__
# # __iadd__
# # __ipow__ 
# # __floordiv__
# # """

# # #Problem 2
# # class Cat:
# #     def __init__(self, name):
# #         self.name = name

# #     def __eq__(self, other):
# #         if not isinstance(other, Cat):
# #             return NotImplemented
        
# #         return self.name.casefold() == other.name.casefold()
    
# #     def __ne__(self, other):
# #         if not isinstance(other, Cat):
# #             return NotImplemented
        
# #         return self.name.casefold() != other.name.casefold()
    
# #     def __lt__(self, other):
# #         if not isinstance(other, Cat):
# #             return NotImplemented
        
# #         return self.name.casefold() < other.name.casefold()
    
# #     def __le__(self, other):
# #         if not isinstance(other, Cat):
# #             return NotImplemented
        
# #         return self.name.casefold() <= other.name.casefold()
    
# #     def __gt__(self, other):
# #         if not isinstance(other, Cat):
# #             return NotImplemented
        
# #         return self.name.casefold() > other.name.casefold()
    
# #     def __ge__(self, other):
# #         if not isinstance(other, Cat):
# #             return not NotImplemented
        
# #         return self.name.casefold() >= other.name.casefold()
    


# # fluffy1 = Cat('Fluffy')
# # fluffy2 = Cat("FLUFFY")
# # buttercup = Cat("Buttercup")
# # print(fluffy1 == fluffy2)
# # print(fluffy1 != fluffy2)
# # print()
# # print(fluffy1 > fluffy2)
# # print(fluffy1 < fluffy2)
# # print(fluffy1 <= fluffy2)
# # print(fluffy1 >= fluffy2)
# # print()
# # print(buttercup == fluffy1)
# # print(buttercup != fluffy2)
# # print()
# # print(buttercup > fluffy1)
# # print(buttercup < fluffy1)
# # print(buttercup <= fluffy1)
# # print(buttercup >= fluffy1)

# #Problem 4
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
    
#     def __add__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented
        
#         return Vector(self.x + other.x, self.y + other.y)
    
#     def __iadd__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented
        
#         return Vector(self.x + other.x, self.y + other.y)

#     def __sub__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented
        
#         return Vector(self.x - other.x, self.y - other.y)
    
#     def __isub__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented
        
#         return Vector(self.x - other.x, self.y - other.y)
    
#     def __mul__(self, other):
#         if not isinstance(other, int):
#             return NotImplemented
        
#         return Vector(self.x * other, self.y * other)
    
#     def __imul__(self, other):
#         if not isinstance(other, int):
#             return NotImplemented
        
#         return Vector(self.x * other, self.y * other)
    
#     def __rmul__(self, other):
#         if not isinstance(other, int):
#             return NotImplemented
        
#         return Vector(self.x * other, self.y * other)
    
# print()
# print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
# print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
# print(Vector(5, 12) * 2)              # Vector(10, 24)
# print(3 * Vector(5, 12))              # Vector(15, 36)
# print()

# my_vector = Vector(5, 7)
# my_vector += Vector(3, 9)
# print(my_vector)                      # Vector(8, 16)
# print()

# my_vector -= Vector(1, 7)
# print(my_vector)                      # Vector(7, 9)
# print()

# print(Vector(3, 2) + 5)
# # TypeError: unsupported operand type(s) for +: 'Vector'
# # and 'int'

#Problem 5
class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'
    
    def _is_numeric(self, value):
        if isinstance(value, int):
            return True
        
        return value.isdigit()
    
    def __add__(self, other):
        if not isinstance(other, (int, str)):
            return NotImplemented
        
        both_numeric = (self._is_numeric(self.value) and 
                        self._is_numeric(other))
        
        if both_numeric:
            return Silly(int(self.value) + int(other))
        
        else:
            return Silly(str(self.value) + str(other))

    # def __add__(self, other):
    #     if not isinstance(other, [int, str]):
    #         return NotImplemented

    #     if isinstance(self.value, int):
    #         if isinstance(other, int) or other.isdigit():
    #             return self.value + int(other)
    #         else:
    #             return str(self.value) + str(other)

    #     elif self.value.isdigit():
    #         if isinstance(other, int) or other.isdigit():
    #             return int(self.value) + int(other)

    #     else:
    #         return str(self.value) + str(other)


print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)