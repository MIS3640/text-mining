from mediawiki import MediaWiki
wikipedia = MediaWiki()
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def average(lst):
    """ Returns the average of a list of numbers
    """ 
    return sum(lst) / len(lst)

def word_count(str):
    count = 0
    for letter in str:
        if ord(letter) == 32:
            count += 1
    return count

# Dictionaries containing leading left/centre/right candidate (admittedly arbitrary person opinion) at the last general
# or presidental election from G20 countries with (again personal opinion) a strong multi-party democracy
arg = {"left":"Alberto Fernández", "centre": "Roberto Lavagna", "right": "Mauricio Macri"} # argentina
aus = {"left":"Richard Di Natale", "centre": "Bill Shorten", "right": "Scott Morrison"} # australia
bra = {"left":"Fernando Haddad", "centre": "Geraldo Alckmin", "right": "Jair Bolsonaro"} # brazil
can = {"left":"Jagmeet Singh", "centre": "Justin Trudeau", "right": "Scheer"} # canada (just "Scheer" as "Andrew Scheer causes a crash")
fra = {"left":"Benoît Hamon", "centre": "Emmanuel Macron", "right": "Marine Le Pen"} # france
ger = {"left":"Martin Schulz", "centre": "Angela Merkel", "right": "Alexander Gauland"} # germany
ind = {"left":"Mamata Banerjee", "centre": "Rahul Gandhi", "right": "Narendra Modi"} # india
idn = {"left":"Joko Widodo", "centre": "Muhaimin Iskandar", "right": "Prabowo Subianto"} # indonesia 
jap = {"left":"Yukio Edano", "centre": "Yuichiro Tamaki", "right": "Shinzō Abe"} # japan
mex = {"left":"Andrés Manuel López Obrador", "centre": "José Antonio Meade", "right": "Ricardo Anaya"} # mexico
rsa = {"left":"Julius Malema", "centre": "Cyril Ramaphosa", "right": "Mmusi Maimane"} # south africa
kor = {"left":"Ahn Cheol-soo", "centre": "Kim Chong-in", "right": "Kim Moo-sung"} # south korea
gbr = {"left":"Jeremy Corbyn", "centre": "Jo Swinson", "right": "Boris Johnson"} # united kingdom
usa = {"left":"Hillary Clinton", "centre": "Gary Johnson", "right": "Donald Trump"} # united states (okay Johnson is a push for central)

# Created empty lists to add values too
left_word_count = []
left_neu = []
left_compound = []
centre_word_count = []
centre_neu = []
centre_compound = []
right_word_count = []
right_neu = []
right_compound = []

def leaders_wiki_analysis(country):
    """ Analyses the wikipedia summary of a country's leading left/centre/right politician, does a word count,
    determines how much of the content is neutral, and whether it leans positive or negative,
    then appending those scores to the revelent lists
    """
    left_summary = wikipedia.page(country["left"]).summary
    left_word_count.append(word_count(left_summary))
    left_neu.append(SentimentIntensityAnalyzer().polarity_scores(left_summary)["neu"])
    left_compound.append(SentimentIntensityAnalyzer().polarity_scores(left_summary)["compound"])
    centre_summary = wikipedia.page(country["centre"]).summary
    centre_word_count.append(word_count(centre_summary))
    centre_neu.append(SentimentIntensityAnalyzer().polarity_scores(centre_summary)["neu"])
    centre_compound.append(SentimentIntensityAnalyzer().polarity_scores(centre_summary)["compound"])
    right_summary = wikipedia.page(country["right"]).summary
    right_word_count.append(word_count(right_summary))
    right_neu.append(SentimentIntensityAnalyzer().polarity_scores(right_summary)["neu"])
    right_compound.append(SentimentIntensityAnalyzer().polarity_scores(right_summary)["compound"])

# Created a list with the countries
countries = [arg, aus, bra, can, fra, ger, ind, idn, jap, mex, rsa, kor, gbr, usa]

def ideology_wiki_sentiments():
    """ Runs a sentiment analysis of the wiki summaries for each country in the "countries" list,
    and then calculates the average percentage of non-neutral next and the averaged normalised positivity score
    of the three ideologies across all the countries.
    """
    for country in countries:
        leaders_wiki_analysis(country)
    print(f"The average word count the wikipedia summaries is:")
    print(f"Left-wing politicians: {average(left_word_count):4.0f}")
    print(f"Central politicians:   {average(centre_word_count):4.0f}")
    print(f"Right-wing politicians:{average(right_word_count):4.0f}")
    print(f"\nThe proportion of non-neutral text in the wikipedia summaries is:")
    print(f"Left-wing politicians:  {(1-average(left_neu))*100:5.2f}%")
    print(f"Central politicians:    {(1-average(centre_neu))*100:5.2f}%")
    print(f"Right-wing politicians: {(1-average(right_neu))*100:5.2f}%")
    print(f"\nThe normalised positivity score is:")
    print(f"Left-wing politicians:  {average(left_compound):.2f}")
    print(f"Central politicians:    {average(centre_compound):.2f}")
    print(f"Right-wing politicians: {average(right_compound):.2f}")

ideology_wiki_sentiments()