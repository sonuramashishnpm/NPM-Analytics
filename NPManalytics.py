import streamlit as st
import numpy as np
import json
import pandas as pd
import requests
import matplotlib.pyplot as plt
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from npmai import Ollama

llm=Ollama(
    model="llama3.2",
    temperature=0.8,
)


st.write("          To Analyze your accounting and create Visualise charts".center(30))

# ---------------- CSV Chart Section ----------------
file_path = st.file_uploader("Upload your CSV file", type="csv")
titlename = st.text_input("Enter Your Chart Title", "My Chart")
question = st.text_input("Enter your any query related to your data of simco you can ask to NPMAI")



if file_path is not None:
    df = pd.read_csv(file_path)
    pd.options.display.max_rows = 1000000
    categories = ["sales","market","interest","executive salaries","contracts","fees","taxes",
                  "executive poaching","bonds"]
    value = [df["Category"].value_counts().get(cat,0) for cat in categories]

    plt.figure(figsize=(13, 6))
    plt.bar(categories, value, color="g")
    plt.xticks(rotation=45)
    plt.title(titlename, size=40, color="g")
    plt.xlabel("Category", size=30, color="b")
    plt.ylabel("Data", size=30, color="b")
    st.pyplot(plt)


if question:
    response=llm.invoke(question)
    st.write(response)






