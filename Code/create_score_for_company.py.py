from download_article_from_search import extract_articles_from_parser, find_list_articles
import os
import sys
sys.path.append(os.path.abspath('../database_management'))
from add_a_row import add_row
from datetime import date

def create_score_for_company(company):
  query = company + " ESG"
  parser, nb_articles = find_list_articles(query)
  L = extract_articles_from_parser(parser)

  scores = [article["ESGscore"] for article in L]
  if len(L)!=0:
    return(sum(L)/len(L),nb_articles)
  else:
    return(False,False)

def add_score_to_database(company):
  score, nb_articles = create_score_for_company(company)

  if score == False:
    print("error no article found")
    return(-1)
  else:
    add_row("database_ratings.db",(company,str(date.today()), score,nb_articles))
