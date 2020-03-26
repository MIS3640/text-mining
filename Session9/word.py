# f = open('session9/words.txt') 
# line = f.readline()
# print(line)

# f = open('session9/words.txt')
# number_of_words = 0

# for line in f: 
#     word = line.strip()
#     number_of_words += 1

# print(number_of_words)
    
# f = open('session9/words.txt')
# line = f.readline()

def find_long_words():
    """
    prints only the words with more than 20 characters
    """
    f = open('session9/words.txt')
    
    for line in f: 
        word = line.strip()
        if len(word) > 20: 
            print(word) 
        

# find_long_words()


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter "e" in it
    """
    # for c in word: 
    #     if c.lower() == 'e': 
    #         return False 
    
    # return True

    return not 'e' in word.lower()

# print(has_no_e('Babson'))
# print(has_no_e('College'))
# print(has_no_e('EA sports'))


def find_words_no_e():
    """
    returns the percentage of the words that don't have the letter "e"
    """
    f = open('session9/words.txt') 
    num_no_e = 0
    num_words = 0
    for line in f: 
        num_words += 1
        word = line.strip()
        if has_no_e(word): 
            num_no_e += 1
    print(num_no_e, num_words)
    return num_no_e/num_words


# perc_no_e = find_words_no_e()
# print(f'The percentage of the words with no "e" is {perc_no_e*100:.2f}%.')


def avoids(word, forbidden):
    """
    returns True if the given word does not use any of the forbidden letters
    """
    for letter in word: 
        if letter in forbidden: 
            return False 
    return True 


# print(avoids('Babson', 'abcde'))
# print(avoids('College', 'e'))
# print(avoids('Boston', 'xyz'))


def find_words_no_vowels():
    """
    returns the percentage of the words that don't vowel letters
    """
    f = open('session9/words.txt') 
    num_no_vowels = 0
    num_words = 0
    for line in f: 
        num_words += 1
        word = line.strip()
        if avoids(word, 'aeiou'): 
            num_no_vowels += 1
    print(num_no_vowels, num_words)
    return num_no_vowels/num_words


# perc_no_vowel = find_words_no_vowels()
# print(f'The percentage of the words without vowel letters is {perc_no_vowel*100:.2f}%.')


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the string available. 
    """
    for letter in word: 
        if letter not in available: 
            return False 
    return True 


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


def find_words_only_use_planet():
    f = open('session9/words.txt')
    
    num_words_only_use_planet = 0
    for line in f: 
        word = line.strip()
        if uses_only(word, 'planets'): 
            print(word)
            num_words_only_use_planet += 1
    return num_words_only_use_planet


# print('Number of words that use only letters from "planet" is', find_words_only_use_planet())


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for letter in word:
        for reqletter in required:  
            while reqletter in letter and reqletter == letter: 
                return True
            else: 
                return False 
    

# print(uses_all('apple', 'ape'))
# print(uses_all('apple', 'ac'))


def find_words_using_all_vowels():
    """
    return the number of the words that use all the vowel letters
    """
    f = open('session9/words.txt')
    num_words_only_use_all_vowels = 0

    for line in f: 
        word = line.strip()
        if uses_only(word, 'aeiou'): 
            print(word)
            num_words_only_use_all_vowels += 1
    return num_words_only_use_all_vowels

# print('The number of words that use all the vowels:', find_words_using_all_vowels())


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True



# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))


def find_abecedarian_words(word):
    """
    returns the number of abecedarian words
    """
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True


# print(find_abecedarian_words())


def is_abecedarian_using_recursion(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    # previous = word[0]
    # for c in word:
    #     if c < previous:
    #         return False
    #     previous = c
    # return True


# print(is_abecedarian_using_recursion('abcdef'))


def is_abecedarian_using_while(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    # previous = word[0]
    # for c in word:
    #     if c < previous:
    #         return False
    #     previous = c
    # return True


#exercise 3

def is_triple_double(word):
    """return True if the word contains three consecutive
    double letters."""
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False

def find_triple_double():
    f = open('session9/words.txt')

    for line in f:
        word = line.strip()
        if is_triple_double(word):
            print(word)

# find_triple_double()

