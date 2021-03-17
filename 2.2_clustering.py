import urllib.request
import string
import random
import sys
from unicodedata import category
import nltk
nltk.download('punkt')



def download_book(url):
    """
    Download the book from Gutenberg by using the url of the book
    return: a string
    """
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    return text

# import the url of the two analyzed books and other 4 books to python
url_PP = 'http://www.gutenberg.org/files/1342/1342-0.txt'
text1 = download_book(url_PP)

url_Gatsby = 'https://dev.gutenberg.org/files/64317/64317-0.txt'
text2 = download_book(url_Gatsby)

url_Northanger = 'http://www.gutenberg.org/files/121/121-0.txt'
text3 = download_book(url_Northanger)

url_Park = 'http://www.gutenberg.org/files/141/141-0.txt'
text4 = download_book(url_Park)

url_Susan = ' http://www.gutenberg.org/ebooks/946.txt.utf-8'
text5 = download_book(url_Susan)

url_Paradise = 'http://www.gutenberg.org/files/805/805-0.txt'
text6 = download_book(url_Paradise)


# Program to measure the similarity between two texts using cosine similarity. 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

# tokenization 
text1_list = word_tokenize(text5)  
text2_list = word_tokenize(text6) 

# sw contains the list of stopwords
sw = stopwords.words('english')  
l1 =[]
l2 =[] 

# remove stop words from the string 
text1_set = {w for w in text1_list if not w in sw}  
text2_set = {w for w in text2_list if not w in sw} 

# form a set containing keywords of both strings  
rvector = text1_set.union(text2_set)  
for w in rvector: 
    if w in text1_set: 
        l1.append(1) # create a vector 
    else: 
        l1.append(0) 
    if w in text2_set: 
        l2.append(1) 
    else: 
        l2.append(0) 
c = 0
  
# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 
print("similarity: ", cosine) 

# import numpy as np
# from sklearn.manifold import MDS
# import matplotlib.pyplot as plt

# # these are the similarities computed from the previous section
# S = np.asarray()

# # dissimilarity is 1 minus similarity
# dissimilarities = 1 - S

# # compute the embedding
# coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)

# plt.scatter(coord[:, 0], coord[:, 1])

# # Label the points
# for i in range(coord.shape[0]):
#     plt.annotate(str(i), (coord[i, :]))


# plt.show()