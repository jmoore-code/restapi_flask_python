# Video 13- advanced set operations 



# art = {"Bob", "Jen", "Rolf", "Charlie"}
# science = {"Bob", "Jen", "Adam", "Anne"}


# both = art.intersection(science)
# print(both)



# Video 15- Booleans

# the same as javascript for operators

# python can compare list 
# friends = ["Rolf", "Bob"]
# abroad = ["Rolf", "Bob"]

# print(friends == abroad) will print true



# Video 16 - 
# day_of_week = input("what day of the week is it today?").lower()
# if day_of_week == "monday":
#     print("Have a great start to your week!")
# elif day_of_week == "tuesday":
#     print("It's Tuesday")
# else:
#     print("Full speed ahead!")

# print("This always runs") 



#video 18 - "if and in"

# movies_watched = {"The Matrix", "Green Book", "Her"}
# user_movie = input("Enter something you've watched recently: ")

# if user_movie in movies_watched: 
#     print(f"I've watched {user_movie} too!")
# else:
#     print("I haven't watched that yet.")

# example 2
# number = 7
# user_input = input("Enter 'y' if you would like to play: ").lower()

# if user_input == "y":
#     user_number = int(input("guess our number: "))
#     if user_number == number:
#             print("You guessed correctly!")
#     elif number - user_number in (1, -1):
#         print("You were off by one")
#     else:
#         print("sorry, it's wrong")
# else:
#     print("Good bye")

# video 19 - loops
# while loop
# number = 7

# while True:
#     user_input = input("Would like to play? (Y/n) ")

#     if user_input == "n":
#         break 

#     user_number = int(input("guess our number: "))
#     if user_number == number:
#             print("You guessed correctly!")
#     elif number - user_number in (1, -1):
#         print("You were off by one")
#     else:
#         print("sorry, it's wrong")
   
# for loop

# friends = ["Rolf", "Jen", "Bob", "Anne"]

# for friend in friends:
#     print(f"{friend} is my friend.")

# exmaple of using for loop to avg grades in list however you can also use sum instead
# grades = [35, 67, 98, 100, 100]
# total = 0 
# amount = len(grades)

# for grade in grades:
#     total += grade

# print (total / amount)

# sum example
# grades = [35, 67, 98, 100, 100]
# total = sum(grades) 
# amount = len(grades)
# print (total / amount)



# video 21 - list comprehensions
# numbers = [1, 2, 5]
# doubled = [num * 2 for num in numbers]
# print(doubled)


# example 2
# friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
# starts_s = [friend for friend in friends if friend.startswith("S")]

# print(starts_s)



# video 22 - Dictionaries
# friend_ages = {"Rolf": 24, "Adam": 30 , "Anne": 27}

# friend_ages["Bob"] = 29

# print(friend_ages)

# friends = [
#     {"name": "Rolf", "age": 24},
#     {"name": "Adam", "age": 30},
#     {"name": "Anne", "age": 27}
# ]

# print(friends[1]["name"])

# student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}")

# attendance_values = student_attendance.values()
# print(sum(attendance_values) / len(attendance_values))



# video 23 - destructing variables
#x, y = 5, 11 // x will be = 5 and y = 11

# people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

# for name, age, profession in people:
#     print(f"Name: {name}, Age: {age}, Profession: {profession}")

# person = ("Bob", 42, "Mechanic")
# name, _, profession = person
# print(name, profession)
# #collects first value in head and rest in tail
# head, *tail = [1, 2, 3, 4]
# print(head)
# print(tail)
# # collects all values in head and puts last one in tail
# *head, tail = [1, 2, 3, 4]
# print(head)
# print(tail)

# video 24 Functions-------------------------------------------------
# def hello(): 
#     print("hello")
# hello()

# def user_age_in_seconds():
#     user_age = int(input("Enter your age: "))
#     age_seconds = user_age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is {age_seconds}.")
# print("Welcome to the age in seconds program")
# user_age_in_seconds()
# print("Goodbye")



# video 25 function arguments and parameters ----------------------

# def add(x, y):
#     result = x + y
#     print (result)
# add(5,3)

# def divide(dividend, divisor):
#     if divisor != 0:
#         print(dividend / divisor)
#     else:
#         print("you fool!")
# # it is recommend to call functions using key-value parameters for better readability
# divide(dividend=15, divisor=3)



# video 26 default parameter values
# you don't need to define y if you give it a default value
# def add(x, y=8):
#     print(x + y)

# add(x=5)


# video 27 returning functions values
# functions return "None" by default, so you must "return" something from it
# def add(x, y):
#     print( x + y)
#     return x + y

# result = add(5, 8)
# print(result)



