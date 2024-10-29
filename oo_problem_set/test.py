class PlayList:
    def __init__(self):
        self._songs = {}

    def play_song(self, song_name, count):
        self._songs.setdefault(song_name, 0)
        self._songs[song_name] += count
    
    def __mul__(self, num):
        new_songs = {name: count * num for name, count
                in self._songs.items()}
        new_playlist = PlayList()

        for name, count in new_songs.items():
            new_playlist.play_song(name, count)
        
        return new_playlist
    
    def __str__(self):
        return str(self._songs)

p1 = PlayList()
p1.play_song("Song1", 3)
p1.play_song("Song2", 2)

p2 = p1 * 2
print(p2)                     # {'Song1': 6, 'Song2': 4}

try:
    print(p1.songs["Song1"])
except AttributeError as e:
    print(f"Error: {e}")      # Prints error message

class Dog:
    def __init__(self, name):
        self.name = name

fido1 = Dog('Fido')
fido2 = Dog('Fido')
fido3 = fido1

print(fido1 is fido2)  #False
print(fido1 is fido3)  #True
print(fido3 is fido2)  #False

class Employee:
    _number_of_employees = 0
    _role_distribution = {}

    def __init__(self, name, role):
        self._name = name
        
        self._role = role
        self._role_distribution.setdefault(self._role, 0)
        self._role_distribution[self._role] += 1

        Employee._number_of_employees += 1

    @classmethod
    def get_employee_count(cls):
        return cls._number_of_employees
    
    @classmethod
    def get_role_distribution(cls):
        return cls._role_distribution

emp1 = Employee('Srdjan', 'Engineer')
emp2 = Employee('Chris', 'Manager')
emp3 = Employee('Pete', 'Engineer')

print(Employee.get_employee_count())       # 3
print(Employee.get_role_distribution())
# {'Engineer': 2, 'Manager': 1}

class Animal:
    def eat(self):
        print("I'm eating")

class SwimMixin:
    def swim(self):
        print("I'm swimming")

class FlyMixin:
    def fly(self):
        print("I'm flying")

class Fish(SwimMixin, Animal):
    pass

class Bird(FlyMixin, Animal):
    pass

class Duck(SwimMixin, Bird):
    pass

daffy = Duck()
print(Duck.mro())
print(Bird.mro())
print(daffy.__class__.mro())

class ColorIntensity:
    def __init__(self, intensity):
        self.intensity = intensity

    @property
    def intensity(self):
        return self._intensity
    
    @intensity.setter
    def intensity(self, intensity):
        if 0 <= intensity <= 255:
            self._intensity = intensity
        else:
            raise ValueError("Intensity must be between 0 and 255.")

    def __lt__(self, other):
        if not isinstance(other, ColorIntensity):
            return NotImplemented
        
        return self.intensity < other.intensity
    
    def __eq__(self, other):
        if not isinstance(other, ColorIntensity):
            return NotImplemented
        
        return self.intensity == other.intensity
    
    def __gt__(self, other):
        if not isinstance(other, ColorIntensity):
            return NotImplemented
        
        return self.intensity > other.intensity
    
ci1 = ColorIntensity(100)
ci2 = ColorIntensity(150)
ci3 = ColorIntensity(100)
print(ci1.intensity)

try:
    ci4 = ColorIntensity(256)
except ValueError as e:
    print(f"Error: {e}")      # Prints an error message

try:
    ci5 = ColorIntensity(-1)
except ValueError as e:
    print(f"Error: {e}")      # Prints an error message

print(ci1 < ci2)    # True
print(ci1 == ci2)   # False
print(ci3 == ci1)   # True
print(ci3 > ci1)    # False
print(ci2 > ci3)    # True

import random

class Player:
    def __init__(self, name):
        self.name = name
        self._health = 100
        self._strength = Player.roll_dice()
        self._intelligence = Player.roll_dice()
        self._player_class = self.__class__.__name__

    def __str__(self):
        return ((f"Name: {self.name}\n")
            + (f"Class: {self._player_class}\n")
            + (f"Health: {self._health}\n")
            + (f"Strength: {self._strength}\n")
            + (f"Intelligence: {self._intelligence}"))

    @classmethod
    def roll_dice(self):
        return random.randint(2, 12)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            return ('Name must be a string.')
        
        self._name = name
    
    def heal(self, amount):
        self.health += amount
    
    def hurt(self, amount):
        self.health -= amount

class WearArmorMixin:
    def attach_armor(self):
        print("I put on armor!")

    def remove_armor(self):
        print("I take off the armor!")

class CastSpellsMixin:
    def cast_spell(self, spell):
        print(f"I cast {spell}!")

class PotionMixin:
    def create_potion(self):
        print("I made a potion!")

class Warrior(WearArmorMixin, Player):
    def __init__(self, name):
        super().__init__(name)
        self._strength += 2

class Paladin(WearArmorMixin, CastSpellsMixin, Player):
    def __init__(self, name):
        super().__init__(name)

class Magician(CastSpellsMixin, Player):
    def __init__(self, name):
        super().__init__(name)
        self._intelligence += 2

class Bard(CastSpellsMixin, PotionMixin, Player):
    def __init__(self, name):
        super().__init__(name)

alexei = Paladin('Alexei')
print(alexei)
alexei.cast_spell('Fireball')
alexei.attach_armor()
print()
alexei = Bard('Alexei')
print(alexei)
alexei.cast_spell("Fireball")
