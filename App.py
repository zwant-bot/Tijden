import streamlit as st
import pandas as pd
from datetime import datetime

# App Styling
st.set_page_config(page_title="SwimClub Manager", page_icon="🏊‍♂️")
st.title("🏊‍♂️ SwimClub Manager")

# Sidebar voor navigatie
menu = st.sidebar.selectbox("Ga naar:", ["Presentielijst", "Tijden Tracker", "Ledenoverzicht"])

# Voorbeeld data (dit zou normaal uit een database komen)
if 'zwemmers' not in st.session_state:
    st.session_state.zwemmers = ["Lars", "Sophie", "Mo", "Emma", "Thomas"]
if 'tijden' not in st.session_state:
    st.session_state.tijden = []

# --- SCHERM 1: PRESENTIELIJST ---
if menu == "Presentielijst":
    st.header("📍 Presentie - " + datetime.now().strftime("%d-%m-%Y"))
    presentie = {}
    
    for zwemmer in st.session_state.zwemmers:
        presentie[zwemmer] = st.checkbox(f"{zwemmer} is aanwezig", key=zwemmer)
    
    if st.button("Presentie Opslaan"):
        st.success("De presentie is succesvol bijgewerkt!")

# --- SCHERM 2: TIJDEN TRACKER ---
elif menu == "Tijden Tracker":
    st.header("⏱️ Tijden Registreren")
    
    with st.form("tijd_form"):
        zwemmer = st.selectbox("Selecteer zwemmer", st.session_state.zwemmers)
        slag = st.selectbox("Slag", ["50m Vrije Slag", "100m Vrije Slag", "50m Schoolslag", "50m Rugslag"])
        tijd = st.text_input("Tijd (bijv. 00:32.45)")
        submit = st.form_submit_button("Tijd opslaan")
        
        if submit and tijd:
            st.session_state.tijden.append({"Naam": zwemmer, "Slag": slag, "Tijd": tijd, "Datum": datetime.now().date()})
            st.success(f"Tijd voor {zwemmer} toegevoegd!")

    if st.session_state.tijden:
        st.subheader("Laatste Resultaten")
        st.table(pd.DataFrame(st.session_state.tijden))

# --- SCHERM 3: LEDEN ---
elif menu == "Ledenoverzicht":
    st.header("👥 Clubleden")
    nieuw_lid = st.text_input("Naam nieuw lid")
    if st.button("Lid Toevoegen"):
        st.session_state.zwemmers.append(nieuw_lid)
        st.rerun()
    
    st.write("Huidige leden:", ", ".join(st.session_state.zwemmers))
  
