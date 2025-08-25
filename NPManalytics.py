import streamlit as st
import numpy as np
import json
import pandas as pd
import requests
import matplotlib.pyplot as plt
import feedparser
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
mydict={}
Your_Sim_Company_Name=st.text_input("Enter Your Sim-Companies Account Name")
passward=st.number_input("Enter only numbers for passward"))
order=st.text_input("Enter The Product Name and quantity like this :- Product Name, Quantity")
if st.button("Order"):
    mydict["Order Details"]=(Your_Sim_Company_Name,passward,order)
    st.write(mydict)

url='https://feeds.feedburner.com/ndtvnews-top-stories'
feed=feedparser.parse(url)
st.title("NDTV -newspaper")
for entry in feed.entries[:10]:
    st.subheader(entry.title)
    st.write(entry.link)
    st.caption(entry.published)
    














