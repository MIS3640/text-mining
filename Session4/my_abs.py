# def my_abs(W):
#     print(abs(W))


# my_abs(-8)

# def my_abs(n):
#     if n < 0: 
#         n = -n
#         print(n)
#     else: 
#         print(n)

# my_abs(-1)
# my_abs(1)
# my_abs(0)


# def cat_twice(part1, part2):
#     cat = part1 + part2
#     print_twice(cat)

# cat_twice('Babson', 'College') 

# print_twice('s')


# def give_me_a_break():
#     str1 = 'break'
#     return str1

# # give_me_a_break()
# print(give_me_a_break())

# def give_me_two_breaks():
#     str1 = 'break'
#     return str1
#     print('another break')

# print(give_me_two_breaks())

# def print_lyrics():
#     print('HI')
#     print('HELLO')
 
# print_lyrics()

# def print_twice(a):
#     print(a)
#     print(a)

# # print_twice('b')

# def cat_twice(part1, part2):
#     cat = part1 + part2
#     print_twice(cat)



# cat_twice(1, 2)

# def give_me_a_break():
#         str1 = 'break'
#         return str1
#         print('another break')

    
# print(give_me_a_break())

# result = print_twice('Bing')

# print(result)

# def nop():
#     pass

# age= int(input())
# if age >= 18: 
#     pass

def my_abs(number): 
    
    """
    number: an integer or a floating number
    return the absolute value of a number
    """

    if isinstance(number, int) or isinstance(number, float): 
        if number >= 0:
            return number 
        else: 
            return -number
    else: 
            return 'I don\'t know'

print(my_abs(-4.2))







