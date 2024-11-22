import streamlit as st
import time
from download_articles_from_search import find_list_articles, extract_one_article_from_parser, compute_score_from_list_of_article
from create_graph_from_db import create_graph_from_name

# from ../Backend/download_article_from_search import test

ss = st.session_state

st.set_page_config(page_title="Sense AL", page_icon="🍜", layout="wide")

tabs = ["Monitoring","Search tab", "Results"]
st.sidebar.subheader("Navigation")
selected_tab = st.sidebar.radio(' ',tabs)

if selected_tab == tabs[0]:
    list_companies = ['Total','Crédit_agricole','Amazon','Shell']
    company_to_display = st.selectbox("Select one company to monitor",list_companies)
    fig = create_graph_from_name(company_to_display)
    st.pyplot(fig)
    pass

if selected_tab == tabs[1]:
    ss['esg_company'] = ''
    ss['search_esg_type'] = ''
    ss['search_country'] = ''

    st.title("Recherche d'ESG")
    

    ss['esg_company'] = st.text_input("Entreprise")

    st.header('Critères optionnels')
    col1, col2 = st.columns(2)
    ss['search_esg_type'] = col1.text_input("Type d'ESG")
    ss['search_country'] = col2.text_input("Pays où se passe l'ESG")

    st.markdown('')
    st.markdown('')
    st.markdown('')
    c1,c2,c3 = st.columns(3)
    a = c2.button("Lancer la recherche")

    if a:
        placeholder = st.empty()
        placeholder.markdown('Fonction recherche lancée')

        
        placeholder.markdown('Recherche en cours...')

        query = ss['esg_company'] + ' ESG'

        parser, nb_articles = find_list_articles(query)

        placeholder.markdown(f"{nb_articles} articles trouvés")

        placeholder2 = st.empty()
        placeholder2.markdown('Analyse des articles en cours...')
        placeholder3 = st.empty()
        placeholder4 = st.empty()
        L = []

        max_nb_article = 10

        nb_articles = min(nb_articles,max_nb_article)

        for k in range(nb_articles):
            placeholder3.progress(k/nb_articles)
            extracted_article = extract_one_article_from_parser(parser,k)
            if extracted_article:
                L.append(extracted_article)
            placeholder4.markdown(f"{k} articles sur {nb_articles} extraits")
        placeholder4.empty()
        placeholder3.empty()
        placeholder2.markdown('Analyse terminée')

        score_of_this_search = compute_score_from_list_of_article(L)
        st.text(f'Le score pour cette boite est : {score_of_this_search}')


if selected_tab == tabs[2]:
    st.text("iuzefouh")