import urllib.request

url = 'http://www.gutenberg.org/ebooks/1080.txt.utf-8'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
print(text) # for testing