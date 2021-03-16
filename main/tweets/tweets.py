from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from collections import OrderedDict
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.decomposition import TruncatedSVD
import matplotlib.pyplot as plt
import string
import csv
import numpy as np
import random
import dill as pickle

# Data obtained from https://www.kaggle.com/kapastor/democratvsrepublicantweets
# Dictionaries for Reps + Parties + Words as well as set of stopwords for later
Reps = {}
Parties = {}
Reps2Parties = {}
stopWords = set(stopwords.words('english'))


def anti_dict(d):
    """Return a new, flipped version of a provided dictionary."""
    return {k: v for v, k in d.items()}


def register(dc, st):
    """Given a dict and a string, adds st to dict and assigns id number as value"""
    if st not in dc.keys():
        dc[st] = len(dc)


def process_string(txt, tk):
    """Text Pipeline: extract -> lower & remove non-ascii chars -> tokenize -> filter stopwords, punctuation and links.
    txt: string, tweet to process
    tk: tokenizer to process string with

    returns: list of strings from the processed tweet"""
    # Text Pipeline: extract -> lower & remove non-ascii chars -> tokenize -> filter stopwords, punctuation and links
    txt = txt.lower().encode('latin1').decode('ascii', errors='ignore')
    txt = tk.tokenize(txt)
    txt = [wd for wd in txt if wd not in stopWords.union(set(string.punctuation))]
    txt = list(filter(lambda x: False if 'https:' in x else True, txt))
    txt = tuple(filter(lambda x: False if len(x) <= 3 else True, txt))

    return txt


def process_row(row, tk):
    """Given row from csv read, and tokenizer, returns tuple(Party, Rep, Text)
    
    Party: 0 or 1, string in Parties
    Reps: integer i, string in Reps
    Text: list of strings []"""

    # Text Pipeline: extract -> lower & remove non-ascii chars -> tokenize -> filter stopwords, punctuation and links -> maybe stem leftover words to reduce misspelling error
    txt = process_string(row[2], tk)
    
    return (Parties[row[0]], Reps[row[1]], txt)
    

def read_csv(fp="main/tweets/ExtractedTweets.csv"):
    """Given a filepath, reads a csv and returns a list of tuples:
    (Party, Rep, Text)
    
    Party: 0 or 1, string in Parties
    Reps: integer i, string in Reps
    Text: list of strings []
    """

    with open(fp, encoding="latin1") as csvfile:
        # Create Generator and Tokenizer
        readCSV = csv.reader(csvfile, delimiter=',')
        tk = TweetTokenizer(strip_handles=True)
        
        # Iterate over CSV file
        rows = []
        i = 0
        for row in readCSV:
            if i > 0:
                # Register Party/Rep names
                register(Parties, row[0])
                register(Reps, row[1])
                Reps2Parties[row[1]] = Parties[row[0]]
                
                # Add row to output
                rows.append(process_row(row, tk))
                
            i += 1
            # readCSV is a generator so I just manually put the length in, 86,461
            if i % 1000 == 0:
                print(f"Row {i} of {86461} parsed: {round(i/86461,4)*100}%")
        
        return rows 


def fitTFIDF(data, return_int=False, vector=TfidfVectorizer):
    """Given list of tuples from read csv, as well as a sklearn vectorizer class,
    returns encoded words/the encoder"""
    # We set min to keep words that are too infrequent from clogging up the features
    # We want words that appear at least 30 times
    encoder = vector(min_df=30/len(data), lowercase=False, analyzer=lambda x: x)
    encoder = encoder.fit([w[2] for w in data])
    scores = encoder.transform([w[2] for w in data])

    if return_int:
        scores = (scores > 0).astype(int)

    return scores, encoder


