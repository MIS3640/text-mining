from twython import Twython
import pickle

TOKEN = '1915967478-7AZ8k90eXWueq2h0kNMo48P7J79M9RMO4N1IgqW'
TOKEN_SECRET = 'EJkwgo0qGumc3NLtBLrJEuALz0yUnNZZFvDZNTVRNPR3w'
CONSUMER_KEY = 'REUfo4IgkLZPFFAOqnb8rJkhf'
CONSUMER_SECRET = 'RCLFC1tNjhfRHE1lxVLC7p1FQNfLj25RP5TsGzUWx1ZOu550cT'

t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
TOKEN, TOKEN_SECRET)

data = t.search(q="Coronavirus", count=280)

for status in data['statuses']:
    print(status['text'])
    # print(len(data['statuses']))

# Save data to a pickle named 'tweets' (will be part of your data fetching script)
with open('tweets.p','wb') as p:
    pickle.dump(data, p)
