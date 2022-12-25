# Import Libraries 
import UI
import streamlit as st

import numpy as np
import matplotlib.pyplot as plt
import math

import cv2
from PIL import Image
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +==================================================================================

# Set Page configuration
st.set_page_config('Christmas AI',page_icon='🎅')
UI.add_bg_from_local('Images\santa.png')



# Make It show
col1,col2=st.columns(2)

if col1.button('make it snow'):
    note=open('Jingle-Bells-3.mp3','rb')
    st.audio(note,format='audio/mp3',start_time=20)
    import time
    for i in range(20):
        st.snow()
        time.sleep(1)
else:
    UI.write('M♥e♥r♥r♥y♥ ♥C♥h♥r♥i♥s♥t♥m♥a♥s',padding=150,color='red',bg='green',fontsize=30,textalign='center')



# +============================================
# Image Processing
# ++++++++++++++++++++++++++++++++++++++++++++++++

UI.write('Take a picture to get a christmas themed Picture',padding=0,color='green',bg='red')
picture = st.camera_input(' ',)

# To read the image file buffer as a PIL Image and convert it to a NumPy array:
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

if picture:
    UI.write('Success',tag='p',fontsize=50,fontweight='bold',color='green',padding=None,bg='red')
    
    #Store Array in Image
    img = Image.open(picture)
    img_array = np.array(img)
    plt.imsave('Images/image.jpg',img_array)

    import Age_detection as ad

    # Get age and gender prediction
    x,y=ad.predict_age_and_gender('image.jpg')
    UI.write(f'Age: {x[1:-1]} years')
    UI.write(f'Gender: {y}')

# except:
    UI.write('𝔄𝔪𝔞𝔷𝔦𝔫𝔤!!!',padding=0,bg='#e52b50',fontsize=20,color='green')

#++================================= =============
# Detecting Age and gender
#================================================
