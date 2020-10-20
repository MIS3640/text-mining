''' ANALYZING THE SENTIMENT OF THE INTRO PARAGRAPH OF THE BIDEN ARTICLE ''' 
import nltk

text = '''Joseph Robinette Biden Jr. (born November 20, 1942) is an American politician who served as the 47th vice president of the United States from 2009 to 2017. A member of the Democratic Party, he served as a United States Senator for Delaware from 1973 to 2009. Biden is the Democratic presidential nominee for the 2020 election, running against the incumbent, President Donald Trump.[2]
Biden was raised in Scranton, Pennsylvania, and New Castle County, Delaware. He studied at the University of Delaware before receiving his law degree from Syracuse University.[3] He became a lawyer in 1969 and was elected to the New Castle County Council in 1970. He was elected to the U.S. Senate from Delaware in 1972, becoming the sixth-youngest senator in American history. Biden was a longtime member and eventually chairman of the Senate Foreign Relations Committee. He opposed the Gulf War in 1991 but supported the expansion of the NATO alliance into Eastern Europe and its intervention in the Yugoslav Wars of the 1990s. He supported the resolution authorizing the Iraq War in 2002 but opposed the surge of U.S. troops in 2007. He also served as chairman of the Senate Judiciary Committee from 1987 to 1995, dealing with issues related to drug policy, crime prevention, and civil liberties. Biden led the efforts to pass the Violent Crime Control and Law Enforcement Act and the Violence Against Women Act, and oversaw six U.S. Supreme Court confirmation hearings, including the contentious hearings for Robert Bork and Clarence Thomas. Biden ran unsuccessfully for the Democratic presidential nomination in 1988 and 2008.
Biden was reelected six times to the U.S. Senate and was the fourth-most senior senator when he resigned after winning the vice presidency alongside Barack Obama in the 2008 presidential election.[4] Obama and Biden were reelected in 2012. As Vice President, Biden oversaw infrastructure spending in 2009 to counteract the Great Recession. His negotiations with congressional Republicans helped the Obama administration pass legislation including the 2010 Tax Relief Act, which resolved a taxation deadlock; the Budget Control Act of 2011, which resolved a debt ceiling crisis; and the American Taxpayer Relief Act of 2012, which addressed the impending fiscal cliff. In foreign policy, Biden led the efforts to pass the United States–Russia New START treaty, supported military intervention in Libya, and helped formulate U.S. policy toward Iraq through the withdrawal of U.S. troops in 2011. Following the Sandy Hook Elementary School shooting, Biden led the Gun Violence Task Force, created to address the causes of gun violence in the United States.[5]
In October 2015, Biden announced that he would not seek the presidency in the 2016 election. In January 2017, Obama awarded Biden the Presidential Medal of Freedom with distinction.[6] Biden announced his 2020 candidacy for president on April 25, 2019, and in June 2020, he met the 1,991-delegate threshold needed to secure the Democratic Party's nomination.[7] On August 11, 2020, Biden announced U.S. Senator Kamala Harris as his running mate in the 2020 presidential election.[8]'''

def token_sent(text):
    '''splits text up into individual sentences'''
    from nltk.tokenize import sent_tokenize
    sentences = sent_tokenize(text)
    return sentences


def sent_analysis(sentences):
    '''takes the sentences from the text and performs a sentiment analysis on each sentence 
    to see if it is positive, negative, or neutral'''
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    for sentence in sentences:
        print(sentence)
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]), end='')
        print()

def text_words_no_sw(text):
    '''this function takes the text input andsplits it all into individual words.
    It then generates a list of words to be disregarded called "stopwords".
    After that it creates a list of words excluding the stop words  
    '''
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words("english"))

    from nltk.tokenize import word_tokenize
    tokenized_word = word_tokenize(text)

    filtered_words = []
    for word in tokenized_word:
        if word not in stop_words:
            filtered_words.append(word)
    
    return filtered_words

def top_word_plot_no_sw(filtered_words, num):
    '''takes a list of words and returns a frequencey distribution of the words
    num: an int of the number of words you want to be shown in the plot from largest to smallest'''

    from nltk.probability import FreqDist
    fdist = FreqDist(filtered_words)
    import matplotlib.pyplot as plt
    fdist.plot(num, cumulative = False)
    plt.show()

def main():
    text = '''Joseph Robinette Biden Jr. (born November 20, 1942) is an American politician who served as the 47th vice president of the United States from 2009 to 2017. A member of the Democratic Party, he served as a United States Senator for Delaware from 1973 to 2009. Biden is the Democratic presidential nominee for the 2020 election, running against the incumbent, President Donald Trump.[2]
    Biden was raised in Scranton, Pennsylvania, and New Castle County, Delaware. He studied at the University of Delaware before receiving his law degree from Syracuse University.[3] He became a lawyer in 1969 and was elected to the New Castle County Council in 1970. He was elected to the U.S. Senate from Delaware in 1972, becoming the sixth-youngest senator in American history. Biden was a longtime member and eventually chairman of the Senate Foreign Relations Committee. He opposed the Gulf War in 1991 but supported the expansion of the NATO alliance into Eastern Europe and its intervention in the Yugoslav Wars of the 1990s. He supported the resolution authorizing the Iraq War in 2002 but opposed the surge of U.S. troops in 2007. He also served as chairman of the Senate Judiciary Committee from 1987 to 1995, dealing with issues related to drug policy, crime prevention, and civil liberties. Biden led the efforts to pass the Violent Crime Control and Law Enforcement Act and the Violence Against Women Act, and oversaw six U.S. Supreme Court confirmation hearings, including the contentious hearings for Robert Bork and Clarence Thomas. Biden ran unsuccessfully for the Democratic presidential nomination in 1988 and 2008.
    Biden was reelected six times to the U.S. Senate and was the fourth-most senior senator when he resigned after winning the vice presidency alongside Barack Obama in the 2008 presidential election.[4] Obama and Biden were reelected in 2012. As Vice President, Biden oversaw infrastructure spending in 2009 to counteract the Great Recession. His negotiations with congressional Republicans helped the Obama administration pass legislation including the 2010 Tax Relief Act, which resolved a taxation deadlock; the Budget Control Act of 2011, which resolved a debt ceiling crisis; and the American Taxpayer Relief Act of 2012, which addressed the impending fiscal cliff. In foreign policy, Biden led the efforts to pass the United States–Russia New START treaty, supported military intervention in Libya, and helped formulate U.S. policy toward Iraq through the withdrawal of U.S. troops in 2011. Following the Sandy Hook Elementary School shooting, Biden led the Gun Violence Task Force, created to address the causes of gun violence in the United States.[5]
    In October 2015, Biden announced that he would not seek the presidency in the 2016 election. In January 2017, Obama awarded Biden the Presidential Medal of Freedom with distinction.[6] Biden announced his 2020 candidacy for president on April 25, 2019, and in June 2020, he met the 1,991-delegate threshold needed to secure the Democratic Party's nomination.[7] On August 11, 2020, Biden announced U.S. Senator Kamala Harris as his running mate in the 2020 presidential election.[8]'''
    
    # print(token_sent(text))

    sentences = token_sent(text)
    sent_analysis(sentences)

    # print(text_words_no_sw(text))

    # filtered_words = text_words_no_sw(text)
    # top_word_plot_no_sw(filtered_words, 20)

if __name__ == '__main__':
    main()