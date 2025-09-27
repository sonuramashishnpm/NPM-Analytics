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

st.write("          To Analyze your accounting and create Visualise charts".center(30))

# ---------------- CSV Chart Section ----------------
file_path = st.file_uploader("Upload your CSV file", type="csv")
titlename = st.text_input("Enter Your Chart Title", "My Chart")

if file_path is not None:
    df = pd.read_csv(file_path)
    pd.options.display.max_rows = 1000000
    categories = ["Sales","Market","Interest","Executive Salaries","Contracts","Fees","Taxes",
                  "Executive Poaching","Bonds"]
    value = [df["Type"].value_counts().get(cat,0) for cat in categories]

    plt.figure(figsize=(13, 6))
    plt.bar(categories, value, color="g")
    plt.xticks(rotation=45)
    plt.title(titlename, size=40, color="g")
    plt.xlabel("Category", size=30, color="b")
    plt.ylabel("Data", size=30, color="b")
    st.pyplot(plt)

