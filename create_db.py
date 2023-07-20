import sqlite3

exercises = {"Lists":["Write a program to find the length of a list.", 
                      "Write a program to concatenate two lists.",
                      "Write a program to find the maximum and minimum elements in a list.",
                      "Write a program to remove duplicates from a list.",
                      "Write a program to check if a list is empty or not.",
                      "Write a program to sort a list in ascending order.",
                      "Write a program to reverse a list.",
                      "Write a program to count the occurrences of an element in a list.",
                      "Write a program to find the sum of all elements in a list.",
                      "Write a program to find the average of all elements in a list."],

            "Dictionaries":["Write a program that creates an empty dictionary and adds key-value pairs to it.",
                            "Write a program that takes a dictionary as input and prints all the keys in the dictionary.",
                            "Write a program that takes a dictionary as input and prints all the values in the dictionary.",
                            "Write a program that takes a dictionary as input and prints all the key-value pairs in the dictionary.",
                            "Write a program that takes a dictionary as input and checks if a given key exists in the dictionary.",
                            "Write a program that takes a dictionary as input and removes a given key from the dictionary.",
                            "Write a program that takes a dictionary as input and removes all the key-value pairs from the dictionary.",
                            "Write a program that takes two dictionaries as input and merges them into a single dictionary.",
                            "Write a program that takes a dictionary as input and calculates the sum of all the values in the dictionary.",
                            "Write a program that takes a dictionary as input and finds the key with the maximum value in the dictionary."],

            "Tuples":["Write a Python program to create a tuple with different data types.",
                      "Write a Python program to create a tuple with numbers and print the sum of all the elements.",
                      "Write a Python program to find the length of a tuple.",
                      "Write a Python program to find the largest and smallest elements of a tuple.",
                      "Write a Python program to find the count of a specific element in a tuple.",
                      "Write a Python program to check if an element exists within a tuple.",
                      "Write a Python program to convert a tuple into a list.",
                      "Write a Python program to reverse a tuple.",
                      "Write a Python program to convert a list of tuples into a dictionary.",
                      "Write a Python program to concatenate two tuples."],

            "Sets":["Write a Python program to create an empty set.",
                    "Write a Python program to create a set with elements of different data types.",
                    "Write a Python program to find the length of a set.",
                    "Write a Python program to add an element to a set.",
                    "Write a Python program to remove an element from a set.",
                    "Write a Python program to check if an element exists within a set.",
                    "Write a Python program to perform union of two sets.",
                    "Write a Python program to perform intersection of two sets.",
                    "Write a Python program to perform difference between two sets.",
                    "Write a Python program to check if a set is a subset of another set."],

            "String manipulation":["Write a Python program to count the number of characters in a string.",
                                   "Write a Python program to reverse a string.",
                                   "Write a Python program to check if a string is a palindrome.",
                                   "Write a Python program to find the first occurrence of a specific character in a string.",
                                   "Write a Python program to count the number of occurrences of a specific character in a string.",
                                   "Write a Python program to remove all whitespaces from a string.",
                                   "Write a Python program to convert the first character of each word in a string to uppercase.",
                                   "Write a Python program to check if a string starts with a specific prefix.",
                                   "Write a Python program to split a string into a list of words.",
                                   "Write a Python program to replace all occurrences of a specific substring in a string."],

            "Indexing and Slicing":["Write a Python program to print the first character of a string.",
                                    "Write a Python program to print the last character of a string.",
                                    "Write a Python program to print the n-th character of a string.",
                                    "Write a Python program to print the first 3 characters of a string.",
                                    "Write a Python program to print the last 3 characters of a string.",
                                    "Write a Python program to print a substring from a string using positive indexing.",
                                    "Write a Python program to print a substring from a string using negative indexing.",
                                    "Write a Python program to print every second character of a string.",
                                    "Write a Python program to reverse a string using slicing.",
                                    "Write a Python program to check if a string is a palindrome using slicing."],

            "Mutable and Imutable types":["Create a program that demonstrates the difference between mutable and immutable types.",
                                          "Write a function that takes a string as input and returns a new string with all uppercase letters.",
                                          "Create a list of strings and try to modify one of the elements. What happens?",
                                          "Write a function that takes a list of strings and sorts them in alphabetical order.",
                                          "Create a tuple of strings and try to modify one of the elements. What happens?",
                                          "Write a program that swaps the values of two variables without using a temporary variable.",
                                          "Create a dictionary with string keys and integer values. Modify one of the values and print the updated dictionary.",
                                          "Write a function that takes a list of strings and removes any duplicates.",
                                          "Create a program that demonstrates the concept of shallow copy and deep copy.",
                                          "Write a program that uses a set to remove any duplicate strings from a list."],

            "Data types":["Write a program to demonstrate the immutability of strings. Create a variable `name` and assign it a string value. Try to change a character in the string and observe the output.",
                          "Create a list `numbers` with some integer values. Modify one of the elements in the list and print the updated list.",
                          "Write a program to demonstrate the immutability of tuples. Create a tuple `my_tuple` with some values. Try to change one of the values and observe the output.",
                          "Create a dictionary `student` with keys as the names of students and values as their respective ages. Update the age of one student and print the updated dictionary.",
                          "Write a program to demonstrate the immutability of sets. Create a set `my_set` with some values. Try to add or remove an element from the set and observe the output.",
                          "Create a variable `x` and assign it an integer value. Create another variable `y` and assign it the value of `x`. Modify the value of `x` and print both `x` and `y` to observe the difference.",
                          "Create a list `fruits` with some fruit names. Create another variable `my_fruits` and assign it the value of `fruits`. Append a new fruit to `fruits` and print both `fruits` and `my_fruits` to observe the difference.",
                          "Write a program to demonstrate the immutability of frozensets. Create a frozenset `my_frozenset` with some values. Try to add or remove an element from the frozenset and observe the output.",
                          "Create a dictionary `person` with keys as the names of people and values as their respective email addresses. Create another variable `my_person` and assign it the value of `person`. Update the email address of one person in `person` and print both `person` and `my_person` to observe the difference.",
                          "Create a variable `a` and assign it a float value. Create another variable `b` and assign it the value of `a`. Modify the value of `a` and print both `a` and `b` to observe the difference."],

            "Methods of types":["Write a program that takes a string input from the user and uses the `upper()` method to convert it to uppercase.",
                                "Write a program that takes a list of numbers as input from the user and uses the `sort()` method to sort the list in ascending order.",
                                "Write a program that takes a tuple as input from the user and uses the `count()` method to count the number of occurrences of a specific element in the tuple.",
                                "Write a program that takes a dictionary as input from the user and uses the `keys()` method to print all the keys in the dictionary.",
                                "Write a program that takes a set as input from the user and uses the `add()` method to add an element to the set.",
                                "Write a program that takes a string input from the user and uses the `split()` method to split the string into a list of words.",
                                "Write a program that takes a list of strings as input from the user and uses the `join()` method to concatenate all the strings into one.",
                                "Write a program that takes a list of numbers as input from the user and uses the `max()` method to find the maximum value in the list.",
                                "Write a program that takes a tuple as input from the user and uses the `index()` method to find the index of a specific element in the tuple.",
                                "Write a program that takes a dictionary as input from the user and uses the `values()` method to print all the values in the dictionary."],

            "Comprehension":["Write a program that uses list comprehension to create a list of even numbers from 1 to 20.",
                            "Write a program that uses dictionary comprehension to create a dictionary mapping numbers from 1 to 10 to their squares.",
                            "Write a program that uses set comprehension to create a set of vowels from a given string.",
                            "Write a program that uses list comprehension to create a list of the first letter of each word in a given sentence.",
                            "Write a program that uses dictionary comprehension to create a dictionary mapping lowercase letters to their corresponding ASCII values.",
                            "Write a program that uses set comprehension to create a set of common elements between two given lists.",
                            "Write a program that uses list comprehension to create a list of numbers from 1 to 100, but only includes numbers that are divisible by both 3 and 5.",
                            "Write a program that uses dictionary comprehension to create a dictionary mapping each word in a given sentence to its length.",
                            "Write a program that uses set comprehension to create a set of unique characters from a given string.",
                            "Write a program that uses list comprehension to create a list of all prime numbers between 1 and 100."],

            "Exceptions":["Write a program that uses a try-except block to handle a ZeroDivisionError when dividing a number by zero.",
                          "Write a program that uses a try-except block to handle a ValueError when converting a string to an integer.",
                          "Write a program that uses a try-except block to handle an IndexError when accessing an element from a list using an invalid index.",
                          "Write a program that uses a try-except block to handle a FileNotFoundError when opening a non-existent file.",
                          "Write a program that uses a try-except block to handle a KeyError when accessing a non-existent key from a dictionary.",
                          "Write a program that uses a try-except block to handle a TypeError when performing an unsupported operation on different data types.",
                          "Write a program that uses a try-except block to handle a NameError when accessing a variable that is not defined.",
                          "Write a program that uses a try-except block to handle an OverflowError when performing a calculation that exceeds the maximum limit of the data type.",
                          "Write a program that uses a try-except block to handle a KeyboardInterrupt when the user interrupts the program execution.",
                          "Write a program that uses a try-except block to handle a FileNotFoundError and a PermissionError when opening a file and performing operations on it."],

            "Local and global scope":["Write a program that defines a global variable and a function that modifies its value. Print the value of the variable before and after calling the function.",
                                      "Write a program that defines a local variable inside a function and tries to access it outside the function. Handle the NameError that occurs.",
                                      "Write a program that defines a local variable inside a function and prints its value. Call the function and observe if the variable is accessible outside the function.",
                                      "Write a program that defines a global variable and a local variable with the same name inside a function. Print the value of both variables inside and outside the function.",
                                      "Write a program that defines a global variable and a function that tries to modify its value using the `global` keyword. Print the value of the variable before and after calling the function.",
                                      "Write a program that defines a local variable inside a nested function and tries to access it from the outer function. Handle the NameError that occurs.",
                                      "Write a program that defines a global variable and a local variable inside a function with the same name. Print the value of both variables inside and outside the function.",
                                      "Write a program that defines a global variable and a local variable inside a function. Modify the value of the local variable and print both variables inside and outside the function.",
                                      "Write a program that defines a global variable and a function that assigns a new value to it. Call the function multiple times and observe if the value of the variable changes.",
                                      "Write a program that defines a local variable inside a function and a nested function. Try to access the local variable from the nested function and handle the NameError that occurs."],

            "Closures":["Create a closure that adds a constant number to a given number.",
                        "Create a closure that calculates the average of a series of numbers.",
                        "Create a closure that counts the number of times a function is called.",
                        "Create a closure that calculates the factorial of a given number.",
                        "Create a closure that checks whether a number is prime or not.",
                        "Create a closure that finds the maximum and minimum numbers from a list.",
                        "Create a closure that calculates the sum of all even numbers in a list.",
                        "Create a closure that generates Fibonacci numbers.",
                        "Create a closure that converts temperatures between Celsius and Fahrenheit.",
                        "Create a closure that calculates the area and circumference of a circle."],

            "Short circuit evaluation":["Write a program that asks the user for two numbers and checks if both numbers are positive using short circuit evaluation. If both numbers are positive, print 'Both numbers are positive'. Otherwise, print 'At least one number is not positive'.",
                                        "Write a program that asks the user for a number and checks if the number is divisible by 3 and 5 using short circuit evaluation. If the number is divisible by both 3 and 5, print 'Divisible by 3 and 5'. Otherwise, print 'Not divisible by 3 and 5'.",
                                        "Write a program that asks the user for a string and checks if the string is empty or has more than 10 characters using short circuit evaluation. If the string is empty or has more than 10 characters, print 'Invalid input'. Otherwise, print 'Valid input'.",
                                        "Write a program that asks the user for two boolean values and checks if at least one of the values is True using short circuit evaluation. If at least one of the values is True, print 'At least one value is True'. Otherwise, print 'Both values are False'.",
                                        "Write a program that asks the user for a number and checks if the number is greater than 10 and less than 20 using short circuit evaluation. If the number is within the range, print 'Number is in range'. Otherwise, print 'Number is out of range'.",
                                        "Write a program that asks the user for a string and checks if the string starts with 'a' or ends with 'z' using short circuit evaluation. If the string satisfies either condition, print 'String matches the condition'. Otherwise, print 'String does not match the condition'.",
                                        "Write a program that asks the user for two numbers and checks if either of the numbers is zero using short circuit evaluation. If either of the numbers is zero, print 'At least one number is zero'. Otherwise, print 'None of the numbers are zero'.",
                                        "Write a program that asks the user for a string and checks if the string contains both uppercase and lowercase letters using short circuit evaluation. If the string contains both uppercase and lowercase letters, print 'String contains both uppercase and lowercase letters'. Otherwise, print 'String does not contain both uppercase and lowercase letters'.",
                                        "Write a program that asks the user for a number and checks if the number is positive or even using short circuit evaluation. If the number is positive or even, print 'Number is positive or even'. Otherwise, print 'Number is negative and odd'.",
                                        "Write a program that asks the user for a string and checks if the string contains the word 'python' or the word 'programming' using short circuit evaluation. If the string contains either of the words, print 'String contains <python> or <programming>'. Otherwise, print 'String does not contain <python> or <programming>'."]}


conn = sqlite3.connect("Ex_App/exercise_db.db")
cur = conn.cursor()

for key, value in exercises.items():
    key = key.replace(" ", "_")
    cur.execute(f"CREATE TABLE IF NOT EXISTS {key} (exercise TEXT)")
    #conn.commit()
    cur.executemany(f"INSERT INTO {key} (exercise) VALUES (?)", [(v,) for v in value])
    #cur.executemany(f"INSERT INTO {key} (exercise) VALUES (?)", [v for v in value])
    conn.commit()


# test = cur.execute("SELECT * FROM Closures")
# for row in test:
#     print(row, "\n")


cur.close()
conn.close()

