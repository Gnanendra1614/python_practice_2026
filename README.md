**Python Basics, Loops, Conditional Statements & Data Structures**

**1. Python Basics**

Python is a high-level and easy-to-learn programming language.
Python uses simple and readable syntax.
Variables are used to store data values.
Python does not require explicit variable type declaration.
The print() function is used to display output.
Comments are written using #.
The type() function is used to check the data type of a value.
Common Data Types
int – Whole numbers
float – Decimal numbers
str – Text values
bool – True or False

**2. Conditional Statements**

Conditional statements are used to make decisions in a Python program.
if is used to check a condition.
elif is used to check additional conditions.
else is executed when the given conditions are false.
Conditions use comparison operators such as >, <, ==, !=, >=, and <=.
Types
if
if-else
if-elif-else
Nested if

**3. Loops**

Loops are used to execute a block of code repeatedly.
Python mainly provides for and while loops.
A for loop is generally used to iterate over a sequence.
A while loop executes as long as a condition is True.
break is used to stop a loop.
continue is used to skip the current iteration.
range() is commonly used with for loops.

**4. Python Data Structures**

Python provides different data structures for storing and organizing multiple values.

**List**

Ordered and changeable collection.
Allows duplicate values.
Uses square brackets [].

**Tuple**

Ordered collection.
Generally immutable, meaning its elements cannot be directly changed.
Uses parentheses ().

**Set** 

Stores unique values.
Duplicate values are automatically removed.
Uses curly brackets {}.

**Dictionary**

Stores data in key-value pairs.
Uses curly brackets {}.
Values can be accessed using their keys.

**5. Data Structure Operations**

**List Operations**

append() – Add an element
insert() – Insert an element
remove() – Remove an element
pop() – Remove an element using index
sort() – Sort elements
reverse() – Reverse elements

**Tuple Operations**

Access elements using index
count() – Count occurrences
index() – Find the position of an element
Slicing
Tuple concatenation

**Set Operations**

add() – Add an element
remove() – Remove an element
discard() – Remove an element safely
union() – Combine sets
intersection() – Find common elements
difference() – Find different elements

**Dictionary Operations**

Access values using keys
Add and update key-value pairs
pop() – Remove an item
keys() – Get keys
values() – Get values
items() – Get key-value pairs
get() – Access a value safely
clear() – Remove all items

 Python Functions

A function is a reusable block of code that performs a specific task. Functions help to avoid repeating the same code and make programs easier to understand and maintain.

Parameters

A parameter is a variable defined in the function definition. It acts as a placeholder for the value that will be passed to the function.

Types of Parameters

Positional Parameters
Default Parameters
Keyword Parameters
Variable-Length Parameters
Variable-Length Keyword Parameters

Arugments:

An argument is the actual value that you pass to a function when you call it.

Types of Arguments in Python

There are mainly 5 types :

1.Positional Arguments
2.Keyword Arguments
3.Default Arguments
4.Variable-Length Positional Arguments
5.Variable-Length Keyword Argument

1. Positional Arguments

In positional arguments, values are passed according to the position/order of the parameters.

2. Keyword Arguments

In keyword arguments, we specify the parameter name while passing the value.

3. Default Arguments

A default argument is used when a parameter already has a default value.

4. Variable-Length Positional Arguments

Sometimes we don't know how many positional arguments the user will provide.

5. Variable-Length Keyword Arguments 

Sometimes we don't know how many keyword arguments will be provided.

Python Modules and Parameters

1. Python Modules

A module is a Python file (.py) that contains reusable code such as functions, variables, and classes. Modules help us organize code and reuse it in different programs.

2. Python Parameters

A parameter is a variable written inside the function definition. It receives a value when the function is called.

Python Programming – Modules, Packages, OOP & Functions


This repository contains my learning and practice work on important Python programming concepts, including:

Python Modules
Python Packages
Object-Oriented Programming (OOP)
Classes and Objects
Attributes and Methods
Constructors
Encapsulation
Inheritance
Polymorphism
Abstraction
Method Overloading
Method Overriding
Lambda Functions
Higher-Order Functions

1. Python Modules

A module is a Python file containing reusable code such as functions, classes, and variables.

Types of Modules

Built-in Modules – Modules provided by Python.
math
os
sys
random
datetime

User-Defined Modules – Modules created by the programmer.

2. Python Packages

A package is a directory that contains related Python modules and helps organize large applications.

Example Structure
my_package/
│
├── __init__.py
├── calculator.py
├── student.py
└── employee.py

3. Object-Oriented Programming (OOP)

OOP stands for Object-Oriented Programming.

It is a programming approach based on classes and objects.

Main OOP Concepts

Class
Object
Attributes
Methods
Constructor
Encapsulation
Inheritance
Polymorphism
Abstraction
Method Overloading
Method Overriding

4. Class

A class is a blueprint or template used to create objects.

Example:

class Student:
    pass

5. Object

An object is an instance of a class.

Example:

class Student:
    pass

student1 = Student()
student2 = Student()

6. Attributes

Attributes represent the properties or data of an object.

7. Methods

A method is a function defined inside a class.

Types of Methods

Python mainly has three types of methods:

Instance Method
Class Method
Static Method

8. Constructor

A constructor is used to initialize an object's attributes.

In Python, __init__() is commonly used as the constructor.

Types of Constructors

Default Constructor
Parameterized Constructor

9. Encapsulation

Encapsulation means combining data and methods within a class and controlling access to the data.

10. Inheritance

Inheritance allows a child class to acquire properties and methods from a parent class.

Types of Inheritance

Single Inheritance
Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance
Hybrid Inheritance

11. Method Overriding

Method overriding occurs when a child class provides its own implementation of a method that exists in the parent class.

12. Polymorphism

Polymorphism means many forms.

The same method or interface can behave differently depending on the object.

13. Method Overloading

Method overloading refers to using the same method name with different arguments.

Python does not support traditional method overloading by defining multiple methods with the same name. Similar behavior can be achieved using techniques such as default arguments.

14. Abstraction

Abstraction means hiding unnecessary implementation details and showing only the essential functionality.

Python provides the abc module to implement abstract base classes.

15. Lambda Functions

A lambda function is a small anonymous function created using the lambda keyword.

Common Uses of Lambda

map()
filter()
sorted()
reduce()

16. Higher-Order Functions

A higher-order function is a function that:

Takes another function as an argument, or
Returns another function.

Python Comprehensions

Python comprehensions provide a concise and readable way to create new collections from existing iterables such as lists, sets, dictionaries, strings, and ranges.

They reduce the amount of code required compared with traditional for loops while keeping the logic simple and readable.

Types of Comprehensions

List Comprehension
Conditional List Comprehension
If-Else Comprehension
Dictionary Comprehension
Set Comprehension
Nested Comprehension

What are Comprehensions?

A comprehension is a compact way to create a new collection by iterating over an existing iterable and optionally applying a condition or transformation.

1. List Comprehension

A list comprehension is used to create a new list.

2. Conditional List Comprehension

A condition can be added to a list comprehension to filter values.

3. If-Else Comprehension

An if-else expression can be used to transform every item.

4. Dictionary Comprehension

Dictionary comprehension is used to create dictionaries in a concise way.

5. Set Comprehension

Set comprehension creates a new set.

6. Nested Comprehension

A comprehension can contain multiple for clauses.