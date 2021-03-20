# from mediawiki import MediaWiki

# wikipedia = MediaWiki()
# babson = wikipedia.page("iPhone")
# print(iphone.title)
# print(iphone.content)

from mediawiki import MediaWiki

wikipedia = MediaWiki()
babson = wikipedia.page("Iphone")
print(babson.title)
print(babson.content)

