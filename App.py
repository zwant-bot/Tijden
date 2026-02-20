import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Zwemclub Tijden", page_icon="🏊‍♂️")
st.title("🏊‍♂️ Zwemclub Dashboard")

# Navigatie
menu = st.sidebar.radio("Menu", ["Presentie", "Tijden Invoeren", "Resultaten"])

if 'data' not in st.session_state:
    st.session_state.data = []

if menu == "Presentie":
    st.header("Presentielijst")
    namen = ["Lars", "Sophie", "Mo", "Emma"]
    for naam in namen:
        st.checkbox(naam, key=naam)
    st.button("Opslaan")

elif menu == "Tijden Invoeren":
    st.header("Nieuwe Tijd")
    naam = st.selectbox("Zwemmer", ["Lars", "Sophie", "Mo", "Emma"])
    slag = st.selectbox("Slag", ["50m Vrij", "50m School", "100m Wissel"])
    tijd = st.text_input("Tijd (bijv. 32.45)")
    if st.button("Voeg toe"):
        st.session_state.data.append({"Naam": naam, "Slag": slag, "Tijd": tijd, "Datum": datetime.now().strftime("%d-%m")})
        st.success("Tijd opgeslagen!")

else:
    st.header("Resultaten")
    if st.session_state.data:
        st.table(pd.DataFrame(st.session_state.data))
    else:
        st.info("Nog geen tijden ingevoerd.")
        
