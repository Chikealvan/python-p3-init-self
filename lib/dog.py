#!/usr/bin/env python3

# Define a Dog class with a constructor that initializes 'name' and 'breed' attributes.
class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name  # Initialize the 'name' attribute with the provided name.
        self.breed = breed  # Initialize the 'breed' attribute with the provided breed.
        

    # Define a method 'bark' to print a message indicating that the dog is barking.
    def bark(self):
        print(f"{self.name} is barking.")

    # Define a method 'sit' to print a message indicating that the dog is sitting.
    def sit(self):
        print("The dog is sitting.")
