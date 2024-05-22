"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the Animal Kingdom program from Lab 1 to include polymorphism,
               demonstrating method overriding in derived classes.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Paste your base class Animal and the derived classes from Lab 1 here.

class Animal:
    def __init__(self, name: str, age: int, habitat: str) -> None:
        self.name = name
        self.age = age
        self.habitat = habitat

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

class Fish(Animal):
    def swim(self):
        print(f"{self.name} is swimming.")

# Modify the classes to demonstrate polymorphism through method overriding.
# Each derived class should override at least one method from the Animal class.
# For instance, you might want to override a 'make_sound' method to reflect the specific sound each animal makes.



# Create at least two instances of your derived classes





# Call the overridden methods on the instances.




