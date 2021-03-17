from sklearn.feature_extraction.text import TfidfVectorizer
import string
import pickle
import nltk
nltk.download('punkt')
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

def cosine_sim_toarray(documents): #return toarray
    tfidf = vectorizer.fit_transform(documents)
    
    return (tfidf * tfidf.T).toarray()

def cosine_sim(documents): #return possibility of similarity
    tfidf = vectorizer.fit_transform(documents)
    return ((tfidf * tfidf.T).A)[0,1]
 

documents = [a, b, c, d, e]

import numpy as np
import matplotlib
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# these are the similarities computed from the previous section
S = np.asarray([[1., 0.82212268, 0.87105148, 0.81267892, 0.89582767],
                [0.82212268, 1., 0.89358607, 0.94076155, 0.93715077],
                [0.87105148, 0.89358607, 1., 0.90638528, 0.92821412],
                [0.81267892, 0.94076155, 0.90638528, 1., 0.92599655],
                [0.89582767, 0.93715077, 0.92821412, 0.92599655, 1]])


# dissimilarity is 1 minus similarity
dissimilarities = 1 - S

# compute the embedding
coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)

plt.scatter(coord[:, 0], coord[:, 1])

# Label the points
for i in range(coord.shape[0]):
    plt.annotate(str(i), (coord[i, :]))


plt.show()
