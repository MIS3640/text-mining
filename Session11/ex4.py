def read_store_key(): 
    f = open('session9\words.txt')
    words = dict()
    words = f.read().split()
    return words


def has_duplicates(dict): 
    for i in dict: 
        count = 0
        if i not in dict: 
            count = count
        else: 
            count += 1 
    if count >= 1: 
        return True 
    else: 
        return False 



has_duplicates(read_store_key())




