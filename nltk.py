from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentence = 'Software Design is my favorite class because learning Python is so cool!'
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)