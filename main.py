


# from turtle import * (전체 임포트지만 웬만하면 지양)

##하나만 사용할때
# import turtle
# tim = turtle.Turtle()

# import turtle as t
# tim = t.Turtle()

# import heroes
# print(heroes.gen())


from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("orange")


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)


# for _ in range(20):
#     timmy.forward(10)
#     timmy.penup() #color("white")
#     timmy.forward(10)
#     timmy.pendown() #color("black")

#
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)














screen = Screen()
screen.exitonclick()



