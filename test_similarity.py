from analyze_text import hist, hist1
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

# nltk.download('punkt') # if necessary...

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


print(cosine_sim(hist, hist1))