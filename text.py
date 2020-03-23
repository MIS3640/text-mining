import urllib.request

url = 'http://www.gutenberg.org/files/76/76-0.txt.utf-8'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
print(text) # for testing