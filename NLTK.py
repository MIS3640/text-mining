#Code developed by Raphael using the class and online ressources
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 


def sentiment(filename):
    book = open(filename, 'r', encoding='UTF8')
    book1 = book.read()
    book2 = book1[1020:-18940]
    score = SentimentIntensityAnalyzer().polarity_scores(book2)
    print(score)
    print(filename)

def main():
    # sentiment('data/a_modest_proposal.txt')
    # sentiment('data/cape_cod.txt')
    # sentiment('data/frankenstein.txt')
    # sentiment('data/mrs_dalloway_in_bond_street.txt')
    # sentiment('data/the_coquette.txt')
    sentiment('data/the_great_gatsby.txt')


if __name__ == "__main__":
    main()
