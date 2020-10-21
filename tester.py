from imdbpie import Imdb
import pprint
import pickle
import matplotlib.pyplot as plt

# main Program

movieName = "The Fault In Our Stars"
author = [] # List to store all author names for a review
wordCnt = [] # A List to store count of the reviewText 
imdb = Imdb() 
movieDict =  imdb.search_for_title(movieName)[0] # closest match is the first index
id = movieDict['imdb_id']
reviews = imdb.get_title_user_reviews(id)
allReviews = reviews['reviews'] # get the reviews into a dictionary


def countWords():
    for R in allReviews: # Loop to traverse through each Review
        #print (R['author']['displayName'],R['reviewText']) # to debug
        author.append(R['author']['displayName']) # author has display name and author ID
        wordCnt.append( len (R['reviewText']) ) 
    
def countFrequency():
    wordstring=""
    stopWords = ["this","the", "to", "time","on","a","not","is","I","we","they","he","are","an","was","and","here","there","that","where","why","don't","in","you","she","of","it","by","be","as","about"]
    
    # Join all the reviews together and make it as one text first
    for R in allReviews: 
        wordstring +=  R['reviewText']
    
    wordlist = wordstring.split() # change that text to a list of values , space as terminator

    # remove the stop words from the list
    for s in stopWords:
        try:
	        while True:
		        wordlist.remove(s)
        except ValueError:
	        pass
    
    wordfreq = []
    for w in wordlist:
        wordfreq.append(wordlist.count(w))

    # print("String\n" + wordstring +"\n")
    # print("List\n" + str(wordlist) + "\n")
    # print("Frequencies\n" + str(wordfreq) + "\n")
    finalList = list(zip(wordlist, wordfreq))
    
    finalSet = set(finalList); # only take unique values
    finalList = list(finalSet)
    # sorted the list
    for i in range (len(finalList)):
        for j in range (i+1, len(finalList)):
            if finalList[i][1] < finalList[j][1]:
                temp = finalList[i]
                finalList[i] = finalList[j]
                finalList[j] = temp
    print(finalList)

def authorGraph():
    """plot a graph to show visually the number of words"""
    fig = plt.figure(figsize=(9,7))
    plt.plot(author, wordCnt, color='green', linewidth=3)
    plt.xticks(rotation=45)
    plt.xlabel('Authors')
    plt.ylabel('Review Text Count')
    plt.title('Count of Review Text By Each Author')
    plt.show()



# word count of ReviewText & graph
countWords()
authorGraph()
countFrequency()

