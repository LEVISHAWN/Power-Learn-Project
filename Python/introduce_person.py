class Person:
  """
  Represents a person's information
  
  attributes:
    name: representing the person's name.
    age: representing the person's age.
    gender: representing the person's gender.
  """

# Create the Person() class
class Person:
    # Define the constructor method
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Implement the 'introduce' method
    def introduce(self):
        print(f"Hello! My name is {self.name}, I am {self.age} years old, and I am {self.gender}.")

# Create an instance and call the method
person1 = Person("Levi", 19, "Male")
person1.introduce()
  
