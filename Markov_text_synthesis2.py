from random import randint

def makeDict(text):
    #替换换行符和引号
    text = text.replace('\n', ' ')
    text = text.replace('\“', '')
    text = text.replace('\”', '')

    punc = ['，', '。', '？', '；', ':', '!']
    for symbol in punc:
        text = text.replace(symbol, ' '+symbol+' ')

    words = [word for word in text if word != '']

    wordict = {}
    for i in range(1, len(text)):
        if words[i-1] not in wordict:
            wordict[words[i-1]] = {}
        if words[i] not in wordict[words[i-1]]:
            wordict[words[i-1]][words[i]] = 0
        wordict[words[i-1]][words[i]] += 1

    return wordict


def wordLen(wordict):
    sum = 0
    for key, value in wordict.items():
        sum += value
    return sum


def retriveRandomWord(wordict):
    """
    感觉这个函数计算每个单词的机率的思路太帅了
    :param wordict:
    :return:
    """
    randindex = randint(1, wordLen(wordict))
    for key, value in wordict.items():
        randindex -= value
        if randindex <= 0:
            return key

with open('Assignment 2/Walden.txt','r') as f:
    t = f.read()
text = str(t)
wordict = makeDict(text)

length = 200
chain = ''
currentword = 'I'
for i in range(0, length):
    chain += currentword
    currentword = retriveRandomWord(wordict[currentword])

with open("Assignment 2/Walden.txt",'w') as file:
    file.write(chain)
print(chain)