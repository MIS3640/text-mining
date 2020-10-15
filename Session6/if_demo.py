# age = int(input('How old are you?'))

# if age >= 18: 
#     print(f'Your age is {age}.')
#     print('You are an adult')
# elif age >= 12: 
#     print('You are a teenager')
# else: 
#     print('Kid')


# x = 1
# y = 2


# if x == y: 
#     print('x and y are equal.')
# else: 
#     if x < y:
#         print('x < y')
#     else: 
#         print('y < x')

# import webbrowser

# def bmi_calc(weight, height):
#     bmi = 703 * weight / (height * height)

#     if bmi <= 18.5: 
#         print('Underweight!')
#         webbrowser.open('www.google.com')
#     elif bmi <= 24.9:
#         print('Normal')
#     elif bmi <= 29.9:
#         print('Overweight')
#     else: 
#         print('Obese')

# def compare(a,b): 
#     """
#     Compares a and b
#     """
#     if isinstance(a, str) or isinstance(b, str):
#         print('string involved')
#     else: 
#         if a > b: 
#             print('Bigger')
#         elif a == b: 
#             print('equal')
#         else: 
#             print('smaller')

# compare('1', 2)
# compare(1, 2)
# compare(1, 1)




# def diff21(n):
#     """
# Given an int n, return the absolute difference between n and 21, 
# except return double the absolute difference if n is over 21.
# """
#     # if n-21 <= 21
#     #     return 21 - n
#     # else: 
#     #     return (n-21)*2


# def cigar_party(cigars, is_weekend):
#     """
#     When squirrels get together for a party, they like to have cigars. 
#     A squirrel party is successful when the number of cigars is between 40 and 60, 
#     inclusive. Unless it is the weekend, in which case there is no upper bound on 
#     the number of cigars. Return True if the party with the given values is successful, 
#     or False otherwise.
#     """
  
# if is_weekend == true: 
#     if cigars >= 60:
#         print('Success')
#     if cigars <= 40: 
#         print('Failure')

# if is_weekend == false:
#     if cigars <= 60 and cigars >= 40: 
#         print('Success')
#     else: 
#         print('Failure')

# cigar_part(40, false)


def countdown(n): 
    import time
    time.sleep(1)

    if n<= 0: 
        print("blastoff!")
    else: 
        print(n)
        countdown(n-1)
    
# countdown(5)

def fibonacci(n):
    """
    return the nth fibonacci number
    """
    if n == 1 or n ==2:
        return 1
    else: 
        return fibonacci(n - 2) + fibonacci(n - 1) 





print(fibonacci(1))
#1
print(fibonacci(2))
#1
print(fibonacci(3))
#2
print(fibonacci(7))
#13