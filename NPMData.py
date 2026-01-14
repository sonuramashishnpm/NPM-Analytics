import streamlit as st
import numpy as np
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from npmai import Ollama

llm=Ollama(
    model="llama3.2",
    temperature=0.3,
)

st.title("NPM Data AI")
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
    
    #data for AI
    sales=df[df["Category"]=="sales"].to_string(index=False)
    market=df[df["Category"]=="market"].to_string(index=False)
    interest=df[df["Category"]=="interest"].to_string(index=False)
    salaries=df[df["Category"]=="executive salaries"].to_string(index=False)
    contracts=df[df["Category"]=="contracts"].to_string(index=False)
    fees=df[df["Category"]=="fees"].to_string(index=False)
    taxes=df[df["Category"]=="taxes"].to_string(index=False)
    executive_poachings=df[df["Category"]=="executive poaching"].to_string(index=False)
    bonds=df[df["Category"]=="bonds"].to_string(index=False)
    
    plt.figure(figsize=(13, 6))
    plt.bar(categories, value, color="g")
    plt.xticks(rotation=45)
    plt.title(titlename, size=40, color="g")
    plt.xlabel("Category", size=30, color="b")
    plt.ylabel("Data", size=30, color="b")
    st.pyplot(plt)


if question:
    prompt=f"""
    Hey you are a Business Analyst and you are going to get some accounting data of a company of simcompanies,
    simcompanies is a business simulation game and here you have like all indutries that exist in real world and there players have to like deal with real players 
    as company and you have to grow your company using a lot of way like reselling and a lot producing retailing as i said you have a lot of industries to work in ok 
    so now this is a data here we have just a data of accounting and just asnwer user as per the data you are getting:
    1.Sales:- data related to sales in Retail shops:- {sales},
    2.Marke:- data related to like buying and selling from exchange market where all players list their respoective products to sell without negotiations:- {market},
    3.Interests:- data related to loans bonds like interest that either they are getting or paying :- {interest},
    4.Salaries:- data related to company executives and empoyees expenditures:- {salaries},
    5.Contracts:- data related to products buy or sell through contracts where negotiatiosn and all are involved:- {contracts},
    6.Fees:- data related to fines and like when we sell things in exchnage then we need to pay 4% of total money including profit like if i have to sell a in 10 dollar in
    market then if product is sold then i need to pay 4 dollar from 10 dollar:- {fees},
    7.Taxes:- data related to Tax and that company pays one important thing is most common tax you cab see in the data is of Company Overhead that means if any company has
    3 Million or plus cash then they companies need to pay a tax and if company want to minimize or freee from tax then they need to hire Chief Financial OfficerL:- {taxes},
    8.Executive Poachings:- data related to Poachings you can understand sometime companies poach executives for various puroises like Marketing, Administration, Finance,
    Technology etc, :- {executive_poachings},
    9.Bonds:- data related to Bonds here you will see the data that companies sold bonds not bought:- {bonds},
    You can see some like information you can get None even beacause some activies might not happen sometimes
    Now you have to tell things as per User Questions related to this data ok so this is the user question: {question}
    """
    response=llm.invoke(prompt)
    st.write(response)



