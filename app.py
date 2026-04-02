# import the libaries
import streamlit as st
import pandas as pd
import yfinance as yf
import matplot.lib.pyplot as plt

# Set the pag title and layout
st.set_page_config(page_title = "Stock Data Extraction App", layout="wide")

# Main title of the app
st.title("Stock Data Extraction App")

# Short description under the title
st.write("Extract stock market data from Yahoo Finance using a ticker symbol.")

# Sidebar Header
st.sidebar.header("User Input")

# Input box for stock ticker
ticker = st.sidebar.text_input("Enter a ticker symbol", "AAPL")

# Input for start date
start_date = st.sidebar.date_input("Start date", pd.to_datetime("2023-01-01"))

# Input for end date
end_date = st.sidebar.date_input("End date", pd.to_datetime("today"))

# from prompt_toolkit.shortcuts import set_title
# Download data button
if st.sidebar.button("Get Data"):

# Create ticker object
  stock = yf.Ticker(ticker)

  # Download historical price data
  data = stock.history(start=start_date, end=end_date)
  # Check if data exists
  if df.empty:
    st.error("No data found. Please check the ticker symbol or date range. ")
  else:
    # Show success menu
    st.success(f"Data successfully extracted for {ticker}")

    # Display company information
    st.subheader("Company Information")
    info = stock.info

    company_name = info.get("longName", "N/A")
    sector = info.get("sector", "N/A")
    industry = info.get("industry", "N/A")
    market_cap = info.get("marketCap", "N/A")
    website = info.get("website", "N/A")

    st.write(f"**Company Name:** {company_name}")
    st.write(f"**Sector:** {sector}")
    st.write(f"**Industry:** {industry}")
    st.write(f"**Market Cap:** {market_cap}")
    st.write(f"**Website:** {website}")

    # Display stock data
    st.subheader("Historical Stock Data")
    st.dataframe(df)

    # Plot closing price
    st.subheader("Closing Price")
    fig, ax = plt.subplots()
    ax.plot(df.index, df["Close"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price")
    ax.set_title(f"{ticker} Closing Price")
    st.pyplot(fig)

    # Convert dataframe to CSV for download

  csv = df.to_csv().encode("utf-8")

