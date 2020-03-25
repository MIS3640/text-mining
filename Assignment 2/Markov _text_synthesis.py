import numpy as np

walden = open('Assignment 2/Walden.txt', encoding='utf8').read()

#Split text file into single words (keeping all the punctuation)
corpus = walden.split()

def make_pairs(corpus):
    '''
    Return all the pairs of words in the Walden.
    '''
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
        
pairs = make_pairs(corpus)

#Dictionary: if the first word of the pair is already a key in the dictionary, then append the next word; 
#Otherwise, initialize a new entry in the dictionary
word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]
 
#Randomize first word
first_word = np.random.choice(corpus)

while first_word.islower():
    first_word = np.random.choice(corpus)

chain = [first_word]

n_words = 100

#Randomize every word in the chain
for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

print(' '.join(chain))

