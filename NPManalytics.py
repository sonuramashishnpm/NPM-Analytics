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
    sales = df["Category"].value_counts().iloc[0]
    market = df["Category"].value_counts().iloc[1]
    interest = df["Category"].value_counts().iloc[2]
    executive_salaries = df["Category"].value_counts().iloc[3]
    contract = df["Category"].value_counts().iloc[4]
    fees = df["Category"].value_counts().iloc[5]
    taxes = df["Category"].value_counts().iloc[6]
    executive_poaching = df["Category"].value_counts().iloc[7]
    bonds = df["Category"].value_counts().iloc[8]
    value = [sales, market, interest, executive_salaries, contract, fees,
             taxes, executive_poaching, bonds]
    label = ["Sales", "Market", "Interest", "Executive Salaries", "Contracts", "Fees", "Taxes",
             "Executive Poaching", "Bonds"]
    plt.figure(figsize=(13, 6))
    plt.bar(label, value, color="g")
    plt.xticks(rotation=45)
    plt.title(titlename, size=40, color="g")
    plt.xlabel("Category", size=30, color="b")
    plt.ylabel("Data", size=30, color="b")
    st.pyplot(plt)

# ---------------- Google Sheets Section ----------------
st.write("If you want to order something")

# ---------------- Using Streamlit Secrets ----------------
# Store your service account JSON in Streamlit secrets.toml
# Example: [gcp_service_account]
#          type = "service_account"
#          project_id = "my-project"
#          private_key_id = "..."
#          private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
#          client_email = "npmsimco@mythic-delight-462310-g7.iam.gserviceaccount.com"
#          client_id = "..."
#          auth_uri = "https://accounts.google.com/o/oauth2/auth"
#          token_uri = "https://oauth2.googleapis.com/token"
#          auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
#          client_x509_cert_url = "..."
secrets_dict = st.secrets["gcp_service_account"]

creds = ServiceAccountCredentials.from_json_keyfile_dict(secrets_dict,
                                                         ["https://spreadsheets.google.com/feeds",
                                                          "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(creds)
sheet_name = "NPM_Data"

# Try to open sheet, else create
try:
    sheet = client.open(sheet_name).sheet1
except gspread.SpreadsheetNotFound:
    sheet = client.create(sheet_name).sheet1
    sheet.share(secrets_dict["client_email"], perm_type='user', role='writer')
    st.info(f"📄 Sheet '{sheet_name}' created automatically!")

# Inputs for Google Sheet
resource = st.text_input("Enter Resource you want:")
quantity = st.number_input("Enter Quantity", min_value=1, step=1)

if st.button("Submit Order"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([now, resource, quantity])
    st.success("✅ Order added to Google Sheet!")

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
        location = geocoder.description_for_number(parsed, "en")
        st.write(f"**Location:** {location}")
        sim_carrier = carrier.name_for_number(parsed, "en")
        st.write(f"**Carrier:** {sim_carrier}")
        tz = timezone.time_zones_for_number(parsed)
        st.write(f"**Timezone:** {tz}")

        st.subheader("📌 Formatted Numbers")
        st.write("International:", phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
        st.write("National:", phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL))
        st.write("E.164:", phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164))

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# ---------------- IP / Location Section ----------------
st.write("Your Location")

# .text usage explained:
# requests.get(url) returns a Response object
# .text reads the body as a plain string
ip = requests.get("https://api.ipfy.org").text

# Get location info using IP in JSON format
response = requests.get(f"https://ipinfo.io/{ip}/json").json()
st.write(response)
