from mediawiki import MediaWiki

# import os
# print(os.getcwd())

# load in Trump wikipedia page
wikipedia = MediaWiki()
trump = wikipedia.page("Donald Trump")
# print(trump.content)

t_text = open('data/trump.txt', 'w', encoding='UTF8')
trump_title = trump.title
trump_content = trump.content

t_text.write(trump_title)
t_text.write(trump_content)
t_text.close

# load in Biden wikipedia page 
wikipedia = MediaWiki()
biden = wikipedia.page("Biden")
# print(biden.content)

b_text = open('data/biden.txt', 'w', encoding='UTF8')
biden_title = biden.title
biden_content = biden.content

b_text.write(biden_title)
b_text.write(biden_content)
b_text.close