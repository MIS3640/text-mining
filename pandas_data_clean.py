#### create dataframe using pandas to organize dictionary #####
import pandas as pd
df = pd.DataFrame(list(reloaded_review_text.items()),columns = ['user','reviews']) 
# print (df)
# print (type(df))

import re
import string

def clean_text_round1(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    for k,v in reloaded_review_text.items():
        text = text.lower() # Make text lowercase
        text = re.sub('\[.*?\]', '', text) # remove text in square brackets
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text) # remove punctuation 
        text = re.sub('\w*\d\w*', '', text) # remove words containing numbers
    return text

round1 = lambda x: clean_text_round1(x)

data_clean = pd.DataFrame(df.reviews.apply(round1))
# print(data_clean)

def clean_text_round2(text):
    '''Get rid of some additional punctuation and non-sensical 
    text that was missed the first time around.'''
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    return text

round2 = lambda x: clean_text_round2(x)
data_clean = pd.DataFrame(data_clean.reviews.apply(round2))
print(data_clean)

new_dict = data_clean.to_dict() # converts dataframe back to dictionary
pprint.pprint(new_dict)
print(type(new_dict))