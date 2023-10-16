"""

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a Python file named lab_4-5.py
Write a program that prompts one user for their first name, 
then a second user for their first name. Using the format method, 
output a string that follows this template.

Hello, person1. My name is person2.


"""
# Author: Andrew Tkacs

# Prompt the first user for their first name

person1 = input("Enter your first name: ")

# Prompt the second user for their first name

person2 = input("Enter the second person's first name: ")

# format method used to create the output string

output_string = "Hello, {}. My name is {}.".format(person1, person2)

# Print the output

print(output_string)
