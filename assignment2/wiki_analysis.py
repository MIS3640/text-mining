### Wikipedia Text Analysis , Code developed by Prim Prasitanond ###

# PART 1: Data Importation and Cleaning

# Importing Text - Data Source : Wikipedia
from mediawiki import MediaWiki
def import_wiki (article_title):
    """
    This function fetch text from Wikipedia page based on the article title.
    This function returns the wikipedia article.

    article_title: The title of Wikipedia article (in string)
    """

    wikipedia = MediaWiki()
    article = wikipedia.page(article_title)
    # print(article.title)
    return article.content


# Clean Text - Remove punctuations
import string
def clean_text(text):
    """
    This function removes any punctuation in the text and return a cleaned string of
    wikipedia article without punctuation.

    text: the article content, output of import_wiki (article_title) function.
    """

    punctuations = string.punctuation
    no_punc = "" #string to store cleaned version of text

    for char in text:
        if char not in punctuations:
            no_punc = no_punc + char
    return no_punc

# Clean Text - Remove stopwords 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def remove_stopwords(cleaned_text):
    """
    This function removes any stopwords (such as 'about', 'the', 'any', etc)
    from the Wikipedia article.

    cleaned_text: string of wikipedia article without punctuation, output of the clean_text(text) function
     """
    word_tokens = word_tokenize(cleaned_text) #break down words from string
    stop_words = list(stopwords.words('english'))
    filtered_sentence = []

    for w in word_tokens:
        w =  w.lower()
        if w not in stop_words:
            filtered_sentence.append(w)
    
    #converting list back to string
    return " ".join(filtered_sentence)

# PART 2: Analyzing your text

# Word Frequency
def word_freq(processed_text):
    """This function returns a dictionary of word frequency in the article, 
    with word as a key and its frequency as value.

    processed_text: the cleaned article without punctuation and stopwords, output from previous functions.
    """
    d = {}

    for word in processed_text.split():
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    return d

# Export cleaned version of dictionary as pkl file
import pickle
def export_file (d, article_title):
    """This function exports cleaned version of word frequency dictionary as pkl file,
    the pkl file will later be used in the process of finding similar words between 2 articles.

    d:word frequency dictionary, output of the word_freq(processed_text) function
    article_title: the title of Wikipedia article (in string)
    """

    file = open(f'{article_title}.pkl', "wb")
    pickle.dump(d, file)
    file.close()

# Total words in dictionary
def total_words(d):
    """
    This function returns the total unique words in the article

    d: word frequency dictionary, output of the word_freq(processed_text) function
    """
    return len(d)

# Most common words - descending order
def most_common(d):          
    """
    This function returns a sorted list of tuples (in descending order) of frequent words in the article.

    d: word frequency dictionary, output of the word_freq(processed_text) function
    """
    common_words = [] #this is a list of tuples

    for word, freq in d.items():
        common_words.append((freq, word))

    #sort the list in descending order
    common_words.sort(reverse=True)

    return common_words

# Finding similar words between 2 articles
def similar(d1, d2):
    """
    This function returns a list of common words between 2 articles. 
    This list is sorted from the shortest to longest words.

    d1: the pkl file of first article 
    d2: the pkl file of second article
    """
    similar_words = []

    #the condition: add to d1 if the key doesn't exist in d2 (filtering), result returns common words
    for word in d1.keys():
        if word in d2.keys():
            similar_words.append(word)

    #sort the list based on word length
    similar_words.sort(key = len)

    return similar_words

# Bar Graph
import matplotlib.pyplot as plt
def plot_graph (most_frequent_word, article_title):
    """
    This function returns a bar graph of top 20 most frequent words in the article.

    most_frequent_word: list of tuples with words and its frequency, output of most_common(d) function.
    article_title: the title of Wikipedia article (in string)
    """
   #grabbing the values from tuples within list
    x_all = [x[1] for x in most_frequent_word]
    y_all = [y[0] for y in most_frequent_word]
    
    #limiting to top 20 most frequent words on the graph
    x_limit = x_all[0:20]
    y_limit = y_all[0:20]

    #graphing
    plt.bar(x_limit,y_limit, color='darkgreen')

    #labeling
    plt.title(f"Word Frequency in Wikipedia Article '{article_title}'")
    plt.xlabel("Words")
    plt.ylabel("Count of Words")
    plt.xticks(rotation=90)
    
    #displaying the graph
    plt.show()

#Test Code
def main():
    ###   PART 1   ###
    # import article from Wiki
    article_title = 'Psychoanalysis' #change the article based on your article preference
    import_wiki(article_title)

    # defining text
    text = import_wiki(article_title)
    # print(text)

    # cleaning text - remove punc. and stopwords
    cleaned_text = clean_text(text)
    remove_stopwords(cleaned_text)
    # print(remove_stopwords(cleaned_text))

    ###   PART 2   ###
    # word frequency
    processed_text = remove_stopwords(cleaned_text)
    word_freq(processed_text)
    print(word_freq(processed_text))

    # export to dictionary to txt file
    # d = word_freq(processed_text)
    # export_file(d, article_title)

    # word total
    d = word_freq(processed_text)
    print(f"The total words in this article: {total_words(d)} words")

    # most common words
    most_frequent_word = most_common(d)
    print('The most common words are:\n')
    for freq, word in most_frequent_word[0:20]: #20 most commonly used words
        print(f"{word:<10} \t {freq}")
    
    # bar graph
    plot_graph(most_frequent_word, article_title)

    # common words between 2 articles
    pkl_file1 = open("Psychoanalysis.pkl","rb")
    d1 = pickle.load(pkl_file1)

    pkl_file2 = open("Unconcious Mind.pkl","rb")
    d2 = pickle.load(pkl_file2)

    print('The similar words between 2 articles are:\n')
    print(similar(d1,d2))
    print(f"There are {len(similar(d1,d2))} words in common.")

if __name__ == '__main__':
    main()