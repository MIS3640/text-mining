from imdbpie import Imdb
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string

imdb = Imdb()

def get_stopwords():
    """
    This function reads a text doc of stopwords, and returns a set of these stopwords. 
    """
    results = set()
    f = open("stopwords.txt", "r")
    lines = f.readlines()
    for line in lines:
        results.add(line.strip('\n'))
    f.close()
    return results

def get_word_count_dict(list_of_reviews):
    """
    Given a list of reviews, this function counts the frequency of each word excluding stopwords. 
    If there are no reviews, returns an empty dictionary. Otherwise, returns a dictionary of words to their word counts.  
    """
    if not list_of_reviews:
        return {}
    stopwords = get_stopwords()
    translator = str.maketrans('', '', string.punctuation)

    word_count_dict = {}
    for review in list_of_reviews:
        review_text = review['reviewText']
        review_text = review_text.translate(translator)
        words = review_text.split()
        for word in words:
            word_lower = word.lower()
            if word_lower in stopwords:
                continue
            if word_lower in word_count_dict:
                word_count_dict[word_lower] += 1
            else:
                word_count_dict[word_lower] = 1

    return word_count_dict

def get_top_words(word_count_dict, n):
    """
    Given a dictionary of words to their word counts, this function creates a list of tuples of words and their word counts of the top n most frequently used words.
    It then returns the top 10 most common words in these reviews, starting from the most common word. 
    """
    word_count_list = []
    for k, v in word_count_dict.items():
        word_count_list.append((v, k))
    
    word_count_list = sorted(word_count_list, reverse=True)

    top_n_words_count = word_count_list[:n]
    for idx, count_and_word in enumerate(top_n_words_count):
        print(f'{idx + 1}. Word: {count_and_word[1]}, Count: {count_and_word[0]}')

def get_average_review_stats(list_of_reviews):
    """
    Given a list of reviews, this function aggregates the sentiment intensity polarity scores of each review 
    and returns the total positive reviews, total negative reviews, average compound score, average positive score, and average negative score.
    """
    if not list_of_reviews:
        return {}
    analyzer = SentimentIntensityAnalyzer()

    polarity_scores = []
    for review in list_of_reviews:
        polarity_scores.append(analyzer.polarity_scores(review['reviewText']))

        total_positive_reviews = 0
        total_negative_reviews = 0
        total_compound_score = 0
        total_positive_score = 0
        total_negative_score = 0

    for score in polarity_scores:
        if score['compound'] > 0:
            total_positive_reviews += 1
        else:
            total_negative_reviews += 1
        
        total_compound_score += score['compound']
        total_positive_score += score['pos']
        total_negative_score += score['neg']

    avg_compound_score = total_compound_score / len(list_of_reviews)
    avg_positive_score = total_positive_score / len(list_of_reviews)
    avg_negative_score = total_negative_score / len(list_of_reviews)
    
    print(f'The total positive reviews is: {total_positive_reviews}')
    print(f'The total negative reviews is: {total_negative_reviews}')
    print(f'The average compound score is: {avg_compound_score}')
    print(f'The average positive score is: {avg_positive_score}')
    print(f'The average negative score is: {avg_negative_score}')

def main():
    """
    This function allows the user to enter a movie of his or her choice. 
    It searches for the title using the imdbpie library & takes the first result. 
    It provides a sentiment analysis of the film's reviews, as well as the top 10 most frequently used words in those reviews.
    """
    print("****************************************************************************\n")
    print("Hi! This is the film analyzer.\n")
    movie_title = input("Enter a movie title:\n")
    try:
        titles = imdb.search_for_title(movie_title)
    except:
        print("Title Not Found. Please Try Another Title.")
        return main()
        
    if len(titles) == 0:
        print("Title Not Found. Please Try Another Title.")
        return main()
        
    title = titles[0]
    print(title)

    print("Analyzing {title}...".format(title=title['title']))
    reviews = imdb.get_title_user_reviews(title['imdb_id'])
    raw_reviews = reviews.get('reviews')

    if not raw_reviews:
        print("This movie has no reviews. Please try another title")
        return main()

    print("Sentiment analysis of the current movie's reviews:")
    avg_review_stats = get_average_review_stats(raw_reviews)
    print("Top 10 words in the reviews for the current movie:")
    word_count_dict = get_word_count_dict(raw_reviews)
    get_top_words(word_count_dict, 10)

if __name__ == "__main__":
    main()