# Python Data Structures and Functional Programming Explained

This document explains various operations on fundamental Python data structures like **tuples**, **sets**, and **dictionaries**, and delves into **functional programming** concepts. It also outlines the structure of a command-line interface (CLI) based **student grade book system**.

---

## 1. Tuple Operations – Immutable Data in Action

**Tuples** are ordered, immutable collections of items. "Immutable" means that once a tuple is created, its elements cannot be changed, added, or removed.

**Key Operations Covered:**

* **Creation:** Demonstrates how to create a tuple.
* **Slicing:** Shows how to extract a portion of a tuple using indexing, similar to lists. For example, `fruits[3:8]` gets elements from index 3 up to (but not including) index 8.
* **Iteration (Reverse Order):** Explains how to loop through a tuple to print its elements in reverse order **without using slicing**, by iterating from the last index down to the first.
* **Tuple to List Conversion and Back:** Illustrates a common pattern: converting a tuple to a list to modify an item (since lists are mutable), then converting the list back into a tuple. This showcases how to "update" a tuple indirectly.
* **Nested Tuples:** Presents how to create tuples containing other tuples (e.g., `(fruit, quantity)` pairs) and how to access elements within these nested structures.

---

## 2. Advanced Set Logic

**Sets** are unordered collections of unique items. They are highly efficient for checking membership and performing mathematical set operations. Duplicates are automatically removed when a set is created or when items are added.

**Key Operations Covered:**

* **Creation:** Shows how to define sets of students enrolled in different courses.
* **`intersection()`:** Returns a new set containing elements common to both sets (students in **both** AI and ML).
* **`symmetric_difference()`:** Returns a new set containing elements that are in either of the sets, but **not in both** (students in only AI or only ML).
* **`union()`:** Returns a new set containing all unique elements from both sets (students enrolled in **at least one** course).
* **`difference()`:** Returns a new set containing elements present in the first set but **not** in the second (students in the full class list but not in AI or ML).
* **Removing Duplicates:** Demonstrates a practical use case of sets: easily removing duplicate entries from a list by converting the list to a set.

---

## 3. Dictionary Manipulation

**Dictionaries** are unordered collections of **key-value pairs**, where each **key must be unique**. They are optimized for retrieving values when the key is known.

**Key Operations Covered:**

* **Creation:** Sets up a `library` dictionary where book titles are keys and their availability (`True`/`False`) are values.
* **Adding Entries:** Explains how to add new key-value pairs to an existing dictionary.
* **`available_books()` Function:** A function that iterates through the library dictionary and returns a list of book titles that are currently available (`True`).
* **Nested Dictionaries:** Shows how to create a more complex dictionary structure where each book title maps to another dictionary containing detailed information like `author`, `year`, and `available` status.
* **Sorting with `lambda`:** Demonstrates how to sort dictionary items (specifically, the books in the `nested_library`) based on the `year` field using the `sorted()` function with a `lambda` expression. A `lambda` is a small anonymous function useful for short, one-time operations.

---

## 4. Functional Programming Challenge

This section features functions that embody principles of functional programming, emphasizing immutable data and pure functions (functions that produce the same output for the same input and have no side effects).

**Functions Explained:**

* **`filter_students(students)`:** Takes a list of `(name, marks)` tuples and uses a loop to **filter** for students who scored above 85.
* **`character_count(input_string)`:** Counts the frequency of each character in a given string. It uses a dictionary to store character counts, demonstrating how to update counts efficiently using `dict.get()`.
* **`matrix_transpose(matrix)`:** Accepts a matrix (represented as a list of lists) and returns its **transposed** form (rows become columns, and columns become rows). It shows how to iterate and rebuild the matrix for transposition.
* **`analyze_list(numbers)`:** Calculates the **minimum**, **maximum**, **average**, and **mode** of a list of numbers. The logic for finding the mode is implemented manually, demonstrating how to determine the most frequently occurring element without external libraries.

---

## 5. Mini Project: Student Grade Book System

This project is a simple **Command-Line Interface (CLI) based grade book system**. It allows users to input student data and provides calculated results and analytics.

**Core Functionality:**

* **Student Data Entry:** The user inputs the number of students, and for each student, their name and marks for three subjects are collected.
* **Data Storage:** All student information (marks, average, grade) is automatically stored in a **dictionary**, where student names serve as keys.
* **Average Calculation:** Computes the average marks for each student.
* **Grade Assignment:** Assigns a letter grade (A, B, or C) based on the calculated average marks:
    * **A:** Average $\ge 90$
    * **B:** Average $\ge 80$ and $<90$
    * **C:** Average $< 80$
* **Sorted Display:** Presents a sorted list of students based on their average marks, from highest to lowest, making it easy to identify top performers.
* **Analytics Dashboard:** Provides additional insights:
    * **Highest Average:** Identifies the student(s) with the highest average marks.
    * **Grade Distribution:** Shows the count of students who received each grade (A, B, C).
    * **Subject-wise Toppers:** Lists the student(s) who scored the highest in each individual subject.

This project integrates concepts from dictionaries, functions, sorting, and user input to create a practical application.