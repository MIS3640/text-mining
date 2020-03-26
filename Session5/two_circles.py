import turtle
from turtle_shape import arc, circle, move, polygon

def draw_two_circles(t): 
    """
    draws two circles. t is a turtle
    """
    # large circle 
    circle(t, 100)
    move(t, 100, 0)

    #another large circle 
    circle(t, 100)

    def main(): 
        t = turtle.Turtle()
        t.speed(0)
        draw_two_circles(t)
        turtle.screen().mainloop()

    if __name__=="__main__":
        main()
