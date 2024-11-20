from download_article_from_search import extract_articles_from_parser, find_list_articles

def create_score_for_company(company):
  query = company + " ESG"
  parser, nb_articles = find_list_articles(query)
  L = extract_articles_from_parser(parser)

  scores = [article["ESGscore"] for article in L]
  if len(L)!=0:
    return(sum(L)/len(L))
  else:
    return(False)

def add_score_to_database(company):
  score = create_score_for_company(company)

  if score == False:
    print("error no article found")
    return(-1)
  else:
    
