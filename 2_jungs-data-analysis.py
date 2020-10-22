def open_file(filename):

    """filename: a str"""

    import pickle

    with open(filename, "rb") as input_file:
        reloaded_copy_of_text = pickle.load(input_file)

    return reloaded_copy_of_text


def processed_data(opened_file, removed_list):

    """remove space, punctuations, and convert every letter into lower case"""
    """removed string = file access route, str"""

    import string

    strippables = string.punctuation + string.whitespace

    a = list(opened_file.split())
    all_words = {}

    for word in a:
        temp_word = list(word)  # str -> list
        for element in temp_word:
            if element in strippables:
                temp_word.remove(element)
        filtered_word = ("".join(temp_word)).lower()  # list-> str
        if filtered_word in all_words:
            all_words[filtered_word] += 1
        else:
            all_words[filtered_word] = 1

    """create the list of words need to be removed"""
    f = open(removed_list)
    meaningless_words = []
    for line in f:
        words = list(line.split())
        meaningless_words.extend(words)

    """check every key in all_words dictionary belongs to the meaningless list"""
    """if it does, remove"""
    meaningful_words = {}
    for word in all_words.keys():
        # print(word)
        if word not in meaningless_words:
            meaningful_words[word] = all_words.get(word)

    """eventually we get a meaniful word list as the final result"""

    return meaningful_words


def total_words(analysis_input):
    result = 0
    for v in analysis_input.values():
        result += v
        # print(result)
    return result


def different_words(analysis_input):
    """Returns the number of different words in a histogram."""
    total_differnt_word = 0
    for key in analysis_input:
        total_differnt_word += 1
    return total_differnt_word


def main():
    opened_file = open_file("jungs_texts.pickle")
    analysis_input = processed_data(opened_file, "data/stopwords.txt")
    # print(analysis_input)
    print(
        f"The total number of meaningful words in this book is {total_words(analysis_input)}"
    )
    print(
        f"The total number of unique meaningful words in this book is {different_words(analysis_input)}"
    )


if __name__ == "__main__":
    main()
