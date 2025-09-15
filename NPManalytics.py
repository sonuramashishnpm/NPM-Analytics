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
    value = [df["Category"].value_counts().get(cat,0) for cat in categories]

    plt.figure(figsize=(13, 6))
    plt.bar(categories, value, color="g")
    plt.xticks(rotation=45)
    plt.title(titlename, size=40, color="g")
    plt.xlabel("Category", size=30, color="b")
    plt.ylabel("Data", size=30, color="b")
    st.pyplot(plt)



# ---------------- Phone Number Info Section ----------------
st.title("📱 Phone Number Info App (NPM)")
number = st.text_input("Enter phone number with country code (e.g. +919876543210):")

if number:
    try:
        parsed = phonenumbers.parse(number, None)
        is_valid = phonenumbers.is_valid_number(parsed)
        is_possible = phonenumbers.is_possible_number(parsed)

        st.subheader("🔍 Number Details")
        st.write(f"**Valid Number:** {is_valid}")
        st.write(f"**Possible Number:** {is_possible}")
        st.write(f"**Location:** {geocoder.description_for_number(parsed, 'en')}")
        st.write(f"**Carrier:** {carrier.name_for_number(parsed, 'en')}")
        st.write(f"**Timezone:** {timezone.time_zones_for_number(parsed)}")

        st.subheader("📌 Formatted Numbers")
        st.write("International:", phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
        st.write("National:", phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL))
        st.write("E.164:", phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164))

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# ---------------- IP / Location Section ----------------
st.write("🌐 Your Location")
ip = requests.get("https://api.ipfy.org").text
response = requests.get(f"https://ipinfo.io/{ip}/json").json()
st.write(response)

