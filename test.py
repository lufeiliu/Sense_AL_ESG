from gnews import GNews
import newspaper

google_news = GNews()
paki = google_news.get_news('Pakistan')
print(paki[0])
article = google_news.get_full_article(paki[0]['url'])
print(article)
print("ahahah 11/11")