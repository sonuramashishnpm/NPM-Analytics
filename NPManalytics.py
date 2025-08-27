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

# ---------------- Google Sheets Section ----------------
st.write("📄 Place Your Order / Save Data to Google Sheet")

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]

# ---------------- Google Sheets Credentials Hardcoded ----------------
gcp_service_account = {
    "type": "service_account",
    "project_id": "mythic-delight-462310-g7",
    "private_key_id": "80815affd458a8035db5d5f47e670c502db34749",
    "private_key": """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC4sshIDgCaTa+X
H9yVUA9iZXRItXAf9WG1U3LsCQBzyWmKlg8mYhSl4Bc2PfPXkpMi/Awkc9Zy9DQX
...
xpm3yHwE97NbPOSu4621jks=
-----END PRIVATE KEY-----""",
    "client_email": "npmsimco@mythic-delight-462310-g7.iam.gserviceaccount.com",
    "client_id": "106573975290558922848",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/npmsimco@mythic-delight-462310-g7.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

creds = ServiceAccountCredentials.from_json_keyfile_dict(gcp_service_account, scope)
client = gspread.authorize(creds)
sheet_name = "NPM_Data"

# Try to open sheet, else create
try:
    sheet = client.open(sheet_name).sheet1
except gspread.SpreadsheetNotFound:
    sheet = client.create(sheet_name).sheet1
    sheet.share(gcp_service_account["client_email"], perm_type='user', role='writer')
    st.info(f"📄 Sheet '{sheet_name}' created automatically!")

# Inputs for Google Sheet
company_name = st.text_input("Enter Your Company Name:")
resource = st.text_input("Enter Resource you want:")
quantity = st.number_input("Enter Quantity", min_value=1, step=1)

if st.button("Submit Order"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([now, company_name, resource, quantity])
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
