# Daily AIML Challenge - Day [1]

# Part 1: Input & Output

# Ask the user their name and favorite color, then print this sentence:
name = input("Enter your name: ")
favorite_color = input("Enter your favorite color: ")
print(f"Hello {name}! Your favorite color is {favorite_color}.")

# Take two numbers as input from the user and print their sum.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"The sum of {num1} and {num2} is: {num1 + num2}")

# Part 2: If-Else Conditions

# Ask the user for their age. If age is above 18, print "You are an adult." Else print "You are not an adult."
age = int(input("Enter your age: "))
if age > 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# Write a program to check whether a number is positive, negative, or zero.
number_check = float(input("Enter a number to check (positive, negative, or zero): "))
if number_check > 0:
    print("The number is positive.")
elif number_check < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Part 3: Loops

# Print numbers from 1 to 10 using a for loop.
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# Print only the even numbers between 1 and 20.
print("Even numbers between 1 and 20:")
for i in range(2, 21, 2):
    print(i)

# Part 4: Strings

# Ask the user for a word and print its length (use len()).
word = input("Enter a word: ")
print(f"The length of the word '{word}' is: {len(word)}")

# Take a string from the user and print the same string in reverse (without using [::-1]).
input_string = input("Enter a string to reverse: ")
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string
print(f"The reversed string is: {reversed_string}")

# Part 5: Lists

# Create a list of 5 numbers.
my_numbers = [10, 20, 30, 40, 50]

# Print the whole list
print(f"The whole list of numbers: {my_numbers}")

# Print the first and last elements
print(f"The first element is: {my_numbers[0]}")
print(f"The last element is: {my_numbers[-1]}")

# Add one more number to the list using .append()
my_numbers.append(60)
print(f"List after appending a number: {my_numbers}")

# Create a list of 3 fruits and ask the user to enter one more fruit to add to the list.
# Then print the updated list.
fruits = ["apple", "banana", "cherry"]
print(f"Initial list of fruits: {fruits}")
new_fruit = input("Enter one more fruit to add to the list: ")
fruits.append(new_fruit)
print(f"Updated list of fruits: {fruits}")