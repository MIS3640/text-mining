import nltk
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
with open('saved_texts.pickle','rb') as input_file:
    The_Modest_Proposal = pickle.load(input_file)
    Time_Machine = pickle.load(input_file)
score1 = SentimentIntensityAnalyzer().polarity_scores(The_Modest_Proposal)
score2 = SentimentIntensityAnalyzer().polarity_scores(Time_Machine)
print(score1)
print(score2)

