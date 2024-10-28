import streamlit as st
import streamlit.session_state as ss

st.set_page_config(page_title="Sense AL", page_icon="🤖", layout="wide")

tabs = ["Monitoring","Search tab", "Results"]
st.sidebar.subheader("Navigation")
selected_tab = st.sidebar.radio(' ',tabs)

