from os import path
import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud, STOPWORDS


def word_freq_freuds():
    """
    Return the most frequent words and least frequent words from Freud's texts in word cloud format.
    """
    # opening and reading a file
    file = open("data/freuds_texts.pickle", errors="ignore")
    text = file.read()
    file.close()
    stopwords = set(STOPWORDS)

    # generating wordcloud
    wordcloud = WordCloud(
        font_path="C:/Windows/Fonts/Georgia.ttf",
        relative_scaling=0.50,
        background_color="white",
        width=800,
        height=800,
        stopwords=stopwords,
        min_font_size=10,
    ).generate(text)

    # plotting the image
    plt.imshow(wordcloud)

    # save the image in .png format
    plt.savefig("wordcloud_freuds.png")

    # display the image file
    plt.show()


def main():
    word_freq_freuds()


if __name__ == "__main__":
    main()
