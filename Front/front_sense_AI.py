import streamlit as st
# import streamlit.session_state as ss
ss = st.session_state

st.set_page_config(page_title="Sense AL", page_icon="🤖", layout="wide")

tabs = ["Monitoring","Search tab", "Results"]
st.sidebar.subheader("Navigation")
selected_tab = st.sidebar.radio(' ',tabs)



if selected_tab == tabs[0]:

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
        print('appuyé')
