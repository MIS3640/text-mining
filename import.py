import urllib.request
import os

#The Project Gutenberg eBook of A Modest Proposal, by Jonathan Swift
print(os.getcwd())

url1 = 'http://www.gutenberg.org/files/1080/1080-0.txt'
response1 = urllib.request.urlopen(url1)
data1 = response1.read()  # a `bytes` object
text1 = data1.decode('utf-8')
# text1 = data1.encode("utf-8")
fout = open('data/the_project_gutenberg.txt','w')
# fout.write(text1)
# fout.close()
print(text1) # for testing


# url2 = 'http://www.gutenberg.org/files/1080/1080-0.txt'
# response1 = urllib.request.urlopen(url1)
# data = response.read()  # a `bytes` object
# text = data.decode('utf-8')
# print(text) # for testing
