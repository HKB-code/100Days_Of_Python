"""Higher-order functions in Python are a powerful concept that let you treat functions as first-class citizens. That means you can pass them around just like variables—into other functions, return them from functions, and even store them in data structures. Here's a breakdown tailored to your backend mindset, Harshil:

🧠 What Is a Higher-Order Function?
A higher-order function is any function that:
- Takes another function as an argument, or
- Returns a function as its result
This enables dynamic behavior, cleaner abstractions, and functional-style programming.

Analogy:- “Higher-order functions are like power sockets—you plug in different appliances (functions) and get different results, all from the same outlet."
"""

# 🔧 Practical Examples
# 1. Passing a Function as an Argument

def apply(func,value):
    return func(value)

def square(x):
    return x*x

print(apply(square,5
            ))

# 2. Returning a Function

def multiplier(n):
    return lambda x:x*n

double = multiplier(2)

print(double(10))

#3. Built-in Higher-Order Functions
# - map(func, iterable) – applies a function to each  item
# - filter(func, iterable) – filters items based on a condition
# - sorted(iterable, key=func) – sorts using a custom key
 
nums = [1,2,3,4,5]
squared = list(map(lambda x: x**2,nums))
evens = list(filter(lambda x:x%2==0, nums ))


# 🧵 Bonus: Decorators = Higher-Order Functions
# Decorators are syntactic sugar for wrapping functions with other functions. Perfect for logging, authentication, caching, etc.


# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# @logger
# def greet(name):
#     return f"Hello, {name}"

# print(greet("Harshil"))

# logger(func)- this is a decorator function
"""->what it does that it wraps a function and inject some extra behaviour like logging , timming,error handling etc

->it accepts a func[the func that is going to be decorate] and return a wrapper
"""

# wrapper(*args, **kwargs) — actual wrapping logic
"""-> It is an inner function that do some work before calling the original function

-> *args, **kwargs , it means it can take any arrguments [positional or keyword]
 
-> return func(*args, **kwargs) — It calls the original function and return its result

"""

# @logger — decorator syntax 
"""
->greet = logger(greet)
->Now the greet function is actually a wrapper - it will first log in, then call the original greet.
"""


# print(greet("Harshil"))
"""
->when this line executes,
1.It calls the wrapper("Harshil")
2.It prints "Calling greet" in console.
3.Then executes greet("Harshil")->returns "Hello, Harshil"
4.Final Output: Hello, Harshil
"""


# 🧵 Real-Life Analogy (Backend Style)
"""Socho tumhare paas ek API endpoint hai /greet. Tum chahte ho ki har baar jab ye endpoint hit ho, ek log print ho jaye — "Calling greet".
Instead of modifying the actual handler, tum ek middleware laga dete ho jo ye kaam kare.
Python decorator = Express.js middleware. Clean, reusable, and elegant.
"""



# 🧠 Bonus Tip: functools.wraps
"""f you want the original name of the greet function, docstering, etc. to be preserved (for debugging or introspection), use:"""

from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name):
    return f"Hello, {name}"

print(greet("Harshil"))



# from functools import wraps
"""- This is a built-in module of Python.
- The job of `wraps` is: when you wrap a function (such as `greet`), it preserves its **original name, docstring, and metadata**.
- Without `@wraps`, `greet.__name__` becomes `'wrapper'`, which is misleading."""


#@wraps(func)
# def wrapper(*args, **kwargs):
#     print(f"Calling {func.__name__}")
#     return func(*args, **kwargs) 

"""- `wrapper` is an **inner function** that wraps the original function.
- `*args, **kwargs` ensures that it can handle **any kind of arguments** — be it positional or keyword.
- `print(f"Calling {func.__name__}")` — It logs which function is being called.
- `return func(*args, **kwargs)` — It calls the original function and returns its result.

> Think of it like an Express.js middleware: request comes in, first logged, then actual handler runs."""




# ✅ Why @wraps Is Important

# 1.Without @wraps, agar tu greet.__name__ check kare:
# print(greet.__name__)  # Without wraps → 'wrapper'

# 2.With @wraps, tu original metadata preserve karta hai:
# print(greet.__name__)  # With wraps → 'greet'
# It is important for debugging, introspection and documentation.