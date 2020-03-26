# print(range(len('andrew')))
import math 

# def factorial(n):
#     for i in range (1, n+1): 
#         print(i)
#         fact = fact * i
         
         

# print(factorial(4))

n = 4
fact = 1

for i in range(1, n+1): 
    fact = fact * i

# print(fact)



# def fib(n): 
#     return fib(n-1) + fib(n-2)

# fib(5)

# def fib(n):
#     num = fib(n-1) + fib(n-2)
#     return num

# fib(5)

def Fibonacci(n): 
    if n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 

# print(Fibonacci(9))

# def gcd(a, b): 

# def countdown(n): 
#     if n <= 0: 
#         print('Blastoff!')
#     else: 
#         print(n)
#         countdown(n-1)

# countdown(4)

def print_N(s, n):
    if n <= 0: 
        return
    print(s)
    print_N(s, n-1)

# print_N('hello', 2)

def recurse_infinite(): 
    recurse_infinite()

# recurse_infinite()

def shampoo(): 
    while 1 == 1: 
        print("Lather, rinse, repeat")

# shampoo()

def twentyplus(): 
    f = open('session12/deutsch.txt')
    for line in f: 
        word = line.strip()
        if len(word) > 20: 
            print(word)

def has_no_e(): 
    f = open('session12/deutsch.txt')
    for line in f: 
        word = line.strip()
        if 'e' not in word: 
            print(word) 

# has_no_e()

word = 'beef' 

def avoids(word, forbidden): 
    f = open('session12/deutsch.txt')
    for line in f: 
        word = line.strip()
        for letter in word: 
            if letter in forbidden:  
                return False
        return True

# print(avoids(word, 'agd'))

def is_abcedarian(word): 
    previous = word[0]
    for c in word: 
        if c < previous: 
            return False 
        previous = c
    return True 

def is_abcedarian(word): 
    if len(word) <= 1:
        return True
    if word[0] > word[1]: 
        return False 
    return is_abcedarian(word[1:])



cheeses = ['cheddar', 'edam', 'gouda']

for cheese in cheeses: 
    print(cheese)

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)
