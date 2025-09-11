# from turtle import Turtle,Screen
# timy = Turtle()


# def move_forwards():
#     timy.forward(40)
#     # timy.left(60)


# screen = Screen()

# screen.listen()
# screen.onkey(key='space',fun=move_forwards)



# screen.exitonclick()


# challenge sketch app

# ////////////////////////////////////////////


# from turtle import Turtle,Screen
# timy = Turtle()


# screen = Screen()

# def forward():
#     timy.forward(20)

# def backward():
#     timy.backward(20)

# def clockWise():
#     timy.right(20)

# def antiClockWise():
#     timy.right(-20)
# def clear():
#     timy.clear()
#     timy.penup()
#     timy.home()
#     timy.pendown()

# def sketch_app():
#     screen.listen()
#     screen.onkey(key="w",fun=forward)
#     screen.onkey(key="s",fun=backward)
#     screen.onkey(key="d",fun=clockWise)
#     screen.onkey(key="a",fun=antiClockWise)
#     screen.onkey(key="c",fun=clear)


# sketch_app()

# screen.exitonclick()

# //////////////////////////////////////
from turtle import Turtle,Screen

import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")
colors = ["red","orange","yellow","green","blue","purple"]
y_position  = [-100,-50,0,50,100,150]
all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230,y=y_position[turtle_index])
    all_turtle.append(new_turtle)



if user_bet:
    is_race_on = True

while is_race_on:
    
          
    for turtle in all_turtle:
     if turtle.xcor()>230:
       is_race_on = False
       winning_color = turtle.pencolor()
       if winning_color==user_bet:
          print(f"You've won!The {winning_color} turtle is the winner")
       else:
          print(f"You've lost!The {winning_color} turtle is the winner")
     random_distance = random.randint(0,10)
     turtle.forward(random_distance)
        
    
   









screen.exitonclick()