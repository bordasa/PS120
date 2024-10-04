# #Problem 1:

# class Person:
#     def __init__(self, name):
#         self._name = name
    
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, name):
#         if not isinstance(name, str):
#             raise TypeError('Name must be a string')
        
#         self._name = name

# bob = Person('bob')
# print(bob.name)           # bob
# bob.name = 'Robert'
# print(bob.name)           # Robert

#Problem 2:

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str):
            raise TypeError('Name must be a string.')
        
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if not isinstance(last_name, str):
            raise TypeError('Name must be a string.')
        
        self._last_name = last_name

    @property
    def name(self):
        if not self._last_name:
            return self._first_name
        
        return self._first_name + ' ' + self._last_name

    # def __repr__(self, name_part):
    #     return self.name_part
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        
        name_parts = name.split()
        self.first_name = name_parts[0]
        self.last_name = ''
        
        if len(name_parts) > 1:
            self._first_name = name_parts[0]
            self._last_name = ' '.join(name_parts[1:])
            

# bob = Person('Robert')
# print(bob.name)             # Robert
# print(bob.first_name)       # Robert
# print(repr(bob.last_name))  # ''
# bob.last_name = 'Smith'
# print()
# print(bob.name)             # Robert Smith
# print()
# bob.name = 'Prince'
# print()
# print(bob.first_name)       # Prince
# print(repr(bob.last_name))  # ''
# print()
# bob.name = 'John Adams'
# print()
# print(bob.first_name)       # John
# print(bob.last_name)        # Adams

bob = Person('Robert Smith')
rob = Person('Robert Smith')

print(bob.name == rob.name)