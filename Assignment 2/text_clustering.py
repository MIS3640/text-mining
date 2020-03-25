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

# vec = TfidfVectorizer(stop_words="english")
# vec.fit(df.text.values)
# features = vec.transform(df.text.values)

# cls = MiniBatchKMeans(n_clusters=5, random_state=random_state)
# cls.fit(features)

# # predict cluster labels for new dataset
# cls.predict(features)

# # to get cluster labels for the dataset used while
# # training the model (used for models that does not
# # support prediction on new dataset).
# cls.labels_


# # reduce the features to 2D
# pca = PCA(n_components=2, random_state=random_state)
# reduced_features = pca.fit_transform(features.toarray())

# # reduce the cluster centers to 2D
# reduced_cluster_centers = pca.transform(cls.cluster_centers_)

# plt.scatter(reduced_features[:,0], reduced_features[:,1], c=cls.predict(features))
# plt.scatter(reduced_cluster_centers[:, 0], reduced_cluster_centers[:,1], marker='x', s=150, c='b')