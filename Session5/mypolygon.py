import turtle

andrew = turtle.Turtle()

# print(andrew)

# for a in range(4): 
#     andrew.fd(100)
#     andrew.lt(90)


# andrew.fd(100)
# andrew.lt(90)
# andrew.fd(100)
# andrew.lt(90)
# andrew.fd(100)
# andrew.lt(90)
# andrew.fd(200)
# andrew.lt(90)
# andrew.fd(200)

# for i in range(3):
#     print(i)

# def square(t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)

def square(t, length): 
    for i in range(4): 
        t.fd(length)
        t.lt(90)

# square(andrew, 50)

# # def polygon(t, length, n): 
# #     angle = 360/n 
# #     for i in range(n): 
# #         t.fd(length)
# #         t.lt(angle)

# polygon(andrew, 3, 20)
import math

# def circle(t, r):
#     circumference = 2 * math.pi * r
#     length = circumference/20
#     polygon(t, length, 20)

# circle(andrew, 50)

# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle/360
#     n = int(arc_length/3) + 1
#     step_length= arc_length / n 
#     step_angle= angle / n 

#     for i in range(n): 
#         t.fd(step_length)
#         t.lt(step_angle)

# print(arc(andrew, r=50, angle=1440))

def polyline(t, n, length, angle): 
    """
    Draws n line segments with the given length and angle (in degrees) between them. t is a turtle. 
    """
    for i in range(n): 
        t.fd(length)
        t.lt(angle)

# polyline(andrew, 4, 50, 60)

def polygon(t, length, n): 
    """
    t is a turtle. draws a polygon with n sides length of length.
    """
    angle = 360/n 
    polyline(t, n, length, angle)

#polygon(andrew, 30, 7)

def arc(t, r, angle):
    """
    t is a turtle. draws arc with radius r and angle
    """
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length/3) + 1
    step_length= arc_length / n 
    step_angle= angle / n 

    polyline(t, n, step_length, step_angle)

arc(andrew, 100, 100)



def circle(t, r): 
    """
    draws circle with radius r. t is a turtle.
    """
    arc(t, r, 360)



def main(): 
    andrew = turtle.Turtle()
    circle(andrew, 150)
    
    turtle.mainloop()


# if __name__ == "__main__":
#     main()






