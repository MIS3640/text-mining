# Exercise 1

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'

# for letters in prefixes:
#     if letters == "O" or letters == "Q": 
#         print(letters + "u" + suffix)
#     else: 
#         print(letters + suffix)


# Exercise 2



# def count(x, a): 
#     count = 0
#     for letter in x: 
#         if letter == a: 
#             count = count + 1
#     print(count)

# count('portapotty', 'p')

# Exercise 3

# Exercise 4

print(ord('a') - 96)

groceryItem = input()


for letter in groceryItem: 
    price = ord(letter) - 96

def price(str): 
    price = 0
    for i in range(len(str)): 
        price += ord(str[i]) - 96
    return price 

def receipt(*item): 
    longest = max(len(x) for x in item)
    total = 0
    for i in range(len(item)): 
        total += price(item[i])
        print(f'{item[i]:{8+longest}s}${price(item[i]):>7.2f}')
        space = " "
    return f"-"*(15 + longest) + f'\n' + f"Total {space*(2 + longest)}${total:>7.2f}"

print(receipt('banana', 'rice', 'paprika', "potato chips"))

# Exercise 5
# 1. Return True for any lower cases
# 2. Return the string "true" for lower and "false" for upper
# 3. Return False for upper and True for lower  
# 4. Opposite of 3
# 5. Return True unless it's upper case

# Exercise 6

# def rotate_word(str, int): 
#     for i in str: 
#        new_letters = chr(ord(i) + int) 
#        print(new_letters)

# rotate_word('hal', 1)

# print(2**38)
