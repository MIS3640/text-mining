
def main():
    import urllib.request
    import pickle

    url = 'http://www.gutenberg.org/ebooks/3567.txt.utf-8'
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    print(text) # for testing

    with open('Napoleon_texts.pickle','w') as f:
        pickle.dump(text,f)


    # Load data from a file (will be part of your data processing script)
    with open('Napolean_text.pickle','r') as input_file:
        reloaded_copy_of_texts = pickle.load(input_file)


if __name__ == '__main__':
    main()






# Save data to a file (will be part of your data fetching script)

