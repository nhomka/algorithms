import turtle
import random

def tree(branch_len, t):
    if branch_len > 20:
        t.width(t.width()-1)
        t.pencolor(t.pencolor()[0]-(5./255), t.pencolor()[1]+(30./255), t.pencolor()[2])
        t.forward(branch_len)
        r_angle = random.randrange(10,26)
        r_len = random.randrange(10, 21)
        t.right(r_angle)
        tree(branch_len - r_len, t)
        l_angle = random.randrange(32,53)
        l_len = random.randrange(10, 21)
        t.left(l_angle)
        tree(branch_len - l_len, t)
        t.right(l_angle-r_angle)
        t.backward(branch_len)
        t.width(t.width()+1)
        t.pencolor(t.pencolor()[0]+(5./255), t.pencolor()[1]-(30./255), t.pencolor()[2])

def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    starting_size = 100
    t.width(starting_size/15)
    t.pencolor(82./255, 58./255, 37./255)
    t.left(90)
    t.up()
    t.backward(120)
    t.down()
    tree(75, t)
    my_win.exitonclick()

main()
