"""So essentially, an object is just a way of combining some piece of data and some
 functionality altogether in the same thing.
"""
from turtle import Turtle,Screen
"""The turtle module in Python is a great way to introduce graphics programming. It provides a drawing canvas and turtle (a pen) that you can control to draw shapes and patterns."""

# timy =Turtle()
# print(timy)
# timy.shape('turtle')
# timy.color("red")
# timy.forward(200)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

"""Now we've seen modules of code where each file that we create in our project is essentially a module

in itself,

but a package differs from a module in the sense that it's actually a whole bunch of code that other

people have written. Lots and lots of files, all packaged together to achieve some sort of goal or purpose.
  """
from prettytable import PrettyTable
table = PrettyTable()
print(table)
table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table)
table.align = "l"

print(table)
