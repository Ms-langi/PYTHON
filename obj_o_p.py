class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"My name is {self.name}, a {self.age} year old {self.gender}.")

# Creating an instance of the Person class
person1 = Person("Marianna", 23, "female")

# Calling the introduce method to display the person's information
person1.introduce()
