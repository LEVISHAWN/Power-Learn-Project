# Base class Animal
class Animal:
    def move(self):
        print("Animals have their own way of moving.")

class Bird(Animal):
    def move(self):
        print("Birds fly in the sky.")

class Fish(Animal):
    def move(self):
        print("Fish swim in the water.")

class Snake(Animal):
    def move(self):
        print("Snakes slither on the ground.")
