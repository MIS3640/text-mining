import extractimdb
import extracttwitter
import analyze_nltk
import analyze_text
import os
import matplotlib.pyplot as plt
import scatterplot

#This is a master function for all of our analysis tools.
 
def analyze_movie(movie):
    """shows stats for movie reviews"""
    source1 = "imdb"
    source2 = "twitter"
    # if imdb pickle does not exist, extracts pickle
    if not os.path.isfile(f"{movie}_imdb.pickle"):
        extractimdb.review_extracter(movie)
    # if twitter pickle does not exist, extracts pickle
    if not os.path.isfile(f"{movie}_twitter.pickle"):
        extracttwitter.twitter_extracter(movie)
 
    # process and analyze data
    for source in [source1, source2]:
        hist = analyze_text.process_file(movie, source)
        t = analyze_text.most_common(hist, excluding_stopwords=True)
        print()
        print(f"The most common words in {source} reviews:")
        for freq, word in t[0:20]:
            print(f"{word:<10} {freq}")
        print()
        print(f"Histogram of top 10 words in {source} reviews")
        analyze_text.print_most_common(hist, num=10)
        print()
        average, sentiment_list = analyze_nltk.sentiment_analysis(movie, source)
        print(f"The average sentiment on {source} is {average}.")
        print("Individual scores are:")
        print(sentiment_list)
    # create sentiment scatter plot
    mulan1 = scatterplot.sentiment_scatter("Parasite", source1)
    mulan2 = scatterplot.sentiment_scatter("Parasite", source2)
    scatterplot.scatter(movie, source1, source2, mulan1, mulan2)
 
 
def main():
    movie = "Parasite"
    analyze_movie(movie)
 
 
if __name__ == "__main__":
    main()
 

