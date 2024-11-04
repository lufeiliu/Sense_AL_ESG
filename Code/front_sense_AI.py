import streamlit as st
import time
from download_articles_from_search import find_list_articles, test

# from ../Backend/download_article_from_search import test

ss = st.session_state

st.set_page_config(page_title="Sense AL", page_icon="🤖", layout="wide")

tabs = ["Monitoring","Search tab", "Results"]
st.sidebar.subheader("Navigation")
selected_tab = st.sidebar.radio(' ',tabs)

if selected_tab == tabs[0]:
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

        placeholder.markdown(f"{nb_articles} articles trouvés !")

        placeholder2 = st.empty()
        placeholder2 = st.markdown('Analyse des articles en cours...')
        


if selected_tab == tabs[2]:
    st.text(test())