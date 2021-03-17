# This program will read the content of two wikipedia pages and compare them to see how similar they are in word frequency, and sentiment.
# Additionally, specifically compare the links and backlinks to see if there is any overlap in what the articles are linked to
# this could be used to estimate how "far" away an article is from another one. i.e, it probably takes only a few clicks to navigate from the article "American Civil War" to the article
# on "Barack Obama", but more clicks to navigate from "American Civil War" to "Cleopatra", but which two articles are more similar in content and style?


from nltk.sentiment.vader import SentimentIntensityAnalyzer
from text_processing import process_str, most_common
from mediawiki import MediaWiki
import random
import nltk
wikipedia = MediaWiki()


def common_words_compare(article1, article2, n):
    """Takes two wikipedia pages, compares the n most popular words in the article, and returns the number of words most
    commonly used within both articles and the number of thimes they are shared"""

    first_page = wikipedia.page(article1)
    second_page = wikipedia.page(article2)
    first_hist = process_str(first_page.content)
    second_hist = process_str(second_page.content)
    t1 = most_common(first_hist)
    t2 = most_common(second_hist)
    shared = []
    for i in t1[0:n]:
        for j in t2[0:n]:
            if len(t1) > len(t2) and i[0] == j[0]:
                shared.append(j)
            elif i[0] == j[0]:
                shared.append(i)
    return shared


def links_compare(article1, article2):
    """Takes two wikipedia pages and returns any mediawiki links the two pages share"""
    first_page = wikipedia.page(article1)
    second_page = wikipedia.page(article2)
    link1 = first_page.links
    link2 = second_page.links
    shared = []
    if len(link1) > len(link2):
        for i in link1:
            for j in link2:
                if i == j:
                    shared.append(i)
    else:
        for i in link2:
            for j in link1:
                if i == j:
                    shared.append(i)
    return shared


def backlinks_compare(article1, article2):
    """Compares the backlinks (pages that lead to the article) and returns a list of overlapping articles that contain 
    links to each article."""
    first_page = wikipedia.page(article1)
    second_page = wikipedia.page(article2)
    backlink1 = first_page.backlinks
    backlink2 = second_page.backlinks
    shared = []
    if len(backlink1) > len(backlink2):
        for i in backlink1:
            for j in backlink2:
                if i == j:
                    shared.append(i)
    else:
        for i in backlink2:
            for j in backlink1:
                if i == j:
                    shared.append(i)
    return shared

def compare_sentiment(article1, article2):
    """Compares the sentiment between the text of two articles, returning the absoulute difference between the two. """
    first_page = wikipedia.page(article1)
    second_page = wikipedia.page(article2)
    str1 = first_page.content
    str2 = second_page.content
    score1 = SentimentIntensityAnalyzer().polarity_scores(str1)
    score2 = SentimentIntensityAnalyzer().polarity_scores(str2)
    diff = dict()
    for key in score1:
        diff[key] = round(abs(score1[key] - score2[key]), 3)
    return diff

def wiki_page_compare():
    """Ask's for a user to decide which two articles to compare and how many similar words, links, and backlinks to view. Finally, it generates a sentiment analysis
    showing the difference between the two."""
    
    page1 = input("Please enter a specifc Wikipedia article")
    page2 = input("Please enter a second Wikipedia article")
    n = int(input("How many of the top words do you want to compare?"))

    t = common_words_compare(page1, page2, n)
    print("Shared words within the top", n, "most common words of each article: ")
    for word, freq in t:
        print(word, "\t", freq, "times")

    links = links_compare(page1, page2)
    links_to_show = int(input("How many shared links do you want to see?"))
    if links_to_show > len(links):
        links_to_show = len(links)
    print("\nShared links between the two pages:", len(links))
    print("Here's", links_to_show, "random ones:")
    rand_link = random.sample(links, links_to_show)
    for i in rand_link:
        print(i)

    print("\nPlease wait while we gather the backlinks...")
    backlinks = backlinks_compare(page1, page2)
    backlinks_to_show = int(input("How many shared backlinks do you want to see?"))
    if backlinks_to_show > len(backlinks):
        backlinks_to_show = len(backlinks)
    print("\nShared backlinks between the two pages:", len(backlinks))
    print("Here's", backlinks_to_show, "random ones:")
    rand_backlink = random.sample(backlinks, backlinks_to_show)
    for i in rand_backlink:
        print(i)
    
    print('\nThe sentiment difference between Article 1 and Article 2:')
    sentiment_diff = compare_sentiment(page1,page2)
    for key in sentiment_diff:
        print("The",key, 'score difference is', sentiment_diff[key], 'points')
    


def main():
    wiki_page_compare()

if __name__ == "__main__":
    main()