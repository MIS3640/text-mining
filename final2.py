### Load data
import pickle
import pprint

with open("review_data.pickle", "rb") as data_input:
    reloaded_review_text = pickle.load(data_input)
# pprint.pprint(reloaded_review_text)
# print(type(reloaded_review_text))

### STEP 2
### Remove punctuations
from unicodedata import category
import sys


def remove_punct(imdb_data_list):
    """
    Removes punctuations in the reviews and puts it back in the original data list
    """
    strippables = "".join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )
    stripped_text = []

    for movie in reloaded_review_text:
        for sub_list in movie["review_info"]:
            t = sub_list["review_text"]
            t = t.replace("-", " ").replace(chr(8212), " ")
            new_t = "".join(x for x in t if x not in strippables)
            sub_list["review_text"] = new_t

    return reloaded_review_text


cleaned = remove_punct(reloaded_review_text)
pprint.pprint(cleaned)

### Save data
import pickle

with open("review_data.pickle", "wb") as f:
    pickle.dump(cleaned, f)

