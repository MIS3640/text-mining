# Work in Progress

from mediawiki import MediaWiki
wikipedia = MediaWiki()
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def average(lst): 
    return sum(lst) / len(lst) 

# Dictionaries containing left/centre/right candidate (admittedly arbitrary) at the last general or presidental election
# Done G20 countries with (only in my personal opinion) a strong multi-party democracy

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
usa = {"left":"Hillary Clinton", "centre": "Gary Johnson", "right": "Donald Trump"} # united states

countries = [arg, aus, bra, can, fra, ger, ind, idn, jap, mex, rsa, kor, gbr, usa]

left_neu = []
left_compound = []
centre_neu = []
centre_compound = []
right_neu = []
right_compound = []

for country in countries:
    left_summary = wikipedia.page(country["left"]).summary
    centre_summary = wikipedia.page(country["centre"]).summary
    right_summary = wikipedia.page(country["right"]).summary
    left_neu.append(SentimentIntensityAnalyzer().polarity_scores(left_summary)["neu"])
    left_compound.append(SentimentIntensityAnalyzer().polarity_scores(left_summary)["compound"])
    centre_neu.append(SentimentIntensityAnalyzer().polarity_scores(centre_summary)["neu"])
    centre_compound.append(SentimentIntensityAnalyzer().polarity_scores(centre_summary)["compound"])
    right_neu.append(SentimentIntensityAnalyzer().polarity_scores(right_summary)["neu"])
    right_compound.append(SentimentIntensityAnalyzer().polarity_scores(right_summary)["compound"])
    
print(f"The proportion of neutral text in the wikipedia summaries is:")
print(f"Left-wing politicians: {average(left_neu)*100:.2f}%")
print(f"Centre-wing politicians: {average(centre_neu)*100:.2f}%")
print(f"Right-wing politicians: {average(right_neu)*100:.2f}%")

print(f"\nThe normalised positivity score is:")
print(f"Left-wing politicians: {average(left_compound):.2f}")
print(f"Centre-wing politicians: {average(centre_compound):.2f}")
print(f"Right-wing politicians: {average(right_compound):.2f}")