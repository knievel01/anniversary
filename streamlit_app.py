import streamlit as st
import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB Client erstellen

uri = "mongodb+srv://" + st.secrets["database"]["user"]+ ":" + st.secrets["database"]["password"] + "@cluster0.0vhlagu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
collection = client["wedding"]["guests"]

# Initialisiere einen leeren DataFrame zum Speichern der Daten
st.set_page_config(
    page_title="Hochzeitstag Denise & Roman",
    page_icon="🎉",
    layout="centered"
)

st.header("🎉 10 Jahre Roman & Denise 🎉")
st.subheader("Das wollen wir mit euch feiern!")

st.markdown("🥂 Was: Unseren 10ten Hochzeitstag")
st.markdown("📅 Wann: 21. Juni 2024, ab 19:00 Uhr" )
url = "https://maps.app.goo.gl/ed2jhVbfdBhKe5Tb9"
st.markdown("🏡 Wo: [In der Bunten Mühle,  Buntenweg 47, 33415 Verl](%s)" % url)

# Formular erstellen
with st.form(key='my_form'):
    st.markdown("Um uns die Planung etwas zu vereinfachen, sagt bitte kurz Bescheid ob Ihr kommt oder nicht.")
    st.markdown("Wir freuen uns auf Euch! 🥳")

    name = st.text_input(label='Name')
    confirmation = st.radio(label='Bist du dabei?', options=['Ja', 'Nein'])
    guests = st.number_input(label='Anzahl der Gäste', min_value=1, max_value=10)
    submit_button = st.form_submit_button(label='Abschicken')

    if submit_button:
        new_data = {
            "name": name,
            "confirmation": confirmation,
            "guests": guests
        }
        collection.insert_one(new_data)
        
        if confirmation == 'Ja':
            st.success("Vielen Dank " + name + " für deine Anmeldung. Party on! 😎")
            st.balloons()
        else:   
            st.error("Schade, wir haben dich trotzdem lieb :).")

# {
#   _id: "$confirmation", 
#   sum_val:{ $sum: "$guests" }
# }