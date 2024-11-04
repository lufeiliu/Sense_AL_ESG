import requests
from lxml.html import fromstring
import json
import base64

class clarticle:
    def __init__(self,title,url,date,author,text):
        self.title = title
        self.url = url
        self.date = date
        self.author = author
        self.text = text

def format_date(date):
    return(date)

def format_author(author):
    return(author)

def decode_base64(encoded_url):
    # Decode the base64-encoded URL and convert it to a UTF-8 string
    decoded_string = base64.b64decode(encoded_url).decode("utf-8")
    
    # The line `return json.loads(decoded_string)[-1]` is decoding a JSON string and returning the
    # last element of the resulting list.
    return json.loads(decoded_string)[-1]


def extract_base64_string(url):
    # Split the URL by semicolon, then further split the second part by colon to extract the base64 string
    return url.split(";")[1].split(":")[1]

def convert_url(url):

    return(decode_base64(extract_base64_string(url)))

def find_list_articles(query,language = 'en-US'):

    return("x",5)

    params = {
        'q': query,
        'hl': language,
        'gl': 'US',
        'ceid': 'US:en',
    }

    response = requests.get('https://news.google.com/search', params=params)
    parser = fromstring(response.text)

    nb_articles = len(parser.xpath('//*[@id="yDmH0d"]/c-wiz/div/main/div[2]/c-wiz')[0])

    return(parser,nb_articles)

def test():
    return("yes")
    