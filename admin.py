import streamlit as st
import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB Client erstellen

uri = "mongodb+srv://" + st.secrets["database"]["user"]+ ":" + st.secrets["database"]["password"] + "@cluster0.0vhlagu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
collection = client["wedding"]["guests"]


st.title("🎉 10 Jahre Roman und Denise 🎉")
st.caption("Das wollen wir mit euch feiern!")

# {
#   _id: "$confirmation", 
#   sum_val:{ $sum: "$guests" }
# }