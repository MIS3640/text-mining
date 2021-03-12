import urllib.request

#The Project Gutenberg eBook of A Modest Proposal, by Jonathan Swift
url1 = 'http://www.gutenberg.org/files/1080/1080-0.txt'
response1 = urllib.request.urlopen(url1)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
print(text) # for testing

url2 = 'http://www.gutenberg.org/files/1080/1080-0.txt'
response1 = urllib.request.urlopen(url1)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
print(text) # for testing