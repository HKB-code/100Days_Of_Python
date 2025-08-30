# Please activate the venv file,  .\venv\Scripts\activate

import colorgram
import turtle
import random

# Step 1: Extract colors from an image
colors = colorgram.extract("./image.jpg", 30)  # Extract top 30 colors

# Step 2: Convert to RGB tuples
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

# Step 3: Setup turtle
turtle.colormode(255)
tim = turtle.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# Step 4: Draw a grid of dots
dot_count = 100
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot in range(1, dot_count + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# Step 5: Exit on click
screen = turtle.Screen()
screen.exitonclick()


# import colorgram
# import turtle
# import random


# # extract color
# colors= colorgram.extract("./image.jpg",30)

# # tuples
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))


# # 
# turtle.colormode(255)
# tim = turtle.Turtle()
# tim.speed("fastest")
# # tim.penup()
# tim.hideturtle()


# dot_count = 100

# for i in range(dot_count):
#     tim.dot(5, random.choice(rgb_colors))
#     tim.forward(10+i*4)
#     tim.right(90)

# # Step 5: Exit on click
# screen = turtle.Screen()
# screen.exitonclick()
