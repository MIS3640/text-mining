from twython import Twython
from config import TOKEN_SECRET_HIDDEN 
from config import CONSUMER_SECRET_HIDDEN
import pickle

# Replace the following strings with your own keys and secrets
TOKEN = '1308753867992170498-y2tPq70sOhS9VxNeRhnuO4wW6cIdXH'
TOKEN_SECRET = TOKEN_SECRET_HIDDEN
CONSUMER_KEY = 'AmSWYiODOWhTIWLo7R09nh3sJ'
CONSUMER_SECRET = CONSUMER_SECRET_HIDDEN


t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
   TOKEN, TOKEN_SECRET)

data = t.search(q="Hello", count=2)

# Save data to a file (will be part of your data fetching script)
with open('', 'w') as f:
   pickle.dump(,f)

# Print fetched tweets
for status in data['statuses']:
    print(status['text'])