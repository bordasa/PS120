class Cat:
    def __init__(self):
        pass

    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat!")

kitty = Cat()
print(type(kitty))
type(kitty).generic_greeting()