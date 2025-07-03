'''1. Tuple Operations – Immutable Data in Action
•	Create a tuple of 10 fruits.
•	Print fruits from index 3 to 7.
•	Use a loop to print the tuple in reverse order without using slicing.
•	Convert the tuple into a list, update one item, and convert it back to a tuple.
•	Create a nested tuple of (fruit, quantity) pairs and access quantities.
'''
#•	Print fruits from index 3 to 7.
fruits = ("apple", "banana", "cherry","mango","pineapple","strawberry","cherry","blueberry","kiwi","blackberry")
print(fruits[3:8])

#•	Use a loop to print the tuple in reverse order without using slicing.
num_tuple = (1,2,3,4,5,6,7,8,9,10)
reversed_num_tuple = []
for item in range(len(num_tuple)-1,-1,-1):
    reversed_num_tuple.append(num_tuple[item])
reversed_tup=tuple(reversed_num_tuple)
print(reversed_tup)

#•	Convert the tuple into a list, update one item, and convert it back to a tuple.
cities=("Aligarh","kanpur","jaipur","Agra","mumbai")

lst_cities=list(cities)

lst_cities[2]="Mathura"

updated_cities=tuple(lst_cities)
print(f"Tup of Cities before update: {cities} and after update: {updated_cities}")

#•	Create a nested tuple of (fruit, quantity) pairs and access quantities.
nested_fruits=(("apple",4), ("banana",7), ("cherry",5))
print(f"Quantity of {nested_fruits[1][0]} is:",nested_fruits[1][1])
#----------------------------------------------------------------------------------------------------------
'''2. Advanced Set Logic
•	Create two sets of students enrolled in “AI” and “ML” courses respectively.
•	Find students:
o	Enrolled in both courses
o	Enrolled in only one course (either AI or ML but not both)
o	Enrolled in at least one course
o	Not enrolled in either course (from a full class list)
•	Remove duplicate student entries from a long list using sets.
'''
#-----------------------------------------------------------------------------------------------------------
full_class_list = {"Harsh Vardhan", "Hritik", "Mohsin", "Rudra", "Gaurav", "leekesh", "Priya", "Rahul", "Simran"}
AI_courses={"Harsh Vardhan","Hritik","Mohsin","Rudra"}
ML_courses={"Hritik","Mohsin","Gaurav","leekesh"}
print(f"Enrolled in both courses {AI_courses.intersection(ML_courses)}")
print(f"Enrolled in only one course {AI_courses.symmetric_difference(ML_courses)}")
print(f"Enrolled in at least one course {AI_courses.union(ML_courses)}")
print(f"Not enrolled in either course (from a full class list) {full_class_list.difference(AI_courses.union(ML_courses))}")
print(f"Remove Duplicate in both courses {AI_courses.union(ML_courses)}")

'''3. Dictionary Manipulation
•	Create a dictionary representing a library with keys as book titles and values as availability (True or False).
•	Add a new book entry.
•	Write a function available_books(library_dict) that returns a list of only available books.
•	Create a nested dictionary for each book with fields: author, year, available.
•	Sort the books based on year using dictionary and lambda function.
'''
library = {
    "Data Structures and Algorithms": "True",
    "Operating Systems": "True",
    "Computer Networks": "False",
    "Database Management Systems": "False",
    "Software Engineering": "True",
    "Artificial Intelligence": "True",
    "Machine Learning": "True",
    "Deep Learning": "False",
    "Web Development": "True",
    "Mobile App Development": "False",
    "Cybersecurity": "True",
    "Cloud Computing": "False",
}
#•	Add a new book entry.
library["Quantum Computing"] = "True"
#Write a function available_books(library_dict) that returns a list of only available books.
print("\n--------------------------A function available_books(library_dict) that returns a list of only available books.---------------------------------")
print("\n")
def available_books(library_dict):
    available_book = []
    for title, availability in library_dict.items():
        if availability == "True":
            available_book.append(title)
    return available_book
print(available_books(library))
#•	Create a nested dictionary for each book with fields: author, year, available.
nested_library ={
    "Data Structures and Algorithms": {
        "author": "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein",
        "year": "2009",
        "available": True
    },
    "Operating Systems": {
        "author": "Andrew S. Tanenbaum, Herbert Bos",
        "year": "2006",
        "available": False
    },
    "Computer Networks": {
        "author": "Andrew S. Tanenbaum, David J. Wetherall",
        "year": "2010",
        "available": False
    },
    "Database Management Systems": {
        "author": "Raghu Ramakrishnan, Johannes Gehrke",
        "year": "2003",
        "available": False
    },
    "Software Engineering": {
        "author": "Ian Sommerville",
        "year": "2015",
        "available": True
    },
    "Artificial Intelligence": {
        "author": "Stuart Russell, Peter Norvig",
        "year": "2010",
        "available": True
    },
    "Machine Learning": {
        "author": "Tom M. Mitchell",
        "year": "1997",
        "available": True
    },
    "Deep Learning": {
        "author": "Ian Goodfellow, Yoshua Bengio, Aaron Courville",
        "year": "2016",
        "available": False
    },
    "Web Development": {
        "author": "Jon Duckett",
        "year": "2011",
        "available": True
    },
    "Mobile App Development": {
        "author": "Joseph Annuzzi Jr., Lauren Darcey, Shane Conder",
        "year": "2015",
        "available": False
    },
    "Cybersecurity": {
        "author": "William Stallings",
        "year": "2011",
        "available": True
    },
    "Cloud Computing": {
        "author": "Rajkumar Buyya, Christian Vecchiola, Thamarai Selvi",
        "year": "2013",
        "available": False
    },
    "Quantum Computing": {
        "author": "Michael A. Nielsen, Isaac L. Chuang",
        "year": "2010",
        "available": True
    }
}
# Sort the nested_library dictionary based on year using lambda
print("\n--------------------Sort the nested_library dictionary based on year using lambda------------------")
sorted_books = dict(
    sorted(nested_library.items(), key=lambda item: int(item[1]['year']))
)

