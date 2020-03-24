import random
import string

def process_file(filename, skip_header=True):
    """
    processes Gutenberg files in to plain texts string
    
    filename: string, file path
    skip_header: boolean, whether to skip the Gutenberg header

    returns: a string.
    """
    text = ''
    fp = open(filename, encoding='UTF8')

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('PREFACE'):
            continue
        if line.startswith('CHAPTER'):
            continue
        if line.startswith('End of the Project'):
            break

        line = line.replace('\n', ' ')
        line = line.replace('\t', ' ')
        line = line.replace('-', ' ')
        line = line.replace('_', ' ')
        line = line.replace('\"', '')
        line = line.replace('(', '')
        line = line.replace(')', '')

        punc = [',', '.', '?', ';', ':', '!', '...']
        for symbol in punc:
            line = line.replace(symbol, f' {symbol} ')

        line = line.lower()
        text = text + line
            
    return text


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def combine_text(new_file, *texts):
    """
    append all texts into the new file
    new_file: string, path to the new file
    *texts: string tuple
    """
    new = open(new_file, 'a')

    for text in texts:
        s = ''.join(text)
        new.write(s)
    
    new.close()

def main():
    a = process_file("Mark Twain/A Connecticut Yankee in King Arthur's Court.txt", skip_header=True)
    b = process_file("Mark Twain/Advantures of Huckleberry Finn.txt", skip_header=True)
    c = process_file("Mark Twain/Eve's Diary, Complete.txt", skip_header=True)
    d = process_file("Mark Twain/Life On The Mississippi.txt", skip_header=True)
    e = process_file("Mark Twain/Roughing It.txt", skip_header=True)
    f = process_file("Mark Twain/The Adventures of Tom Sawyer.txt", skip_header=True)
    g = process_file("Mark Twain/The Innocents Abroad.txt", skip_header=True)
    h = process_file("Mark Twain/The Mysterious Stranger, and Other Stories.txt", skip_header=True)
    i = process_file("Mark Twain/The Prince and The Pauper.txt", skip_header=True)
    j = process_file("Mark Twain/The Tragedy of Pudd'nhead Wilson.txt", skip_header=True)
    
    combine_text("Mark Twain/Mark Twain.txt",(a,b,c,d,e,f,g,h,i,j))


if __name__ == "__main__":
    main()