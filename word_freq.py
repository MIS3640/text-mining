def remove_symbols(text):
    symbols = '''=!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_symbols = ""

    for word in text:
        if word not in symbols:
            no_symbols = no_symbols + word
    return no_symbols

def make_lowercase(text):
    return text.lower()

def word_freq(text, s):
    count = 0
    words = text.split()

    for word in words:
        if word == s:
            count += 1

    return count

def freq(text):

    words = text.split()
    d = dict()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def remove_numbers(dic):
    d = dict()
    for key, value in dic.items():
        if key.isnumeric() == False:
            d[key] = value
    return d

def most_freq(dic):
    d = dict()
    y = sorted(dic.keys(), key=lambda k: dic[k], reverse=True) #list most freq to least
    for k in y:
        d[k] = dic[k]
    return d

def top_10_most_freq(dic):
    dic_items = dic.items()
    top_10 = list(dic_items)[:10]
    
    for key, value in top_10:
        print(f'{key}: {value}')
