from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pickle
import matplotlib.pyplot as plt
 
 
# python -m pip install -U pip
# python -m pip install -U matplotlib
 
 
def sentiment_scatter(movie, source):
    """senitment analysis, input str movie and source, output sentiment analysis"""
    # opens pickle
    with open(f"{movie}_{source}.pickle", "rb") as input_file:
        copy = pickle.load(input_file)
    # stores sentiment score in list
    sentiment_pos = []
    sentiment_neg = []
    for line in copy:
        score = SentimentIntensityAnalyzer().polarity_scores(line)
        sentiment_pos.append(score["pos"])
        sentiment_neg.append(score["neg"])
    return sentiment_pos, sentiment_neg
 
 
def scatter(movie, source1, source2, source1_list, source2_list):
    """prints scatter plot when 2 data sources are inputted"""
    source1_pos, source1_neg = source1_list
    source2_pos, source2_neg = source2_list
    one = plt.scatter(source1_pos, source1_neg, color="r", marker="x")
    two = plt.scatter(source2_pos, source2_neg, color="b")
    plt.xlabel("Positive Words")
    plt.ylabel("Negative Words")
    plt.title(f"Postive vs. Negative words in {movie} reviews.")
    plt.legend((one, two), (source1, source2))
    plt.show()
 
 
def main():
    movie = "Parasite"
    source1 = "twitter"
    source2 = "imdb"
    mulan1 = sentiment_scatter(movie, source1)
    mulan2 = sentiment_scatter(movie, source2)
    scatter(movie, source1, source2, mulan1, mulan2)
 
 
if __name__ == "__main__":
    main()
