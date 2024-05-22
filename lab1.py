"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a base class for an animal and derived classes for specific 
               types of animals in an animal kingdom program.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Animal that represents a generic animal in an animal kingdom.
# This class should have an initialiser with at least three attributes. E.g. name, age, and habitat.
# Add at least two methods for common animal behaviors. E.g. eat and sleep.

class Animal:
    def __init__(self, name: str, age: int, habitat: str) -> None:
        self.name = name
        self.age = age
        self.habitat = habitat

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# Create at least two derived classes from the Animal class. E.g. Bird and Fish.
# Give each of the derived classes at least one specific behavior. E.g. fly and swim.
            
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

class Fish(Animal):
    def swim(self):
        print(f"{self.name} is swimming.")

# Create at least two instances of the Animal derived classes with different data.

eagle = Bird("Eagle", 10, "forest")
shark = Fish("Shark", 15, "Ocean")

# Write code that prints out the details of each animal and calls their specific behaviors.

print(eagle.name, eagle.age, eagle.habitat)
print(shark.name, shark.age, shark.habitat)
print(eagle.fly())
print(shark.swim())
print(eagle.eat())
print(shark.eat())

