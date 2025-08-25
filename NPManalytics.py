import streamlit as st
import numpy as np
import json
import pandas as pd
import requests
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
components.html(
    """
    <h2 style="color:purple;">🚀 Welcome to NPM Analytics</h2>
    <p>Upload your file and see magic happen!</p>
    """, height=150
)

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
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

name = st.text_input("Enter Your Email")
age = st.text_input("Enter Your Age")

if name == "Sonu Kumar":
    st.write("Oh you are Sonu i like you")

# Add custom HTML
components.html(
    """
    <h2 style="color:purple;">🚀 Welcome to NPM Analytics</h2>
    <p>Upload your file and see magic happen!</p>
    """, height=150
)

file_path = st.file_uploader("Upload your CSV file", type="csv")
titlename = st.text_input("Enter Your Chart Title", "My Chart")

if file_path is not None:
    df = pd.read_csv(file_path)
    category_counts = df["Category"].value_counts()

    labels = category_counts.index.tolist()
    values = category_counts.values.tolist()

    fig, ax = plt.subplots(figsize=(13,6))
    ax.bar(labels, values, color="g")
    ax.set_title(titlename, size=40, color="g")
    ax.set_xlabel("Category", size=30, color="b")
    ax.set_ylabel("Data", size=30, color="b")
    plt.xticks(rotation=45)

    st.pyplot(fig)
    





