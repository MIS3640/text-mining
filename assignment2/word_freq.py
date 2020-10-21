# Frequency of Words in a Data.

def clean(text):
    """
    Cleans inputed string by removing symbols, numbers and making all letters lowercase so just words remain in the string. Also, convert the string into dictionary and store each word's frequency in the dictionary.
    """
    # remove symbols
    symbols = '''=!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_symbols = ""

    for word in text:
        if word not in symbols:
            no_symbols = no_symbols + word

    # make all lowercase
    lowered = no_symbols.lower() 

    # find frequency of each words
    words = lowered.split()
    d = dict()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    dic = d

    # remove numbers in the dictionary
    dictionary = dict()
    for key, value in dic.items():
        if key.isnumeric() == False:
            dictionary[key] = value
    return dictionary

def word_freq(text, s):
    count = 0
    lowered = text.lower()
    s_low = s.lower()
    words = lowered.split()

    for word in words:
        if word == s_low:
            count += 1

    return count

def top_10_most_freq(dic):
    """
    This function prints the top 10 most frequent words and its frequency in numbers in a inputed dictionary.
    """
    d = dict()
    y = sorted(dic.keys(), key=lambda k: dic[k], reverse=True) #list most freq to least
    for k in y:
        d[k] = dic[k]

    d_items = d.items()
    top_10 = list(d_items)[:10]
    
    for key, value in top_10:
        print(f'{key}: {value}')
