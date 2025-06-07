hello = "hello"
print(hello[-1])
print("hello"[0])
print(123_456_789)
h1 = str(12345)
print(len(h1))
print(type(h1))
print(type(1234))
print(type(123.8))
print(type(True))

print("Number of letters in your name: "+ str(len(input("Enter Your name"))))
print("Number of letters in your name: ", len(input("Enter Your name")))

# implicit type casting , it is a python default behaviour
print(6/3)
print(type(6/3))
print(6//3)


# PEMDASLR
print(3*3+3/3-3)
print(3/3*3+3-3)
print(84/(1.65*1.65))

bmi = 84/1.65**2
# And this is a programming term for basically just removing all of the remaining decimal places, flooring
# it to the lowest whole number.
print(int(bmi))

# Whereas rounding we'll round up or down one whole number depending on the first decimal place.
print(round(bmi))

# And now when I hit Run, you'll see that this time, instead of simply rounding it to a whole number,
# it rounds it to a floating point number with two decimal places of accuracy.
print(round(bmi,2))


score =0
height=1.8
is_winning=True
# *So all of these different data types got combined into a string by using an f in front of the string,
# and then using these curly braces to place our variables into the string.
# By using f-strings, you cut down on a lot of the manual labor of inserting different data types into
# a string,
print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")

# syntax: template.formate(p1,p2,p3,...,k1=v1,k2=v2)

# template is a string containing format codes, format() method uses it's argument to substitute value for each format codes. For e.g:

# >>> 'Sam has {0} red balls and {1} yellow balls'.format(12, 31)
# {0} and {1} are format codes. The format code {0} is replaced by the first argument of format() i.e 12, while {1} is replaced by the second argument of format() i.e 31.

# This technique is okay for simple formatting but what if you want to specify precision in floating point number? For such thing you need to learn more about format codes. Here is the full syntax of format codes.

# Syntax: {[argument_index_or_keyword]:[width][.precision][type]}
print("Sam has {0} red balls and {1} yellow balls".format(12,31))
# You need to specify precision only in case of floating point numbers if you specify precision for integer ValueError will be raised.
# print("Sam has {0:.2d} red balls and {1} yellow balls".format(12,31))

k = "{:.2f}".format(bmi)
# And this is basically turned this h1,which is a float into string.And that string is abiding bt this particular format, which is the two decimal places.
print(k)
print(type(k))