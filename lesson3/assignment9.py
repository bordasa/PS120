# # # # #Problem 1
# # # # class Dog:
# # # #     def __init__(self, breed):
# # # #         self.breed = breed
    
# # # #     @property
# # # #     def breed(self):
# # # #         return self._breed
    
# # # #     @breed.setter
# # # #     def breed(self, breed):
# # # #         if not isinstance(breed, str):
# # # #             raise TypeError("Breed must be a string.")
        
# # # #         self._breed = breed

# # # # class Cat:

# # # #     def get_name(self):
# # # #         try:
# # # #             return self.name
# # # #         except AttributeError:
# # # #             return "Name not set!"

# # # # # cat1 = Cat()
# # # # # print(cat1.get_name())
# # # # # gr = Dog("Golden Retriever")
# # # # # print(gr.breed)
# # # # # p = Dog("Poodle")
# # # # # print(p.breed)

# # # # dog1 = Dog('Mastiff')
# # # # print(dog1.breed)
# # # # dog1.breed = 'German Shepherd'
# # # # print(dog1.breed)

# # # class Student:
# # #     school_name = 'Oxford'

# # #     def __init__(self, name):
# # #         self._name = name

# # #     @property
# # #     def name(self):
# # #         return self._name
    
# # #     @classmethod
# # #     def get_school_name(cls):
# # #         return cls.school_name

# # # bob = Student('Bob')
# # # sally = Student('Sally')
# # # print(bob.__class__.school_name, bob.name)
# # # print(sally.__class__.school_name, sally.name)
# # # print(Student.school_name, Student.get_school_name())

# # class Car:
# #     manufacturer = 'Ford'

# #     def __init__(self):
# #         self.manufacturer = 'Honda'
    
# #     def show_manufacturer(self):
# #         print(f'{Car.manufacturer=}')
# #         print(f'{self.manufacturer=}')
    
# # car1 = Car()
# # car1.show_manufacturer()

# class Bird:
#     def __init__(self, species):
#         self.species = species

# class Sparrow(Bird):
#     def __init__(self):
#         super().__init__('Sparrow')

# sparrow = Sparrow()
# print(sparrow.species)

class Mammal:
    def __init__(self):
        self.legs = 4

class Human(Mammal):
    def __init__(self):
        self.legs = 2

me = Human()
print(me.legs)