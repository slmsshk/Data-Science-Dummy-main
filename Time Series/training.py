
# ================================================================
# Model Training
from keras.models import Sequential
from keras.layers import LSTM,Dense
import matplotlib.pyplot as plt
import streamlit as st
import keras

def model_training(future,X_train,y_train,sp):


    col3,col4,col5=st.columns(3)
    col4.header('Model Training')

    #Architecture
    nn=Sequential(name='Sequence_LSTM')
    nn.add(LSTM(50,activation='relu',input_shape=(sp,1),name='input_layer_lstm'))
    nn.add(Dense(50,name='Hidden_layer_Dense1',activation='LeakyReLU'))
    nn.add(Dense(50,name='Hidden_layer_Dense2'))
    nn.add(Dense(future,name='Output_layer_Dense'))
    nn.compile(loss='mse',optimizer='adam')
    nn.summary(print_fn=lambda x: st.text(x))
    # st.write(f'<p>{nn.summary()}</p>',unsafe_allow_html=True)

    nn.fit(X_train,y_train,epochs=100,batch_size=100)
    nn.save("Trained")

# ========================================================
# st.write()
def Evaluation(X_test,y_test):
    col3,col4,col5=st.columns(3)
    col4.header('Model Evaluation')
    nn=keras.models.load_model('Trained')
    pred=nn.predict(X_test)
    fig,ax=plt.subplots()
    ax.plot(pred[:,-1],label='prediction',color='orange')
    ax.plot(y_test[:,-1],label='Actual',color='red')
    # plt.xticks(hist.index[:-100])
    ax.legend()
    st.pyplot(fig)

def pred(interval,period,sp,pair):
    import yfinance as yf
    import numpy as np
    nn=keras.models.load_model('Trained')
    x=yf.Ticker(pair)
    pp=x.history(interval=interval,period=period).Close[-sp:].values.reshape(1,sp,1)
    # y=x.history(interval=interval,period=period).Close[-sp:].values
    # st.write(type(pp),pp[0])
    predict=nn.predict(pp)
    fig,ax=plt.subplots()
    ax.plot(np.append(pp,values=predict))
    ax.set_xticks([i+1 for i in range(sp)])
    st.write(predict)
    st.pyplot(fig)

    