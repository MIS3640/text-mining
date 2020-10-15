# a = 'andrew'
# b = 'drewan'
# def is_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)


# print(is_anagram(a, b))

# def append_twice(a_list, val): 
#     """mutates arguments."""
#     a_list.append(val)
#     a_list.append(val)

def histogram(word_list): 
    d = dict()

    for word in word_list: 
        d[word] = d.get(word, 0) + 1
    
    return d 

# lyrics = ['hey', 'jude', 'don\'t', 'make', 'it', 'love']

f = open('session11/lyricslyrics.txt') 
lyrics = f.read().split().replace(',','').replace('-','')
print(lyrics)

# h = histogram(lyrics)
# print(h)

#EXERCISE
