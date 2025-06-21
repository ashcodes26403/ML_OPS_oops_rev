# Simple Inheritance

# Base class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")


# Derived class
class Dog(Animal):

    def __init__(self, breed):
        super().__init__()
        self.breed = breed
    def speak(self):
        super().speak()
        print(f"{self.name} barks. He is of breed {self.breed}")
    
#instance of parent class 
# animal = Animal("Generic Animal")
# animal.speak()

# instance of the derived class
dog = Dog("Labrador")
dog.speak()