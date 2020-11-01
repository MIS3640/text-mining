import praw
import time
#import all variables from config file 
from config import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def login():
    '''Login to redit using user credentials and return the user object'''
    r = praw.Reddit(user_agent = user_agent, username = username, password = password, client_id = client_id, client_secret = client_secret)
    return r

def getNewestSellingPost(name, r):
    '''get the nine newest listing on the subreddit r/mechmarket and return a list containing their id's'''
    sub = name
    posts = []
    i=0
    #only get the first 9 listings
    for submission in r.subreddit("mechmarket").new():
        posts.append(submission)
        i+=1
        if i > 10:
            break
    newPosts = posts.copy()
    #print(len(posts))
    #filter posts only under the selling tab  #filter posts only under the selling tab 
    for z in range(len(posts)-1):
        #print(z)
        subs = r.submission(id=posts[z])
        if subs.link_flair_text != 'Selling':
            #remove it from the list of posts
            newPosts.remove(posts[z])
    #return posts that are actually sellling stuff
    return newPosts
    
def itemDictionaryWithPrice():
    '''return the dictionary containing the items I am interested in purchasing'''
    #glorious pandas are a mid tier mechanica keyboard case whereas the tofu 60 is a relatively high end mechanical kehyboard case and plate
    dic = {'Glorious Pandas': '$80', 'Tofu60': '$200'}
    return dic


def searchPostsForItems(dic, posts, r):
    '''create a dictionary to contain post numbers and the product associated with the post. In additon, only 
    keep posts that are selling products'''
    #search the posts for the wanted items contained in the dictionary
    #this is i dictionary taht will contain post nubmers and coresponding body text for processing later
    postsWithInterest = {}
    #list of names of items
    for m in range(len(posts)):
        #iterate over every post
        sub = r.submission(id=posts[m])
        print(sub.title)
        for x in dic:
            if x in sub.title:
                #found a match for an item I am interested in the title of the post
                #add post id and post text info pairing to dictionary           
                postsWithInterest[posts[m]] = x
    return postsWithInterest 

def searchPostForPrice(postsDict, r):
    '''search through the post's text for a price value after the goods of interest'''
    dictOfInterestedItemsAndCosts = {}
    #searches a post for the price of an item
    for id in postsDict:
        #print(id)
        posts = r.submission(id=id)
        text = posts.selftext
        #print(text)
        #find nearest $ after name of interested product is found
        item = postsDict[id]
        text = posts.selftext
        locationOfProduct = text.find(item)
        money = 'notfound'
        cost = ''
        i=locationOfProduct
        while money != 'found':
            if text[i] == '$':
                #figure out cost, so keep going until you see a space
                i+=1
                while text[i] != ' ':
                    #keep iterating until end of number
                    cost = cost+text[i]
                    i+=1
                #number was found
                money = 'found'
            i+=1
        #creates dictionary storing post id and associated cost of good I am interested in
        dictOfInterestedItemsAndCosts[item] = cost
        print(cost)
    return dictOfInterestedItemsAndCosts

def determineCostBasedOnHappinessOfWriter(dictOfInterestedItemsAndCosts, dicWithInterestedPosts):
    '''determine the happiness of the poster then feed that value into the formula I created'''
    #create dictionary of post number and updated cost 
    for key in dictOfInterestedItemsAndCosts:
        text = dictOfInterestedItemsAndCosts[key]
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        #print(score)
        #arbirtary algorithm for calculating amount to low-ball by, definately needs tweaking in the future
        #currently measures current cost - (cost divided by two times positivity out of one)
        updatedCost = int(dictOfInterestedItemsAndCosts[key])-int(((int(dictOfInterestedItemsAndCosts[key])/2)*score['pos']))
        dictOfInterestedItemsAndCosts[key] = updatedCost

    return dictOfInterestedItemsAndCosts
    
def commentOnPost(text, dictOfUpdatedCosts, dictOfIds):
    '''reply to the post with your offer'''
    #reply to the comments with input text
    for post in dictOfIds:
        title = post.title
        print(title)
        message = text + '$' + str(dictOfUpdatedCosts[dictOfIds[post]]) 
        post.reply(message)

if __name__ == '__main__':
    while(True):
        r = login()
        posts = getNewestSellingPost('mechmarket', r)
        dicWithInterestedPosts = searchPostsForItems(itemDictionaryWithPrice(), posts, r)
        #input dictiionary with posts you are interested in, output dictionary with posts you are interested in with associated cost
        dictOfInterestedItemsAndCosts = searchPostForPrice(dicWithInterestedPosts, r)
        #determine the happiness of the poster to figure out how much you can undercut their price
        dictOfUpdatedCosts = determineCostBasedOnHappinessOfWriter(dictOfInterestedItemsAndCosts, dicWithInterestedPosts)
        #comment the final price on the post
        commentOnPost('Will you take: ', dictOfUpdatedCosts, dicWithInterestedPosts)
        #wait five minutes between calls
        time.sleep(60*5)


