import nltk
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
with open('saved_texts.pickle','rb') as input_file:
    Wuthering_Height = pickle.load(input_file)
    Jane_Eyre = pickle.load(input_file)
score1 = SentimentIntensityAnalyzer().polarity_scores(Wuthering_Height)
score2 = SentimentIntensityAnalyzer().polarity_scores(Jane_Eyre)
print(score1)
print(score2)

