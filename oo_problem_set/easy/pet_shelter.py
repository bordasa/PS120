class Pet:
    def __init__(self, species, name, shelter):
        self._species = species
        self._name = name
        shelter.add_pet(self)
    
    @property
    def species(self):
        return self._species
    
    @property
    def name(self):
        return self._name
    
    @property
    def info(self):
        return f"a {self.species} named {self.name}"
    
class Shelter:
    def __init__(self):
        self.adopters = set()
        self.unadopted_pets = []

    def adopt(self, new_owner, pet):
        new_owner.add_pet(pet)
        
        try:
            pet_index = self.unadopted_pets.index(pet)
            self.unadopted_pets.pop(pet_index)
        except ValueError:
            print('This animal is not found in our database.')

        self.adopters.add(new_owner) #empty set won't add duplicate objects

    def print_adoptions(self):
        for adopter in self.adopters:
            print(f"{adopter.name} has adopted the following pets:")
            adopter.print_pet_list()
    
    def add_pet(self, pet):
        self.unadopted_pets.append(pet)

    def print_unadopted_pets(self):
        print("The Animal Shelter has the following unadopted pets:")
        for pet in self.unadopted_pets:
            print(pet.info)
    
    def number_unadopted_pets(self):
        print(f"The Animal shelter has {len(self.unadopted_pets)} unadopted pets.")

class Owner:
    def __init__(self, name):
        self._name = name
        self._pet_list = []
        
    @property
    def name(self):
        return self._name
    
    def add_pet(self, pet):
        self._pet_list.append(pet)

    def print_pet_list(self):
        for pet in self._pet_list:
            print(pet.info)
    
    def number_of_pets(self):
        return len(self._pet_list)



phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()


cocoa   = Pet('cat', 'Cocoa', shelter)
cheddar = Pet('cat', 'Cheddar', shelter)
darwin  = Pet('bearded dragon', 'Darwin', shelter)
kennedy = Pet('dog', 'Kennedy', shelter)
sweetie = Pet('parakeet', 'Sweetie Pie', shelter)
molly   = Pet('dog', 'Molly', shelter)
chester = Pet('fish', 'Chester', shelter)

shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")
shelter.number_unadopted_pets()