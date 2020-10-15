# fruit = 'banana'
# letter = fruit[0]
# len(fruit)
# print(len(fruit))

# # index = 0 
# fruit = 'banana'
# # while index < len(fruit): 
# #     letter = fruit[index]
# #     print(letter) 
# #     index = index + 1


# for letters in fruit: 
#     print(letters)

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'

# for letters in prefixes:
#     if letters == "O" or letters == "Q": 
#         print(letters + "u" + suffix)
#     else: 
#         print(letters + suffix)


    
# fruit = 'banana'
# print(fruit[:] )

# [1, 2, 3, 4]

# cheeses = ['gouda', 'ham', 'parm']

# for cheese in cheeses: 
#     print(cheese)

# t = ['a','b','c','a']
# t.sort()
# t = t.sort()
# print(t)

import random 

guessesTaken = 0

print('Hello! What is your name?')
myName= input()

number = random.randint(1, 20)
print('Well,' + myName + ', I am thinking of a number between 1 and 20.')
    

for i in range (0, 7): 
    print('Take a guess.') 
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number: 
        print('Your guess is too low.')

    if guess > number: 
        print('Your guess is too high.')
        
    if guess == number: 
        break 

if guess == number: 
    guessesTaken = str(guessesTaken)
    print('Good job,' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

    if guess != number: 
        number = str(number)
        print('Nope. The number I was thinking was ' + number)


