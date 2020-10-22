# Create the file_database for Compared Texts

# Open Book Files
import pickle

with open("freud_texts.pickle", "rb") as input_file:
    freud_texts = pickle.load(input_file)


with open("jungs_texts.pickle", "rb") as input_file:
    jungs_texts = pickle.load(input_file)
    # print(jungs_texts)

# Extract content of Psychology from Wiki
from mediawiki import MediaWiki

wikipedia = MediaWiki()
psychology_content = wikipedia.page("Psychology")
psychology = psychology_content.content


file_database = [freud_texts, jungs_texts, psychology]

# Cosine Similarity Comparison Starts
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Create the Matrix
count_vectorizer = CountVectorizer(stop_words="english")
count_vectorizer = CountVectorizer()
sparse_matrix = count_vectorizer.fit_transform(file_database)

doc_term_matrix = sparse_matrix.todense()
df = pd.DataFrame(
    doc_term_matrix,
    columns=count_vectorizer.get_feature_names(),
    index=["freud_texts", "jungs_texts", "psychology"],
)
df

from sklearn.metrics.pairwise import cosine_similarity

print(cosine_similarity(df, df))