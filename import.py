#Code developed by Raphael using the class and online ressources
import urllib.request
import os

def book_import(book_url, filename):
    """ 
    Function that imports the ebook and saves it into a new file under data
    """
    response = urllib.request.urlopen(book_url)
    data = response.read() 
    text = data.decode('utf-8')
    fout = open(filename,'w', encoding="utf-8")
    fout.write(text)
    fout.close()
    print(text) # for testing


def main():
    # A Modest Proposal by Jonathan Swift (UK 18th century)
    book_import('http://www.gutenberg.org/files/1080/1080-0.txt', 'data/a_modest_proposal.txt')

    # The Coquette by Hannah Webster Foster (US 18th century)
    book_import('http://www.gutenberg.org/cache/epub/12431/pg12431.txt', 'data/the_coquette.txt')

    # Frankenstein by Mary Wollstonecraft (Godwin) Shelley (UK 19th century)
    book_import('http://www.gutenberg.org/files/84/84-0.txt', 'data/frankenstein.txt')

    # Cape Cod by Henry David Thoreau (US 19th century)
    book_import('http://www.gutenberg.org/files/34392/34392-0.txt', 'data/cape_cod.txt')

    # Mrs Dalloway in Bond Street, by Virginia Woolf (UK 18th century)
    book_import('http://www.gutenberg.org/cache/epub/63107/pg63107.txt', 'data/mrs_dalloway_in_bond_street.txt')

    # The Great Gatsby by F. Scott Fitzgerald (US 20th century)
    book_import('http://www.gutenberg.org/files/64317/64317-0.txt', 'data/the_great_gatsby.txt')


if __name__ == "__main__":
    main()