from collections import Counter
import sys
from unicodedata import category
def word_summary(filename):
    """this function takes away any strippables"""
    hist = {}
    fp = open(filename, encoding = 'UTF8')

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )
    for line in fp:

        line = line.replace('-', ' ').replace(chr(8212), ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


# Program to find most frequent 
# element in a list 

def most_frequent(hist): 
	counter = 0
	
	for i in hist: 
		curr_frequency = hist.count(i) 
		if(curr_frequency> counter): 
			counter = curr_frequency 
			num = i 

	return num 
    


def main():
    filename ='Iphone.txt'
    hist = word_summary('Iphone.txt')
    #print(hist)
    print(most_frequent(hist)) 



if __name__ == '__main__':
    main()