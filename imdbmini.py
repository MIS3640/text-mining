#plan is to create a function that creates a dictionary with movie names as keys, then maybe bubble rating, director, and list of stars
import requests
from bs4 import BeautifulSoup
import re

def remove_tags(item):
    """
    Converts item to a string nad removes HTML tags
    """
    item = str(item)
    item = item.replace('<', '(')
    item = item.replace('>', ')')
    item = re.sub(r" ?\([^)]+\)", "", item)
    return item

def initialize(css_selector):
    """
    Initializes the requests for future functions in this API
    """
    url_list = ['https://www.imdb.com/search/title/?groups=top_250&sort=user_rating', 
    'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt',
    'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt',
    'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=151&ref_=adv_nxt',
    'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=201&ref_=adv_nxt']
    array = []
    for url in url_list:
        url = url
        page= requests.get(url)
        soup = BeautifulSoup(page.text,"html.parser")
        movie_titles = soup.select(css_selector)
        for item in movie_titles:
            if css_selector == '.runtime':
                item = remove_tags(item)
                item = re.sub(' min', '', item)
                item = int(item)
                array.append(item)
            else:
                item = remove_tags(item)
                array.append(item)
    return array

def get_titles():
    """
    Prints the titles of the top 250 movies on IMDB in order
    """
    titles = initialize('.lister-item-header a')
    return(titles)

def get_directors():
    """
    Prints the directors of the top 250 movies on IMDB in order
    """
    directors = initialize('.text-muted+ p a:nth-child(1)')
    return(directors)

def get_runtimes():
    """
    Prints the runtimes of the top 250 movies on IMDB in order
    """
    runtimes = initialize('.runtime')
    return(runtimes)

def get_stars():
    """
    Prints the stars of the top 250 movies on IMDB in order
    """
    stars = initialize('.lister-item-content .ghost~ a')
    return(stars)