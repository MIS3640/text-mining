from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download("punkt")
import pickle
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords

# Unpickling the text files
with open("saved_texts.pickle", "rb") as input_file:
    Wuthering_Height = pickle.load(input_file)
    Jane_Eyre = pickle.load(input_file)
    Agnes_Grey = pickle.load(input_file)
    Villette = pickle.load(input_file)
    Wildfell_hall = pickle.load(input_file)


stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def stem_tokens(tokens):
    """breaking document into words and reduces words into root form"""
    return [stemmer.stem(item) for item in tokens]


def normalize(text):
    """remove punctuation, lowercase, stem"""
    return stem_tokens(
        nltk.word_tokenize(text.lower().translate(remove_punctuation_map))
    )


vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words="english")


def cosine_sim(documents):
    """
    returns the similarity between documents
    """
    tfidf = vectorizer.fit_transform(documents)
    return ((tfidf * tfidf.T).A)[0, 1]


def cosine_sim_toarray(documents):
    """returns a array containing all the similarities among the books"""
    tfidf = vectorizer.fit_transform(documents)
    return (tfidf * tfidf.T).toarray()


documents = [Wuthering_Height, Jane_Eyre, Agnes_Grey, Villette, Wildfell_hall]
print(cosine_sim(documents))
print(cosine_sim_toarray(documents))

# computing clustering
import numpy as np
import matplotlib
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# these are the similarities computed from the previous section
S = np.asarray(
    [
        [1.0, 0.82212268, 0.87105148, 0.81267892, 0.89582767],
        [0.82212268, 1.0, 0.89358607, 0.94076155, 0.93715077],
        [0.87105148, 0.89358607, 1.0, 0.90638528, 0.92821412],
        [0.81267892, 0.94076155, 0.90638528, 1.0, 0.92599655],
        [0.89582767, 0.93715077, 0.92821412, 0.92599655, 1],
    ]
)


# dissimilarity is 1 minus similarity
dissimilarities = 1 - S

# compute the embedding
coord = MDS(dissimilarity="precomputed").fit_transform(dissimilarities)

plt.scatter(coord[:, 0], coord[:, 1])

# Label the points
for i in range(coord.shape[0]):
    plt.annotate(str(i), (coord[i, :]))

plt.show()