def print_model_report(nb, encoder, predictions, y_test, class_labels):
    """
    Prints out report on trained Naive Bayes model
    nb: trained NaiveBayes model from sklearn
    encoder: TfIDVectorizer
    Predictions: Np Array, output of model predictions 
    y_test: ground truth labels for classes

    Returns: None
    """
    # Thanks, sklearn!
    print("Model Report:")
    print(classification_report(y_test, predictions))


    # Which words are the most important?

    def print_party(party, results):
        """Takes arguments
           party: string, printed class label
           results: string, word of importance
           and prints them... returns None"""

        print(f"Top 10 {party} words:")
        for i, r in enumerate(results):
            print(f"{i}: {r}")
            if i > 9:
                break
    
    # Get list of log probabilities for each input feature (word)
    label_words = [nb.feature_log_prob_[i, :].argsort() for i, _ in enumerate(class_labels)]

    # For each class, print out the top 10 words
    for i, label in enumerate(class_labels):
        print_party(label, np.take(encoder.get_feature_names(), label_words[i]))

    # Test a few sentences for a sanity check
    def sanity_check():
        """Prints out a test of 2 biased sentences and 1 unbiased sentence to see if what's been done so far makes sense.
           Assumes only two classes, write a new test if I wind up doing anything more than binary classification"""

        print(f"Sanity check: Sentence, [p({class_labels[1]}), p({class_labels[0]})]")

        s1 = ["Thank the lord for president Trump #gopfuture".split()]
        s2 = ["#pollutingpruitt has destroyed the environment".split()]
        s3 = ["Hey would you like to grab a coffee sometime".split()]

        print(f"{s1}: {nb.predict_proba(encoder.transform(s1))}")
        print(f"{s2}: {nb.predict_proba(encoder.transform(s2))}")
        print(f"{s3}: {nb.predict_proba(encoder.transform(s3))}")
    

    sanity_check()


def train_model(data, scores, encoder, class_labels=("Republican", "Democrat"), verbose=True):
    """Given pre-processed training data of the form returned by 'fitTFIDF'*, trains + returns a Multinomial Naive Bayes model
    based on the data and prints report on model performance.
    
    * As well as class labels for printing in report, positive then negative

    data: List of iterables where iterable[0] is the class label (y values come from here)
    scores: TfIDF embedding of data (x values)
    encoder: TfIDVectorizer object trained on input data
    class_labels: Names of classes in English

    returns: Trained MultinomialNaiveBayes object from sklearn
    """

    # Split into Train/Test sets
    X_train, X_test, y_train, y_test = train_test_split(scores, np.array(list(map(lambda x: x[0], data))).reshape(-1, 1), test_size=0.2, random_state=42)


    # Fit + evaluate model
    nb = MultinomialNB()
    nb.fit(X_train, y_train)
    predictions = nb.predict(X_test)

    # Print Model Report
    if verbose:
        print_model_report(nb, encoder, predictions, y_test, class_labels)

    return nb


def plot_model_predictions(scores, nb, data=None, plot=True):
    """Decompose Tf-IdF scores to 2d with SVD and then View model predictions over groups.
    Returns: 2d Representation of tf-idf scores.

    scores: np array (len(data), n_features)
    nb: Trained NB model
    plot: boolean, whether to generate+display graph?
    data: list of iterables where the first element of each iterable is the ground truth.
    If data is provided, plots ground truths rather than model predictions over the 2d projection.
    """

    # Reduce Dimensions
    coord = TruncatedSVD().fit_transform(scores)

    # Label: Ground Truth or Model Prediction
    if data:
        probs = [d[0] for d in data]
    else:
        probs = [nb.predict_proba(sc)[0][1] for sc in scores]

    if plot:
        cmap = plt.cm.get_cmap('seismic')

        plt.scatter(coord[:, 0], coord[:, 1], c=probs, cmap=cmap, alpha=0.3)
        plt.colorbar().set_label("Probability of Tweet coming from a Republican Politician") # Technically correct for ground truth
        plt.title("2d Representation of Tf-IDF Scores")

        plt.show()
        plt.clf()

    return coord


def cluster_labels(scores, coord):
    # Can't fit DBSCAN/Spectral/other clustering algos in memory, so a quick visually-obtained line to seperate the two groups
    return (coord[:,1] > 0.05)


