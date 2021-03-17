from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('punkt')
import pickle
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

with open('saved_texts.pickle','rb') as input_file:
    a = pickle.load(input_file)
    b = pickle.load(input_file)
    c = pickle.load(input_file)
    d = pickle.load(input_file)
    e = pickle.load(input_file)



stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(documents):
    tfidf = vectorizer.fit_transform(documents)
    return ((tfidf * tfidf.T).A)[0,1]

documents = [a, b, c, d, e]