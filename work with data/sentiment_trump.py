''' ANALYZING THE SENTIMENT OF THE INTRO PARAGRAPH OF THE TRUMP ARTICLE ''' 
import nltk

text = """Donald John Trump (born June 14, 1946) is the 45th and current president of the United States. Before entering politics, he was a businessman and television personality.
Born and raised in Queens, New York City, Trump attended Fordham University for two years and received a bachelor's degree in economics from the Wharton School of the University of Pennsylvania. He became president of his father's real estate business in 1971, renamed it The Trump Organization, and expanded its operations to building or renovating skyscrapers, hotels, casinos, and golf courses. Trump later started various side ventures, mostly by licensing his name. Trump and his businesses have been involved in more than 4,000 state and federal legal actions, including six bankruptcies. He owned the Miss Universe brand of beauty pageants from 1996 to 2015, and produced and hosted the reality television series The Apprentice from 2003 to 2015.
Trump's political positions have been described as populist, protectionist, isolationist, and nationalist. He entered the 2016 presidential race as a Republican and was elected in a surprise electoral college victory over Democratic nominee Hillary Clinton while losing the popular vote. He became the oldest first-term U.S. president and the first without prior military or government service. His election and policies have sparked numerous protests. Trump has made many false or misleading statements during his campaign and presidency. The statements have been documented by fact-checkers, and the media have widely described the phenomenon as unprecedented in American politics. Many of his comments and actions have been characterized as racially charged or racist.
During his presidency, Trump ordered a travel ban on citizens from several Muslim-majority countries, citing security concerns; after legal challenges, the Supreme Court upheld the policy's third revision. He enacted a tax-cut package for individuals and businesses, rescinding the individual health insurance mandate penalty of the Affordable Care Act, but has failed to repeal and replace the ACA as a whole. He appointed Neil Gorsuch and Brett Kavanaugh to the Supreme Court. In foreign policy, Trump has pursued an America First agenda, withdrawing the U.S. from the Trans-Pacific Partnership trade negotiations, the Paris Agreement on climate change, and the Iran nuclear deal. He imposed import tariffs which triggered a trade war with China, moved the U.S. embassy in Israel to Jerusalem and withdrew U.S. troops from northern Syria. Trump met three times with North Korean leader Kim Jong-un, but talks on denuclearization broke down in 2019. Trump reacted slowly to the COVID-19 pandemic; he minimized the threat, ignored or contradicted many recommendations from health officials, and promoted false information about unproven treatments and the availability of testing.
A special counsel investigation led by Robert Mueller found that Trump and his campaign welcomed and encouraged Russian interference in the 2016 presidential election under the belief that it would be politically advantageous, but did not find sufficient evidence to press charges of criminal conspiracy or coordination with Russia. Mueller also investigated Trump for obstruction of justice, and his report neither indicted nor exonerated Trump on that offense. After Trump solicited Ukraine to investigate his political rival Joe Biden, the House of Representatives impeached him in December 2019 for abuse of power and obstruction of Congress. The Senate acquitted him of both charges in February 2020."""

def overall_sentiment_of_website(url)
    
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
    text = """Donald John Trump (born June 14, 1946) is the 45th and current president of the United States. Before entering politics, he was a businessman and television personality.
    Born and raised in Queens, New York City, Trump attended Fordham University for two years and received a bachelor's degree in economics from the Wharton School of the University of Pennsylvania. He became president of his father's real estate business in 1971, renamed it The Trump Organization, and expanded its operations to building or renovating skyscrapers, hotels, casinos, and golf courses. Trump later started various side ventures, mostly by licensing his name. Trump and his businesses have been involved in more than 4,000 state and federal legal actions, including six bankruptcies. He owned the Miss Universe brand of beauty pageants from 1996 to 2015, and produced and hosted the reality television series The Apprentice from 2003 to 2015.
    Trump's political positions have been described as populist, protectionist, isolationist, and nationalist. He entered the 2016 presidential race as a Republican and was elected in a surprise electoral college victory over Democratic nominee Hillary Clinton while losing the popular vote. He became the oldest first-term U.S. president and the first without prior military or government service. His election and policies have sparked numerous protests. Trump has made many false or misleading statements during his campaign and presidency. The statements have been documented by fact-checkers, and the media have widely described the phenomenon as unprecedented in American politics. Many of his comments and actions have been characterized as racially charged or racist.
    During his presidency, Trump ordered a travel ban on citizens from several Muslim-majority countries, citing security concerns; after legal challenges, the Supreme Court upheld the policy's third revision. He enacted a tax-cut package for individuals and businesses, rescinding the individual health insurance mandate penalty of the Affordable Care Act, but has failed to repeal and replace the ACA as a whole. He appointed Neil Gorsuch and Brett Kavanaugh to the Supreme Court. In foreign policy, Trump has pursued an America First agenda, withdrawing the U.S. from the Trans-Pacific Partnership trade negotiations, the Paris Agreement on climate change, and the Iran nuclear deal. He imposed import tariffs which triggered a trade war with China, moved the U.S. embassy in Israel to Jerusalem and withdrew U.S. troops from northern Syria. Trump met three times with North Korean leader Kim Jong-un, but talks on denuclearization broke down in 2019. Trump reacted slowly to the COVID-19 pandemic; he minimized the threat, ignored or contradicted many recommendations from health officials, and promoted false information about unproven treatments and the availability of testing.
    A special counsel investigation led by Robert Mueller found that Trump and his campaign welcomed and encouraged Russian interference in the 2016 presidential election under the belief that it would be politically advantageous, but did not find sufficient evidence to press charges of criminal conspiracy or coordination with Russia. Mueller also investigated Trump for obstruction of justice, and his report neither indicted nor exonerated Trump on that offense. After Trump solicited Ukraine to investigate his political rival Joe Biden, the House of Representatives impeached him in December 2019 for abuse of power and obstruction of Congress. The Senate acquitted him of both charges in February 2020."""
    
    # print(token_sent(text))

    # sentences = token_sent(text)
    # sent_analysis(sentences)

    # print(text_words_no_sw(text))

    # filtered_words = text_words_no_sw(text)
    # top_word_plot_no_sw(filtered_words, 20)



if __name__ == '__main__':
    main()
