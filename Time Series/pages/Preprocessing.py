import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

data=pd.read_csv('data.csv')

st.write(data)

pd.plotting.lag_plot(data['Close'])
plt.show()
# st.pyplot(fig)

# https://colab.research.google.com/drive/1bNJOy0v7kthRlBUCQ6NtM5YgOu60C34C