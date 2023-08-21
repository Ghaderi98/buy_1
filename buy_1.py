import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Title
st.title('Gold Price App')

# Download gold price data
@st.cache
def get_gold_data():
    gold_data = yf.download('GC=F', start='2023-01-01', end='2023-08-20')
    return gold_data

gold_df = get_gold_data()

# Display gold price data
st.subheader('Gold Price Data')
st.write(gold_df)

# Display buy and sell information
st.subheader('Buy and Sell Information')

# Calculate buy and sell based on strategy (e.g., buying on the first day and selling on the last day)
buy_price = gold_df['Close'][0].astype(int)
sell_price = gold_df['Close'][-1].astype(int)
profit = sell_price - buy_price
st.write('Buy Price: $', buy_price)
st.write('Sell Price: $', sell_price)
st.write('Profit: $', profit)

# Plot gold price data
st.subheader('Gold Price Chart')

plt.figure(figsize=(12, 6))
plt.plot(gold_df['Close'])
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.title('Gold Price')
st.pyplot(plt)