# Display the sorted result
for book, details in sorted_books.items():
    print(f"{book}: {details}")
print("\n")

print("------------------||||||||||||||||||||||| Filter_students that accepts a list of (name, marks) |||||||||||||||||||||||||--------------")
print("\n")
'''4. Functional Programming Challenge
•	Write a function filter_students that accepts a list of (name, marks) tuples and returns students who scored more than 85.
•	Write a function character_count that returns a dictionary with the frequency of each character in a given string.
•	Write a function matrix_transpose(matrix) that takes a list of lists (matrix) and returns the transposed matrix.
•	Write a function that takes a list and returns a dictionary with:
o	min, max, average, and mode (write logic for mode without any library)
'''

def filter_students(students):
    filtered=[]
    for student in students:
        if student[1] >= 85 and student[1] <= 100:
            filtered.append(student)
    return filtered

tup_students = [("Harsh",86),("Gaurav",88),("Manash",78),("hritik",70)]
print(filter_students(tup_students))
print("\n")
print("••••••••••••••••••••Function character_count that returns a dictionary with the frequency of each character in a given string••••••••••••••••••••")
print("\n")
def character_count(value):
    freq = {}

    for char in value:
        freq[char] = freq.get(char, 0) + 1

    return freq
print(character_count("Harsh vardhan"))

print("\n")
print("-------------------A function matrix_transpose(matrix) that takes a list of lists (matrix) and returns the transposed matrix.-------------------")
print("\n")
def matrix_transpose(matrix):
    # Use list comprehension to switch rows and columns
    transposed = []
    for i in range(len(matrix[0])):  # Loop through columns
        new_row = []
        for row in matrix:           # Loop through each row
            new_row.append(row[i])   # Take the i-th element from each row
        transposed.append(new_row)
    return transposed
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

result = matrix_transpose(matrix)

print(result)


def analyze_list(numbers):
    if not numbers:
        return {}

    # Initialize values
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0
    freq = {}

    # Loop through the list
    for num in numbers:
        # Update min and max
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
        total += num

        # Count frequency for mode
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Calculate average
    average = total / len(numbers)

    # Find mode (number with highest frequency)
    mode = None
    max_freq = 0
    for num, count in freq.items():
        if count > max_freq:
            max_freq = count
            mode = num

    # Return result as dictionary
    return {
        'min': minimum,
        'max': maximum,
        'average': average,
        'mode': mode
    }
data = [4, 2, 7, 4, 9, 2, 4]
result = analyze_list(data)

print(result)

print("\n")
'''5. Mini Project: Student Grade Book System
•	Create a CLI-based grade book system where the user:
o	Enters number of students
o	For each student, enters name and marks for 3 subjects
o	Automatically stores all data in a dictionary
o	Calculates average marks for each student
o	Assigns grade based on rules:
	Avg ≥ 90: A
	Avg ≥ 80 and <90: B
	Avg < 80: C
o	Displays a sorted list of students based on their average marks (highest to lowest)
'''
def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    else:
        return 'C'

def main():
    students = {}
    grade_counts = {'A': 0, 'B': 0, 'C': 0}

    # Input number of students
    num = int(input("Enter the number of students: "))

    for i in range(num):
        print(f"\nEnter details for Student {i + 1}:")
        name = input("Name: ")

        # Input 3 subject marks
        marks = []
        for j in range(3):
            mark = float(input(f"Enter marks for Subject {j + 1}: "))
            marks.append(mark)

        # Calculate average
        avg = sum(marks) / 3
        grade = get_grade(avg)
        grade_counts[grade] += 1

        # Store in dictionary
        students[name] = {
            'marks': marks,
            'average': avg,
            'grade': grade
        }

    # Sort students by average marks (descending)
    sorted_students = sorted(students.items(), key=lambda x: x[1]['average'], reverse=True)

    # Display the sorted results
    print("\n--- Student Grade Report (Sorted by Average Marks) ---")
    print(f"{'Name':<15} {'Average':<10} {'Grade':<5}")
    print("-" * 35)
    for name, data in sorted_students:
        print(f"{name:<15} {data['average']:<10.2f} {data['grade']:<5}")

    # Analytics Dashboard
    print("\n --- Analytics Dashboard ---")

    # Highest average student
    top_student = sorted_students[0]
    print(f"\n Highest Average: {top_student[0]} ({top_student[1]['average']:.2f})")

    # Grade distribution
    print("\n Grade Distribution:")
    for grade in ['A', 'B', 'C']:
        print(f"Grade {grade}: {grade_counts[grade]} students")

    # Subject-wise toppers
    print("\n Subject-wise Toppers:")
    for subj_index in range(3):
        max_marks = -1
        topper_names = []
        for name, data in students.items():
            mark = data['marks'][subj_index]
            if mark > max_marks:
                max_marks = mark
                topper_names = [name]
            elif mark == max_marks:
                topper_names.append(name)
        print(f"Subject {subj_index + 1}: {', '.join(topper_names)} ({max_marks} marks)")


main()