# video 29 Lambda functions -

# add = lambda x, y: x + y
# print(add(5,7))

# sequence = [1, 3, 5, 9]
# doubled = [(lambda x: x*2)(x) for x in sequence]
# doubled2 = list(map(lambda x: x *2, sequence))

# print(doubled)
# print(doubled2)



# Video 30 Dictionaries comprehensions

# users = [
#     (0, "Bob", "password"),
#     (1, "Rolf", "bob123"),
#     (2, "Jose", "longp4assword"),
#     (3, "username", "1234")
# ]

# username_mapping = {user[1]: user for user in users}

# username_input = input("Enter your username: ")
# password_input = input ("Enter your password: ")

# _, username, password = username_mapping[username_input]

# if password_input == password:
#     print("Your details are correct")
# else:
#     print("Your details are incorrect.")



# Video 32 - unpacking arguments

# def multiply(*args):
#     print(args)
#     total = 1
#     for arg in args:
#         total = total * arg
#     return total

# print(multiply(1, 3, 5))

# def add(x, y):
#     return x + y

# nums = [3, 5]
# print(add(*nums)) #the *nums will unpack the list and pass 3 for x and 5 for y

# def add(x, y):
#     return x + y

# nums = {"x": 15, "y": 25}
# print(add(**nums)) #the ** tells python to unpack a dictionary and matchs the keys with the named inputs



# video 33 - unpacking keyword arguments
# def named(name, age):
#     print(name, age)

# details = {"name": "Bob", "age": 25}

# named(**details)

# def named(**kwargs):
#     print(kwargs)

# def print_nicely(**kwargs):
#     named(**kwargs)
#     for arg, value in kwargs.items():
#         print(f"{arg}: {value}")

# print_nicely(named="Bob", age=25)



#  video 34 - object orientated programming

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#     def average(self):
#         return sum(self.grades) / len(self.grades)

# student = Student("Bob", (90, 90, 93, 78, 90))
# print(student.name)
# print(student.grades)
# print(student.average())



# video 35 - magic methods

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"Person {self.name}, {self.age} years old."

#     def __repr__(self): # shows up in debugger and other places, use to represent an object as a string
#         return f"<Person {self.name}, {self.age}>"

# bob = Person("Bob", 35)
# print(bob)




# Video 37 @classmethod @staticmethod
# class ClassTest:
#     def instance_method(self):
#         print(f"Called instance_method of {self}")
#     @classmethod
#     def class_method(cls):
#         print(f"Called class_method of {cls}")
#     @staticmethod
#     def static_method(): #static methods don't receive self or class
#         print("Called static_method")

# # test = ClassTest()
# # test.instance_method()

# ClassTest.class_method()

# ClassTest.static_method()

# Example 2:
# class Book:
#     TYPES = ("hardcover", "paperback")

#     def __init__(self, name, book_type, weight):
#         self.name = name
#         self.book_type = book_type
#         self.weight = weight

#     def __repr__(self):
#         return f"<Book: {self.name}, {self.book_type}, weighting {self.weight}g>"

#     @classmethod
#     def hardcover(cls, name, page_weight):
#         return cls(name, cls.TYPES[0], page_weight + 100) 
    
#     @classmethod
#     def paperback(cls, name, page_weight):
#         return cls(name, cls.TYPES[1], page_weight)

# book = Book.hardcover("Harry Potter", 1500)
# light = Book.paperback("Python 101", 600)

# print(book)
# print(light)


# Video 39 - Class inheritance
# class Device:
#     def __init__(self, name, connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connected = True

#     def __str__(self):
#         return f"Device {self.name!r} ({self.connected_by})"
    
#     def disconnect(self):
#         self.connected = False
#         print("Disconnected.")
    

# class Printer(Device):
#     def __init__(self, name, connected_by, capacity):
#         super().__init__(name, connected_by) #super grabs the parents class and then inits it
#         self.capacity = capacity
#         self.remaining_pages = capacity

#     def __str_(self):
#         return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

#     def print(self, pages):
#         if not self.connected:
#             print("Your printer is not connected!")
#             return
#         print(f"Printing {pages} pages.")
#         self.remaining_pages -= pages

# printer = Printer("Printer", "USB", 500)
# printer.print(20)

# print(printer)



# video 40 class composition
# class BookShelf:
#     def __init__(self, *books):
#         self.books = books

#     def __str__(self):
#         return f"BookShelf with {len(self.books)} books"

# class Book:
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return f"Book {self.name}"

# book = Book("Harry Potter")
# book2 = Book("Python 101")
# shelf = BookShelf(book, book2)

# print(shelf)



# Video 41 Type Hinting

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
    