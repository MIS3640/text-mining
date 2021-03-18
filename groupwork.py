import urllib.request
import analyze_book
import string
import nltk

keys = ["Pride and Prejudice.txt", "Sense and Sensibility.txt", "Northanger Abbey.txt", "Mansfield Park.txt"]
list_of_texts = []

def download_books():
    """
    downloads four Jane Austen books from Project Gutenberg 
    """
    values = ['http://www.gutenberg.org/files/1342/1342-0.txt', 'http://www.gutenberg.org/files/161/161-0.txt', 'http://www.gutenberg.org/files/121/121-0.txt', 'http://www.gutenberg.org/files/141/141-0.txt']
    books = dict(zip(keys, values))
    names = []
    for key in books.keys(): 
        names.append(key) 
    order = 0
    
    # download the books and store them as txt files
    for i in books.values():
        response = urllib.request.urlopen(i)
        data = response.read()  # a `bytes` object
        text = data.decode('utf-8')
        with open(names[order],"w", encoding="utf-8") as fout:
            fout.write(text)
        order += 1

def text_books():
    """
    store each book as a string variable for future methods
    """
    text1 = open(keys[0], "r", encoding="utf-8").read()
    text2 = open(keys[1], "r", encoding="utf-8").read()
    text3 = open(keys[2], "r", encoding="utf-8").read()
    text4 = open(keys[3], "r", encoding="utf-8").read()

    return text1, text2, text3, text4


def process_books():
    """
    processes all four books into dictionaries where the keys are words that appear and the values are frequencies of words in the text
    """
    book1 = analyze_book.process_file(keys[0],skip_header=True)
    book2 = analyze_book.process_file(keys[1],skip_header=True)
    book3 = analyze_book.process_file(keys[2],skip_header=True)
    book4 = analyze_book.process_file(keys[3],skip_header=True)
    
    return book1, book2, book3, book4


def common_words(book1, book2, book3, book4):
    """
    prints top 20 common words for each of the four books
    """  
    books = [book1, book2, book3, book4]
    print("\nThe most common words are:")
    print("\nPride and Prejudice\tSense and Sensibility\tNorthanger Abbey\tMansfield Park")
    
    # prints common words into a table
    for x in range(20):
        output = []
        for i in books:
            t = analyze_book.most_common(i)
            for freq, word in t[x:x+1]:
                add = str(word)+"      "+str(freq)
                output.append(add)
        print("\t\t".join(output))
       

def common_words_wo_stopwords(text1, text2, text3, text4):
    """
    prints top 20 common words without stopwords for each of the four books
    """
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from collections import Counter

    # get rid of stopwords, punctuations, and digits
    added_list = ['“','”',"‘","’"]
    stop_words = set(stopwords.words("english") + list(string.punctuation) + list(string.digits) + added_list)
    texts = [text1.lower(), text2.lower(), text3.lower(), text4.lower()]
    x = 0
    for i in texts:
        word_tokens = word_tokenize(i)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]  
        filtered_sentence = []
        for w in word_tokens:  
            if w not in stop_words:  
                filtered_sentence.append(w)
        list_of_texts.append(filtered_sentence)
        output = Counter(filtered_sentence)
        common = output.most_common(20)
        print("\nThe most common words without stopwords in", keys[x], "are:", "\n", common)
        x += 1


def summary_stats(book1, book2, book3, book4):
    """
    prints a table of summary stats about these four books, including: total number of words, total number 
    of unique words, and the percentage of unique words in each text
    """
    from tabulate import tabulate
    books = [book1, book2, book3, book4]
    num_words = []
    num_unique = []
    percentage = []

    # populate each list
    for i in range(4):
        num_words.append(analyze_book.total_words(books[i]))
        num_unique.append(analyze_book.different_words(books[i]))
        percentage.append(num_unique[i]/num_words[i]*100)

    # prints table
    data = [[keys[0], num_words[0], num_unique[0], percentage[0]],
    [keys[1], num_words[1], num_unique[1], percentage[1]],
    [keys[2], num_words[2], num_unique[2], percentage[2]],
    [keys[3], num_words[3], num_unique[3], percentage[3]]] 
    print("\n\nSummary Stats of these four books:\n")
    print(tabulate(data, headers=["Text", "# of Total Words", "# of Unique Words", "Percentage of Unique Words(%)"]))


def sentiment(text1, text2, text3, text4):
    """
    prints sentiment polarity scores for each book
    """
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    score1 = SentimentIntensityAnalyzer().polarity_scores(text1)
    score2 = SentimentIntensityAnalyzer().polarity_scores(text2)
    score3 = SentimentIntensityAnalyzer().polarity_scores(text3)
    score4 = SentimentIntensityAnalyzer().polarity_scores(text4)
    print("\nThe sentiments are:\n", keys[0], score1,"\n", keys[1], score2,"\n", keys[2], score3,"\n", keys[3], score4)


def jaccard_similarity(alltexts):
    """
    prints jaccard similarity score of each book compared to all four books
    """
    text1 = alltexts[0]
    text2 = alltexts[1]
    text3 = alltexts[2]
    text4 = alltexts[3]
    union = text1+text2+text3+text4
    intersection1 = 0
    intersection2 = 0
    intersection3 = 0
    intersection4 = 0

    # checks for similarity in each book
    for a in text1:
        if a in text2 and a in text3:
            if a in text4:
                intersection1 += 1
    score1 = intersection1/len(union)

    for b in text2:
        if b in text1 and b in text3:
            if b in text4:
                intersection2 += 1
    score2 = intersection2/len(union)

    for c in text3:
        if c in text2 and c in text1:
            if c in text4:
                intersection3 += 1
    score3 = intersection3/len(union)

    for d in text4:
        if d in text2 and d in text3:
            if d in text1:
                intersection4 += 1
    score4 = intersection4/len(union)

    print("\nThe similarity scores are:")
    print("The similarity between", keys[0], "and the rest is: ", score1)
    print("The similarity between", keys[1], "and the rest is: ", score2)
    print("The similarity between", keys[2], "and the rest is: ", score3)
    print("The similarity between", keys[3], "and the rest is: ", score4)


def main():
    download_books()

    b1,b2,b3,b4 = process_books()
    common_words(b1,b2,b3,b4)

    t1,t2,t3,t4 = text_books()
    common_words_wo_stopwords(t1,t2,t3,t4)

    summary_stats(b1,b2,b3,b4)

    sentiment(t1,t2,t3,t4)

    jaccard_similarity(list_of_texts)
    

if __name__ == '__main__':
    main()