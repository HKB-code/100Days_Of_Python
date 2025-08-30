from turtle import Turtle, Screen
import turtle as t
# timmy_the_turtle = Turtle()






# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")

# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)



# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# screen = Screen()
# screen.exitonclick()

# not a good way of code
# from turtle import *

# forward(200)

# from random import *
# print(choice([1,2,3]))

# Alias
# import turtle as t
# timy = t.Turtle()


"""Well, the reason is because turtle is a module that's packaged with the Python standard library,

and this is a small library of code which contains just the basics to get you started.

Like a core set when you buy a board game or like the basic track pieces when you buy

a set of Hot Wheels.

So you can imagine this library of code as like a family library, easily accessible,

but very small.

Now, if we wanted to access the whole world of Python modules and packages, then we need

to go to a much bigger library.

And that is, of course, the Python packages, which are hosted on the internet and we can

install into our project as and when we need them."""
# # installing modules
# import heroes
# print(heroes.gen())







# dashed line
# timy = Turtle()
# for _ in range(8):
#  timy.forward(4)
#  timy.penup()
#  timy.forward(4)
#  timy.pendown()

    


import random

# draw shapes
# timy = Turtle()
# colors = ['forest green','medium orchid','lavender','medium turquoise','deep pink', 'orange']
# def draw_shape(n):
#     angle = 360/n
#     for _ in range(n):
#         timy.forward(100)
#         timy.right(angle)

# for s in range(3,11):
#     timy.color(random.choice(colors))
#     draw_shape(s)




# random walk
# timy = Turtle()
# timy.pensize(15)
# timy.speed('fastest')
# directions = [0,90,180,270]

# for _ in range(200):
#     timy.color(random.choice(colors))
#     timy.forward(30)
#     timy.setheading(random.choice(directions))

# screen = Screen()
# screen.exitonclick()

# timy = Turtle()

t.colormode(255)

# def randomColor():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)

# timy.pensize(15)
# timy.speed('fastest')
# directions = [0,90,180,270]

# for _ in range(200):
#     timy.color(randomColor())
#     timy.forward(30)
#     timy.setheading(random.choice(directions))



# challenge
# timy = Turtle()
# def randomColor():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)

# # timy.pensize(1)
# # timy.speed('fastest')



# for i in range(100):
#     timy.color(randomColor())
#     timy.forward(10 +4*i)
#     timy.right(90)


# Spirograph
timy = Turtle()

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

timy.pensize(1)
timy.speed('fastest')


def drwa_spirograph(n):
    for _ in range(int(360/n)):
     timy.color(randomColor())
     timy.circle(100)
     timy.setheading(timy.heading()+n)



   
drwa_spirograph(5)
    


screen = Screen()
screen.exitonclick()