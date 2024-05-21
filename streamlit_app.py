

def main():
    import streamlit as st
    import pandas as pd
    from dotenv import load_dotenv

    load_dotenv()
    st.set_page_config(
        page_title="Hochzeitstag Denise & Roman",
        page_icon="💍",
        layout="centered",
        initial_sidebar_state="expanded"
    )
 
    st.header("🎉 10 Jahre - Denise und Roman 🎉")
    st.caption("Um uns die Planung zu vereinfachen, sagt bitte kurz Bescheid, ob ihr kommt und zu wie vielen Personen.")
    st.caption("Wir freuen uns auf euch! 🎉")
    # tanz emoji
    st.caption("💃🕺")
    with st.form("registration_form"):
        st.caption("📝 Bitte füllen Sie das Formular aus und klicken Sie auf 'Anmeldung abschicken'")
        st.title("Anmeldung")
        name = st.text_input("Name")
        confirmation = st.toggle("Wir kommen", ["Ja", "Nein"])
        # Füge ein zu wie vielen Personen du kommst
        people = st.select_slider(
            "Anzahl Personen",
             options=["1", "2", "3", "4", "5", "6"])
        
        submit_button = st.form_submit_button("Abschicken")
        
        json_data = []
        #### Abschicken
        if submit_button:
            if name and confirmation and people:
                json_data = {
                    "name": name,
                    "confirmation": confirmation,
                    "people": people
                }
                
                mongo_write = write_to_mongodb(json_data)

                if mongo_write:
                    #send_email(json_data)   
                    st.success("Danke fürs Bescheid sagen, " + name + ". Wir freuen uns auf euch!")
                    st.balloons()
                else:
                    st.error("Fehler beim Speichern der Daten. Bitte versuch es später noch einmal.")
            else:
                st.error("Bitte füllen Sie die Pflichtfelder aus.")

def write_to_mongodb(json_data):
    # write json_data to mongodb atlas
    import pymongo
    CONNECTION_STRING = "mongodb+srv://XXXX:XXXX@cluster0.ty0skaq.mongodb.net/Cluster0"
    # connect to MongoDB
    print("opening connection to MongoDB")
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client["iok-triathlon-verl"]
    collection = db["registrations"]
    # insert data
    print("inserting data")  
    collection.insert_one(json_data)
    # check if data was inserted
    if collection.find_one(json_data):
        print("Data was inserted")
    else:
        st.write("Data was not inserted")

    # close the connection
    client.close()
    return True

            


if __name__ == "__main__":
    main()
