def greet():
    print("hello")
    print("how do you do?")
    print("Isn't the weather nice?")

greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"how do you do {name}")

greet_with_name


# Now the argument is the actual piece of data that's going to be passed over to this function when it's

# being called, whereas the parameter is the name of that data,

# and we use the parameter inside the function to refer to it and to do things with it.

# exercise:
def num_of_weeks(age):
    weeks = (90-age)*52
    print(f"You have {weeks} left.")

num_of_weeks(67)

# Functions with more tahn 1 inputs

def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Harshil","BWM")
greet_with(name="Harshil",location="BWM")


# exercise
# name_1 = input("your_name")
# name_2 = input("your patner name")

# combine_name = name_1+name_2.upper()

# T = combine_name.count("T")
# R= combine_name.count("R")
# U = combine_name.count("U")
# E = combine_name.count("E")
# str1 = int(T+R+U+E)

# L = combine_name.count("L")
# O = combine_name.count("O")
# V = combine_name.count("V")
# E = combine_name.count("E")
# str2 = int(L+O+V+E)

# print(str1+str2)


# exercise 
rev = [1,2,3]
print(rev[::-2])

# Create a script that generates and prints a list of numbers from 1 to 20. Please do not create the list manually.

my_range = range(1,23)
print(list(my_range))


# Ans: 
# The list() function is used to convert an iterable (such as a string , tuple or dictionary) into a list.It takes an iterable as an argument and returns a list with each element of the iterable as an itrm in the list.

# The python range() function returns a sequence of numbers, in given a range. The most common use of it is to iterate sequences on a sequence of numbers using python loops.
# The range() function in Python returns a range object, not a list of numbers. This object is an iterable, which means you can loop over it to access the numbers in the specified range.

# Syntax: range(start, stop, step)

# Parameter :

# start: [ optional ] start value of the sequence
# stop: next value after the end value of the sequence
# step: [ optional ] integer value, denoting the difference between any two numbers in the sequence
# Return : Returns an object that represents a sequence of numbers

# there’s an interesting quirk here: dictionaries are inherently unordered collections, so when you convert a dictionary to a list, Python only considers the keys. 
ok = list({"j":"harshil",
           "l":2})
print(ok)


# using list comprehension: List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# syntax :      [expression for item in iterable if condition == True]
l = [x*10 for x in my_range]
print(l)


# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
new_lists = ["apple","banana","cherry"]
new_lists = ["hello"+x for x in new_lists]
print(new_lists)



b = [x*10 for x in my_range if x>2]
print(b)