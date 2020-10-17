from twython import Twython
from config import TOKEN_SECRET_HIDDEN 
from config import CONSUMER_SECRET_HIDDEN

# Replace the following strings with your own keys and secrets
TOKEN = '1308753867992170498-y2tPq70sOhS9VxNeRhnuO4wW6cIdXH'
TOKEN_SECRET = TOKEN_SECRET_HIDDEN
CONSUMER_KEY = 'AmSWYiODOWhTIWLo7R09nh3sJ'
CONSUMER_SECRET = CONSUMER_SECRET_HIDDEN


t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
   TOKEN, TOKEN_SECRET)

data = t.search(q="Hello", count=2)


for status in data['statuses']:
    print(status['text'])