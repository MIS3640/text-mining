# def my_func(*args):
#     return sum(args)

f = open('Session12/deutsch.txt')

words = f.read() 
words = words.lower() 
twords = tuple(words)


# letters = list()
# for i in words: 
#     if i.isalpha() == True: 
#         letters.append(i)
# print(i)

#ex 2

def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary

def most_frequent(s): 
    letters = [letter.lower() for letter in f if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []

    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)

    for count, letter in result:
        print (letter, count)
    
print(most_frequent(twords))

from collections import defaultdict

with open('Session12/deutsch.txt') as fd:
    words = fd.read().splitlines()





def make_anagram_dict(word_list):

    result = defaultdict(list)
    for word in word_list:
        fp = ''.join(sorted(word))
        result[fp].append(word)

    result = {fp: result[fp] for fp in result if len(result[fp]) > 1}
    return result


anagrams = make_anagram_dict(words)

def longest_anagrams(anagrams):
    anagrams_lists = []
    for fp in anagrams:
        anagrams_lists.append(anagrams[fp])
    anagrams_lists.sort(key=len, reverse=True)

    print(longest_anagrams(anagrams))

    for i in range(0, 5):
        print % ((i + 1), len(anagrams_lists[i])), anagrams_lists[i]
  
longest_anagrams(anagrams)