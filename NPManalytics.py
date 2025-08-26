import streamlit as st
import numpy as np
import json
import pandas as pd
import requests
import matplotlib.pyplot as plt
import feedparser
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

st.write("          To Analyze your accounting and create Visualise charts".center(30))
file_path= st.file_uploader("Upload your CSV file", type="csv")
titlename = st.text_input("Enter Your Chart Title", "My Chart")
if file_path is not None:
    df=pd.read_csv(file_path)
    pd.options.display.max_rows= 1000000
    sales=df["Category"].value_counts().iloc[0]
    market=df["Category"].value_counts().iloc[1]
    interest=df["Category"].value_counts().iloc[2]
    executive_salaries=df["Category"].value_counts().iloc[3]
    contract=df["Category"].value_counts().iloc[4]
    fees=df["Category"].value_counts().iloc[5]
    taxes=df["Category"].value_counts().iloc[6]
    executive_poaching=df["Category"].value_counts().iloc[7]
    bonds=df["Category"].value_counts().iloc[8]
    value=[sales,market,interest,executive_salaries,contract,fees,
       taxes,executive_poaching,bonds]
    label=["Sales","Market","Interest","Executive Salaries","Contracts","Fees","Taxes",
       "Executive Poaching","Bonds"]  
    plt.figure(figsize=(13,6))
    plt.bar(label,value,color="g")
    plt.xticks(rotation=45)
    plt.title(titlename,size=40,color="g")
    plt.xlabel("Category",size=30,color="b")
    plt.ylabel("Data",size=30,color="b")
    st.pyplot(plt)
st.write("If you want to order something")    
mydict={} 
Your_Sim_Company_Name=st.text_input("Enter Your Sim-Companies Account Name") 
passward=st.number_input("Enter only numbers for passward") 
order=st.text_input("Enter The Product Name and quantity like this :- Product Name, Quantity") 
if st.button("Order"): 
    mydict["Order Details"]=(Your_Sim_Company_Name,passward,order) 
    st.write(mydict) 
    with open("Order.json","w") as f: 
        json.dump(mydict,f)

st.title("📱 Phone Number Info App (NPM)")

# Input from user
number = st.text_input("Enter phone number with country code (e.g. +919876543210):")

if number:
    try:
        parsed = phonenumbers.parse(number, None)

        # Check validity
        is_valid = phonenumbers.is_valid_number(parsed)
        is_possible = phonenumbers.is_possible_number(parsed)

        st.subheader("🔍 Number Details")
        st.write(f"**Valid Number:** {is_valid}")
        st.write(f"**Possible Number:** {is_possible}")

        # Location
        location = geocoder.description_for_number(parsed, "en")
        st.write(f"**Location:** {location}")

        # Carrier
        sim_carrier = carrier.name_for_number(parsed, "en")
        st.write(f"**Carrier:** {sim_carrier}")

        # Timezone
        tz = timezone.time_zones_for_number(parsed)
        st.write(f"**Timezone:** {tz}")

        # Formats
        st.subheader("📌 Formatted Numbers")
        st.write("International:", phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
        st.write("National:", phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL))
        st.write("E.164:", phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164))

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
st.write("Your Location")
ip=requests.get("https://api.ipfy.org").text
response=requests.get(f"https://ipinfo.io/{ip}/json").json()
st.write(response)


    


































