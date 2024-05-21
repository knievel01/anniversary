import streamlit as st
import pandas as pd

# Initialisiere einen leeren DataFrame zum Speichern der Daten
data = []

st.title("🎉 Anmeldung zum Hochzeitstag 🎉")
st.caption("🚀 Um uns die Planung etwas zu vereinfachen sagt bitte kurz Bescheid ob Ihr kommt oder nicht.")
st.caption("🤖 Wir freuen uns auf Euch! 🥳")

# Formular erstellen
with st.form(key='my_form'):
    name = st.text_input(label='Name')
    confirmation = st.radio(label='Ich bin dabei', options=['Ja', 'Nein'])
    guests = st.number_input(label='Anzahl der Gäste', min_value=1, max_value=10)
    submit_button = st.form_submit_button(label='Abschicken')

    if submit_button:
        data.append([name, confirmation, guests])  # Füge die Daten zu einer Liste hinzu
        df = pd.DataFrame(data, columns=['Name', 'Confirmation', 'Amount of Guests'])
        # bitte hänge die daten an die datei guests.csv an
        df.to_csv('guests.csv', mode='a', index=False, header=False)
        
        if confirmation == 'Ja':
            st.success("Vielen Dank " + name + " für deine Anmeldung. Wir freuen uns!")
            st.balloons()
        else:   
            st.error("Schade, dass du nicht kommen kannst. Vielleicht klappt es ja beim nächsten Mal.")
