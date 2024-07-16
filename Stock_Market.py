import streamlit as st
import yfinance as yf
from  plotly import graph_objects as go




st.title("Stock Market")

if st.button("Guide"):
    st.toast("A website to see the price and details of the digital currency market and to show the candlestick chart of each currency........Powered by Miracle.......")

select = st.selectbox("Crypto", ["BTC-USD", "DOGE-USD", "ETH-USD", "SHIB-USD", "USDT-USD", "LUS-USD", "NOT-USD", "TON11419-USD"])

start = st.date_input("Start Date")
stop = st.date_input("Stop Date")

plot = st.checkbox("Show CandelStick")

if st.button("Select"):
    df = yf.download(select, start = start, end= stop)
    st.write("your Data is ready.....", df)

    if plot:
        candel = go.Figure(go.Candlestick(x = df.index , open = df.Open, high = df.High, close = df.Close, low = df.Low))
        st.plotly_chart(candel)


