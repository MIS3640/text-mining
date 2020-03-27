import pickle
import string

with open('tweets.p', 'rb') as p:
    t = pickle.load(p)

# unloading the pickled data into a list
tweet_text = [] 
for tweet in t['statuses']:
    tweet_text.append(tweet['text'])
# print(tweet_text)

def convert_to_single_words(tweet_text):
    """
    Function converts sentences from tweet_text list into each word as its own string
    """
    return ' '.join(tweet_text).split()
new_tweet_text = (convert_to_single_words(tweet_text))
print(new_tweet_text)

# Writing the new_tweet_text list into a text file 
new_file = open('tweets.txt', 'w', encoding='utf-8')
for element in new_tweet_text:
    new_file.write(element)
    new_file.write('\n')
# new_file.writelines(new_tweet_text, '\n')
new_file.close()

# hist = {}
# for word in new_tweet_text:
#     hist[word] = hist.get(word, 0) + 1
# print(hist)
    
