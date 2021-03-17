
# Load data
import nltk
import pickle
import pprint

with open("review_data.pickle", "rb") as data_input:
    reloaded_review_text = pickle.load(data_input)

# pprint.pprint(reloaded_review_text)
# print(type(reloaded_review_text))

### STEP 3
# SENTIMENT ANALYSIS
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sent_analysis():
    """Analyzes the sentiment of each review and add the score
    to the dictionary"""
    for movie in reloaded_review_text:
        for sub_list in movie["review_info"]:
            t = sub_list["review_text"]
            s = SentimentIntensityAnalyzer().polarity_scores(t)
            sub_list["sentiment_score"] = s
            del sub_list["review_text"]
        # pprint.pprint(sub_list)
    return reloaded_review_text


sent_dict = sent_analysis()
# pprint.pprint(sent_dict)

### Save data
import pickle

with open("sent_data.pickle", "wb") as f:
    pickle.dump(sent_dict, f)

# CREATE LIST
# create list for imdb rating and compound scores
imdb_rating_list = []
compound_list = []
for movie in sent_dict:
    for user in movie["review_info"]:
        imdb_rating_list.append(user["imdb_rating"])  # list for imdb rating
        compound_list.append(
            user["sentiment_score"]["compound"]
        )  # list for compound score

# print(len(imdb_rating_list))
# print(len(compound_list))

# SCATTERPLOT
import matplotlib.pyplot as plt

plt.scatter(imdb_rating_list, compound_list)
plt.xlabel("IMDB rating")
plt.ylabel("compound score")
plt.title("IMDB rating vs. compound score")
plt.show()  # scatter plot

# CREATE LIST
# for average compound score by movie
avg_compound_list = []
for movie in sent_dict:
    compound_list = []
    for user in movie["review_info"]:
        compound_list.append(user["sentiment_score"]["compound"])
    avg_compound = sum(compound_list) / len(compound_list)  # finding mean
    avg_compound_list.append(avg_compound)

print(avg_compound_list)

# BAR CHART
data = avg_compound_list
plt.bar(["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"], data)
plt.xlabel("movie #")
plt.ylabel("average compound score")
plt.title("Average Compound Score by Movie")
plt.bar(range(len(data)), data)
plt.show()  # print bar chart