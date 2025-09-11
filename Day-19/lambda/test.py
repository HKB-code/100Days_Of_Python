"""🧠 What Is a lambda Function?
A lambda function is a small, anonymous function defined using the lambda keyword. It’s designed for one-off, short-lived operations where defining a full function with def would be overkill.
"""

# 🔍 Syntax
# lambda arguments: expression


# - Arguments: Like any function, you can pass multiple inputs.
# - Expression: Must be a single expression (no statements, loops, or assignments).
# - Return: Implicitly returns the result of the expression.



# ⚖️ lambda vs def

# 1.Lambda:-
# Name : Anonymous(unless assigned)
# Body: Single expression only
# Docstring: Not supported
# Use Case : Short-lived, inline logic
# Readability: Concise but cryptic if overused

# 2.Regular Function(def):-
# Name: Named
# Body: Multiple statements allowed
# Docstrings: Supported
# Use Case: Reusable, complex logic
# Readability: Clear and maintainable


# 🔧 Practical Use Cases

# 1.1. Quick Transformations with map()
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))  # [1, 4, 9, 16]

# 2.2. Filtering with filter()
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]


# 3. Custom Sorting with sorted()
names = ["Peter", "Shah", "Neha"]
sorted_names = sorted(names, key=lambda name: name.split()[-1])

# 4.Conditional Logic

check_sign = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check_sign(-5))  # Negative

# Example:-
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
print(double(10))  # Output: 20

"""🔍 What’s Happening?
- multiplier(n) returns a lambda function that multiplies its input x by n.
- double = multiplier(2) creates a function lambda x: x * 2
- double(10) → 10 * 2 → 20
This is a classic example of a closure—the returned lambda retains access to n even after multiplier has finished executing
"""



# 🧠 Advanced Insight: Closures & Scope
# Python’s lambdas can capture variables from their enclosing scope, which makes them useful for creating dynamic behavior.

functions = []
for i in range(3):
    functions.append(lambda x, i=i: x + i)

for f in functions:
    print(f(10))  # Outputs: 10, 11, 12

# Notice the i=i trick—it ensures each lambda captures the current value of i, not the final one


#  Backend Analogy
# Think of a lambda as a one-line middleware: it intercepts data, transforms it, and passes it along—no setup, no teardown, just pure function.


"""✅ When to Use lambda
- Inline transformations (e.g., sorting, mapping)
- Short-lived callbacks
- Functional-style pipelines
- Closures for dynamic behavior
🚫 When to Avoid
- Complex logic
- Reusability
- Debugging-heavy scenarios
"""