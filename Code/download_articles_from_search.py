import requests
from lxml.html import fromstring
import json
import base64
import newspaper
import time

class clarticle:
    def __init__(self,title,url,date,author,text,ESGscore):
        self.title = title
        self.url = url
        self.date = date
        self.author = author
        self.text = text
        self.ESGscore = ESGscore

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

def extract_articles_from_parser(parser):
    L = []
    articles = parser.xpath('//*[@id="yDmH0d"]/c-wiz/div/main/div[2]/c-wiz')[0]
    
    for k in range(len(articles)):
        parser_author = parser.xpath(f'//*[@id="yDmH0d"]/c-wiz/div/main/div[2]/c-wiz/c-wiz[{k}]/c-wiz/article/div[2]/div/span')
        parser_url = parser.xpath(f'//*[@id="yDmH0d"]/c-wiz/div/main/div[2]/c-wiz/c-wiz[{k}]/c-wiz/article/div[1]/div[1]/a/@jslog')
        parser_date = parser.xpath(f'//*[@id="yDmH0d"]/c-wiz/div/main/div[2]/c-wiz/c-wiz[{k}]/c-wiz/article/div[2]/time/@datetime')
        parser_title = parser.xpath(f'//*[@id="yDmH0d"]/c-wiz/div/main/div[2]/c-wiz/c-wiz{k}/c-wiz/article/div[1]/div[2]/div/a/text()')


   
        if len(parser_url)>0:
            try:
                url = convert_url(parser_url[0])
            except:
                continue
            
            try:
                news = newspaper.Article(url)
                news.download()
                news.parse()
            except:
                continue

            if news.text != '':
                text = news.text
            else:
                continue

            if news.publish_date != None:
                date = news.publish_date
            elif len(parser_date)>0:
                date = format_date(parser_date[0])
            else:
                date = format_date(-1)

            if len(news.authors)>0:
                author = ', '.join(news.authors)
            elif len(parser_author)>0:
                author = format_author(parser_author[0].text)
            else:
                author = 'No author'

            if len(parser_title)>0:
                title = parser_title[0]
            else:
                title = 'No title'

            L.append(clarticle(title,url,date,author,[]))

    return(L)

def compute_esg_score(text):
    return(1)

def extract_one_article_from_parser(parser, k):


    parser_author = parser.xpath(f'//*[@id="yDmH0d"]/c-wiz/div/main/div[2]/c-wiz/c-wiz[{k}]/c-wiz/article/div[2]/div/span')
    parser_url = parser.xpath(f'//*[@id="yDmH0d"]/c-wiz/div/main/div[2]/c-wiz/c-wiz[{k}]/c-wiz/article/div[1]/div[1]/a/@jslog')
    parser_date = parser.xpath(f'//*[@id="yDmH0d"]/c-wiz/div/main/div[2]/c-wiz/c-wiz[{k}]/c-wiz/article/div[2]/time/@datetime')
    parser_title = parser.xpath(f'//*[@id="yDmH0d"]/c-wiz/div/main/div[2]/c-wiz/c-wiz{k}/c-wiz/article/div[1]/div[2]/div/a/text()')



    if len(parser_url)>0:
        try:
            url = convert_url(parser_url[0])
        except:
            return(False)
        
        try:
            news = newspaper.Article(url)
            news.download()
            news.parse()
        except:
            return(False)

        if news.text != '':
            text = news.text
        else:
            return(False)

        if news.publish_date != None:
            date = news.publish_date
        elif len(parser_date)>0:
            date = format_date(parser_date[0])
        else:
            date = format_date(-1)

        if len(news.authors)>0:
            author = ', '.join(news.authors)
        elif len(parser_author)>0:
            author = format_author(parser_author[0].text)
        else:
            author = 'No author'

        if len(parser_title)>0:
            title = parser_title[0]
        else:
            title = 'No title'

        esg_score = compute_esg_score(text)
        
        return(clarticle(title,url,date,author,text,esg_score))
    return(False)

def compute_score_from_list_of_article(L):
    return(max([item.ESGscore for item in L]))

def extract_text_from_url(url):
    '''
    From an url of a newspaper, download the text of the article
    '''
    
    test = newspaper.Article(url)
    test.download()

    test.parse()
    return(test.text)
