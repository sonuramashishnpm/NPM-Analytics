# NPM-Analytics

NPM-Analytics is a collection of tools and code snippets for data analytics, built using Python and Streamlit. This project aims to help you analyze accounting data, visualize charts, store analytics data in Google Sheets, extract phone number information, and even check your IP/location—all in one place.

---

## 🚀 Features

- **CSV Analytics & Visualization:** Upload your accounting CSV file and visualize key categories (Sales, Market, Interest, Fees, Taxes, etc.) in an interactive bar chart.
- **Google Sheets Integration:** Place orders or save custom data directly to a Google Sheet, using built-in Google Cloud service account credentials.
- **Phone Number Lookup:** Enter a phone number (with country code) to get details like validity, carrier, region, and time zone.
- **IP & Location Info:** Instantly fetch your public IP and geolocation using IP-based APIs.
- **Simple Streamlit UI:** All interactive features are accessible via a clean Streamlit app interface.

---
## To understand repo project with AI in detail with full documentation visit here:-
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/sonuramashishnpm/NPM-Analytics)

## 🛠 Technologies Used

- **Python 3**
- **Streamlit** for the web interface
- **Pandas** for CSV and data handling
- **Matplotlib** for plotting charts
- **Google Sheets API (gspread, oauth2client)** for cloud-based storage
- **phonenumbers** for phone number parsing
- **requests** for web APIs

---

## 📂 File Structure

```
NPM-Analytics/
│
├── NPManalytics.py    # Main Streamlit app with all features
├── README.md
├── LICENSE
```

---

## 🏁 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sonuramashishnpm/NPM-Analytics.git
   cd NPM-Analytics
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If requirements.txt is missing, install: streamlit, pandas, matplotlib, gspread, oauth2client, phonenumbers, requests)*

3. **Run the app:**
   ```bash
   streamlit run NPManalytics.py
   ```

---

## 📊 Usage Overview

- **CSV Charting:** Upload your CSV file with a 'Category' column. The app counts occurrences of each category and generates a bar chart.
- **Google Sheets:** Enter your company name, resource, and quantity to submit data straight to a Google Sheet.
- **Phone Number Info:** Input a phone number to see its location, carrier, and formatted versions.
- **IP/Location:** The app automatically fetches and displays your IP and geolocation.

---

## 📄 License

MIT License © Sonu Kumar (Ramashish)  
See [LICENSE](LICENSE) for details.

---

Enjoy analyzing your data with NPM-Analytics! Contributions and suggestions are always welcome.
