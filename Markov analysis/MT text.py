def process_file(filename):
    """
    processes Gutenberg files in to plain strings without headings, footnotes, etc.
    added space before and after punctuations
    
    filename: string, file path
    skip_header: boolean, whether to skip the Gutenberg header

    returns: a string.
    """
    fp = open(filename, encoding='UTF8')

    text = ''
    skip_gutenberg_header(fp)

    for line in fp:
        line = line.lower()
        if line.startswith('preface'):
            continue
        if line.startswith('chapter'):
            continue
        if line.startswith('produced by'):
            continue
        if line.startswith('by mark twain'):
            continue
        if line.startswith('appendix'):
            continue
        if line.startswith('end of the project'):
            break
        if line.startswith('end of project'):
            break
        if line.startswith("transcriber's notes"):
            break
        if line.startswith("footnotes"):
            break

        line = line.replace('\n', ' ')
        line = line.replace('\t', ' ')
        line = line.replace('-', ' ')
        line = line.replace('_', ' ')
        line = line.replace('"', '')
        line = line.replace('(', '')
        line = line.replace(')', '')

        punc = [',', '.', '?', ';', ':', '!', '...']
        for symbol in punc:
            line = line.replace(symbol, f' {symbol} ')

        text += line
            
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
    append all strings into the new file
    
    new_file: string, path to the new file
    *texts: string tuple
    """
    t = ''
    for text in texts:
        s = ''.join(text)
        t += s
    
    with open(new_file, 'w') as new:
        new.write(t)

def main():
    a = process_file("Mark Twain/A Connecticut Yankee in King Arthur's Court.txt")
    b = process_file("Mark Twain/Advantures of Huckleberry Finn.txt")
    c = process_file("Mark Twain/Eve's Diary, Complete.txt")
    d = process_file("Mark Twain/Life On The Mississippi.txt")
    e = process_file("Mark Twain/Roughing It.txt")
    f = process_file("Mark Twain/The Adventures of Tom Sawyer.txt")
    g = process_file("Mark Twain/The Innocents Abroad.txt")
    h = process_file("Mark Twain/The Mysterious Stranger, and Other Stories.txt")
    i = process_file("Mark Twain/The Prince and The Pauper.txt")
    j = process_file("Mark Twain/The Tragedy of Pudd'nhead Wilson.txt")
    
    # combine_text("Markov analysis/Mark Twain.txt",(a,b,c,d,e,f,g,h,i,j))
    combine_text("Markov analysis/Mark Twain.txt",(b,f))


if __name__ == "__main__":
    main()