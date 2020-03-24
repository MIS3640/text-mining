from random import randint

def makeDict(text):
    """
    text: a string
    """
    words = text.split()
    wordict = {}

    for i in range(1, len(words)):
        if words[i-1] not in wordict:
            wordict[words[i-1]] = {}
        if words[i] not in wordict[words[i-1]]:
            wordict[words[i-1]][words[i]] = 0
        wordict[words[i-1]][words[i]] += 1

    return wordict

def wordLen(wordict):
     sum = 0
     for value in wordict.values():
         sum += value
     return sum

def retriveRandomWord(wordict):
    randindex = randint(1, wordLen(wordict))
    for key, value in wordict.items():
        randindex -= value
        if randindex <= 0:
            return key

def markov(filename, length, currentword):
    f = open(filename,'r')
    t = str(f.read())
    wordict = makeDict(t)

    chain = ''

    for i in range(0, length):
        chain += currentword + ' '
        currentword = retriveRandomWord(wordict[currentword])
        
    return chain

def main():
    length = 200
    currentword = 'tom'
    chain = markov('Mark Twain/Mark Twain.txt', length, currentword)

    print(chain)

    # f = open("new book.txt",'w')
    # f.write(chain)
    # f.close()


if __name__ == "__main__":
    main()
