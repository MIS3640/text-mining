import math 
# def move(x, y, step, angle):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)


def quadratic(a, b, c): 
    x1 = (-b + math.sqrt(b**2 - 5*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 5*a*c))/(2*a)
    print(x1, x2)

a= 3
b= 4
c= 5

quadratic(a, b, c)



