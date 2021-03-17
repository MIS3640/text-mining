from mediawiki import MediaWiki

wikipedia = MediaWiki()
babson = wikipedia.page("Galaxy_S")
print(babson.title)
print(babson.content)