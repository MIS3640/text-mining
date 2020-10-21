from mediawiki import MediaWiki
import word_freq

wikipedia = MediaWiki()
print('Enter A Wiki Page:')
title = input()
page = wikipedia.page(title)


# Word Frequency
symbol_less = word_freq.remove_symbols(page.content)
lowered = word_freq.make_lowercase(symbol_less)
numberless = word_freq.remove_numbers(word_freq.freq(lowered))

# Times the Title is mentioned in the content
print(f'{title} appears {word_freq.word_freq(lowered,title.lower())} times in the content.')

most = word_freq.most_freq(numberless)

# Top 10 Most Frequent Words in the Page
print(f'Top 10 Most Frequent Words in Wiki page, {page.title}, are:')
word_freq.top_10_most_freq(most)

