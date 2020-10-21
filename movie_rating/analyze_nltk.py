from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pickle
def sentiment_analysis(movie, source):
    """senitment analysis, input str movie and source, output sentiment analysis"""
    # opens pickle
    with open(f"{movie}_{source}.pickle", "rb") as input_file:
        copy = pickle.load(input_file)
    # stores sentiment score in list
    sentiment_list = []
    for line in copy:
        score = SentimentIntensityAnalyzer().polarity_scores(line)
        sentiment_list.append(score["compound"])
    # finds average of sentiment score
    average = sum(sentiment_list) / len(sentiment_list)
    # returns average and list
    return average, sentiment_list
def main():
    average, sentiment_list = sentiment_analysis("Mulan", "imdb")
    print(f"The average sentiment is {average}.")
    print("Individual scores are:")
    print(sentiment_list)
if __name__ == "__main__":
    main()