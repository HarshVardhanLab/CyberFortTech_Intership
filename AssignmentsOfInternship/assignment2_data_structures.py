# Creating a tuple with 5 favorite movies
favorite_movies = ("Inception", "Interstellar", "Gravity", "Parasite", "3 Idiots")

# Accessing and printing the third movie (index 2)
print("Third favorite movie:", favorite_movies[2])

#favorite_movies[1] = "Tenet"
#TypeError: 'tuple' object does not support item assignment

# Creating a list with duplicate numbers
number_list = [1, 2, 2, 3, 4, 4, 5]

# Converting list to set to remove duplicates
unique_numbers = set(number_list)
print("Unique numbers:", unique_numbers)

# Adding a new number to the set
unique_numbers.add(6)
print("After adding 6:", unique_numbers)

# Removing a number from the set
unique_numbers.remove(2)
print("After removing 2:", unique_numbers)

# Finding union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of sets:", union_set)

#  Dictionaries


# Creating a student dictionary
student = {
    "name": "Ali",
    "roll_no": "CFT101",
    "marks": 85
}

# Adding a new key 'grade'
student["grade"] = "A"

# Updating the 'marks'
student["marks"] = 90

# Looping through the dictionary and printing keys and values
print("Student details:")
for key, value in student.items():
    print(f"{key}: {value}")


#Bonus Challenge


# Dictionary with subjects and marks
subject_marks = {
    "Math": 95,
    "Science": 88,
    "English": 76,
    "History": 84
}

# Calculating and printing average marks
total = sum(subject_marks.values())
average = total / len(subject_marks)
print("Average marks:", average)
