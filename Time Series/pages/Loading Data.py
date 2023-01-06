import streamlit as st #Frontend
import yfinance as yf #Get live Data
import plotly.express as px #Interactive Plotting
import plotly.graph_objects as go #Add details for plotly charts
import matplotlib.pyplot as plt #Plotting
import training as tt #Training
import numpy as np #Array


#Set Page Config
st.set_page_config(page_title="Eur/USD", page_icon="pages/eurusd.png",initial_sidebar_state = "expanded")



# Option for majors available
majors=['USDJPY','EURUSD','AUDUSD','EURUSD','GBPUSD','NZDUSD','USDCAD','USDCHF']

# Options for Traading Pair
pair=st.sidebar.selectbox(label='Select the pair you want to trade',options=majors)+"=X"

# Title to be displayed for the page
st.title(pair[:-2]+"!!!")

# Time for fetching data
st.markdown(f"<p style='background-color:darkgreen;padding:5px;color:#f2f3f4;'>Fetching Data</p>",unsafe_allow_html=True)

# =================================================================
# Input function for interval and period
# Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo] 
#  Valid periods: 1d,5d,1wk,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max

# Side Bar Values
# Heading
st.sidebar.write(f"<p style='font-size:15px;background-color:	#5d8aa8;color:	#f2f3f4;'>Parameters to fetch Data</p>",unsafe_allow_html=True)

# Getting the interval data
interval=st.sidebar.selectbox(label='Select Interval',options=('1m', '2m', '5m', '15m', '30m', '60m', '1d', '5d', '1wk', '1mo', '3mo'))

# default period to avoid errors
period='1d'
# # 1m,
if interval =="1m":
    periods=st.sidebar.selectbox(label='Enter Period',options=['1d','5d','1wk'])
# # 2m,5m,15m,30m
elif interval in ["2m",'5m', '15m','30m']:
    period=st.sidebar.selectbox(label='Select Period',options=['1d','5d','1wk','1mo'])
# # 1hr
elif interval in ['60m']:
    period=st.sidebar.selectbox(label='Select Period',options=['1d','5d','1wk','1mo','2mo','3mo','6mo','1y','2y','ytd'])
    # periods=st.selectbox(label='Enter Period',options=['1d','5d','1wk','1mo',])
else:
    period=st.sidebar.selectbox(label='Select Period',options=['1d','5d','1wk','1mo','2mo','3mo','6mo','1y','3y','5y','10y','ytd','max'])

# Fetching data from yfinance website
eur=yf.Ticker(pair)
hist = eur.history(interval=interval,period=period)
eur.history()
hist.to_csv('data.csv')
# Display code on the UI
st.code(f"""
import yfinance as yf
eur=yf.Ticker({pair})
hist = eur.history(interval={interval},period={period})
""")

# ==================================================================
# Candle Stick Chart
# st.write('Candle Stick for Close Column')
fig = go.Figure(data=[go.Candlestick(x=hist.index,
                open=hist['Open'],
                high=hist['High'],
                low=hist['Low'],
                close=hist['Close'])])
fig.update_layout(xaxis_rangeslider_visible=False)

st.write(fig)
 
fig=px.line(data_frame=hist,y='Close')

st.write(fig)
# ===================================================================
# Data Preparation

st.write(f"<p style='font-size:15px;'>Preparing Data</p>",unsafe_allow_html=True)

# Side bar
st.sidebar.write(f"<p style='font-size:15px;background-color:	#5d8aa8;color:	#f2f3f4;'>Parameters for model training</p>",unsafe_allow_html=True)

# capturing lags from user
end=st.sidebar.number_input("Enter how many lags you want to use",value=1,min_value=1,max_value=10,step=1)
# Storing same in sp
sp=end

# Getting future ts for predictions
future=st.sidebar.number_input("Enter how many steps you want to predict in future",value=1,min_value=1,max_value=None,step=1)

# Display code to prepare TS Data 
st.code("""
X=[]
Y=[]
x=hist.Close.dropna().values

for i in range(len(x)):
    end+=1
    if end>=len(x)-1:break
    X.append(x[i:end])
    Y.append(x[end])""")

# Time Series Sequence

# Create Empty list X&Y
X=[]
Y=[]
x=hist.Close.dropna().values

# end=3 #Lags to be considered

for i in range(len(x)):
    # print(end)
    if end>len(x)-future:break
    X.append(x[i:end])
    Y.append(x[end:end+future]) #end+2 to predict two steps in future
    end+=1

# print(X)

# To make sure X and Y are of same size
while True:
# for i in range(len(Y)):
    if len(Y[-1])<future:
        Y.pop(-1)
        X.pop(-1)
    else:break

col1,col2=st.columns(2)






# Preparing Data
X_arr,Y_arr=np.log(np.array(X)),np.log(np.array(Y))
# st.write(X_arr.shape)
X_arr=X_arr.reshape(X_arr.shape[:][0],sp,1)
# st.write(X_arr.shape)
X_train,X_test,y_train,y_test=X_arr[:-100],X_arr[-100:],Y_arr[:-100],Y_arr[-100:]




# Display the data for input and output
with col1:
    st.write('Input data')
    st.write(X[-5:])
    st.write(f'input data shape{X_train.shape}')

with col2:
    st.write('Output data')
    st.write((Y[-5:]))
    st.write(f'output data shape{y_train.shape}')

    
if st.button("""Train the model""",help='click me to train the model'):
    tt.model_training(future=future,sp=sp,X_train=X_train,y_train=y_train)
    st.write('see the training ')

if st.button("""Evaluate the model""",help='click me to eval the model'):
    tt.Evaluation(X_test=X_test,y_test=y_test)
    st.write('see the evalaution')

# try:
if st.button(f"""Get predicition for {interval} interval""",help='click me for prediction'):
    tt.pred(interval=interval,sp=sp,period=period,pair=pair)
    st.write('see the prediction')
# except:
# st.write("idiot train the model first.")

# Set sidebar image config
st.sidebar.image("pages/images.jpg")