import pandas as pd
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

from sklearn.datasets import load_files

import os
print(os.getcwd())

# for reproducibility
data = load_files('Assignment 2/Walden.txt',description=None,categories=None,load_content=True,shuffle=True,encoding="utf8", decode_error='replace', random_state=0)
# df = pd.DataFrame(list(zip(data['data'], data['target'])), columns=['text', 'label'])
# df.head()