def save_data_and_model(scores, model, nb):
    """Saves our beloved data and model"""

    def save(name, ob):
        """Pickles an obj to cd with fname name.pickle"""
        with open(f"{name}.pickle", "wb") as f:
            pickle.dump(ob, f)
    
    save("tfscores", scores)
    save('tfencoder', model)
    save('naivebayes', nb)


def load_data_and_model():
    """If data/model pickled, returns tuple:
    ( MultinomialNB(), TfidVetorizer(), tfid scores(numpy array) )"""

    def load(name):
        with open(f"{name}.pickle", "rb") as f:
                return pickle.load(f)
    
    return load("naivebayes"), load('tfencoder'), load('tfscores')


def get_rep_tweets(rep_id, data):
    """Given int rep_id and data in (party, rep, tweet) format:
    returns rep's tweets in (party, rep, tweet) format
    """
    return [d for d in data if d[1]==rep_id]


def analyze_rep(rep_id, data, encoder, nb):
    """Given trained model nb, data data, TfIDVectorizer encoder, and int rep_id:
    returns tuple (rep handle, average % Republican via model)
    """
    tweets = encoder.transform([o[2] for o in get_rep_tweets(rep_id, data)])

    predictions = list(map(lambda x: nb.predict_proba(x), tweets))
    
    return (anti_dict(Reps)[rep_id], (sum([p[0][1] for p in predictions]) / len(predictions)))


def reps_report(l):
    for party in Parties.values():
        d = [x[1] for x in l if Reps2Parties[x[0]] == party]
        print(f"Party: {anti_dict(Parties)[party]} Mean: {np.mean(d)} St. Deviation: {np.std(d)}")

    # Plot distributions
    fig, axs = plt.subplots(2, 1)


    # Set axes' scales
    for ax in axs:
        ax.set_xlim(0, 1)
        ax.axvline(0.5, alpha=0.75)

    # Histograms
    axs[0].hist(np.asarray([x[1] for x in l if Reps2Parties[x[0]] == 0]))
    axs[1].hist(np.asarray([x[1] for x in l if Reps2Parties[x[0]] == 1]))

    # Titles
    axs[0].set_title("Democrats' Avg. Probability of Republican Tweet")
    axs[1].set_title("Republicans' Avg. Probability of Republican Tweet")

    plt.show()

    l = sorted(l, key=lambda x: x[1])
 
    print("10 Most Republican Accounts According to Model")
    print("Twitter Handle, Average Probability of Tweet from rep being labelled Republican")
    for t in l[-10:]:
        print(t)
    
    print("Top 10 Least Republican Accounts According to Model")
    for t in l[:10]:
        print(t)
    
    print("Top 10 Most Centrist Accounts According to Model")
    med = sorted(l, key=lambda l: abs(0.5 - l[1]))
    for t in med[:10]:
        print(t)

    
def main():
    # Load data + Pre-Process Text
    data = read_csv()

    # Generate TF-IDF scores and train NB model
    # Not traditional to use Tf-IDF with Multinomial NB... 
    # But like many things in ML, it works pretty well to try theoretically questionable methods which add more information!
    # Model seemed to perform about equally well with both models: slightly overpredicted Repub w/tf, Dem with simple count
    scores, encoder = fitTFIDF(data, return_int=False)
    nb = train_model(data, scores, encoder)

    # twoD = plot_model_predictions(scores, nb)
    # twoD = plot_model_predictions(scores, nb, data=data)

    # Save our work!
    save_data_and_model(scores, encoder, nb)

    # Let's check out the 2 conspicuous clusters generated by SVD decomposition and see if there's any pattern...

    # Fit a Naive Bayes classifier on the new data
    # y = cluster_labels(scores, twoD).astype(int)
    # mo = train_model([(v, "") for v in y], scores, encoder, class_labels=("Small Cluster", "Large Cluster"))

    # Never put this model into production... not a lot to learn here from clusters, maybe an artifact of squishing so many dimensions into 2d


    # Let's rank politicians based on what political party the model thinks they're in
    # Create a list of (rep, avg probability of Republican tweet)
    l = [analyze_rep(v, data, encoder, nb) for k, v in Reps.items()]
    reps_report(l)

    

if __name__ == "__main__":
    main()
