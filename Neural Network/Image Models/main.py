import UI
import streamlit as st

from PIL import Image
import cv2
import tensorflow as tf
import numpy as np

import time
# ++++++++++++++++++++++++++++++++++++++
# Page setup
# ==========================================

UI.add_bg_from_local('Style Background.jpg')

UI.write("NST-Neural Styles Transfer",tag='h1',bg='maroon',fontsize=30)


# ++++++++++++++++++++++++++++++++++++++
# Taking User Upload
# ======================================

col1,col2=st.columns(2)

with col1:
    
    UI.write('Upload your photo',bg='green',fontsize=20,tag='h2')
    image_file = st.file_uploader(" ",type=['jpg'])

    if image_file is not None:

        # col1.write(image_file.name)
        # Open St format to Image format
        img = Image.open(image_file)
        col1.image(img) #Display the image
        cv2.imwrite(img=cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR),filename='im.jpg') #Save the file



with col2:
    
    UI.write('Upload Style photo',bg='green',fontsize=20,tag='h2')
    style_file = st.file_uploader(" ",type=['jpg'],key='style')

    if style_file is not None:

        # col1.write(image_file.name)
        # Open St format to Image format
        sty = Image.open(style_file)
        col2.image(sty) #Display the image
        cv2.imwrite(img=cv2.cvtColor(np.array(sty),cv2.COLOR_RGB2BGR),filename='st.jpg') #Save the file

UI.write('Neural Style transfer image')

but=st.button('press me for Style transfer')

if but:
    import sty
    time.sleep(10)
    st.image('final.jpg')
    
try:
    with open("final.jpg", "rb") as file:
        btn = st.download_button(
                label="Download image",
                data=file,
                file_name="style.png",
                mime="image/png"
            )
except:
    st.write(':)')

UI.write('RESTART THE PAGE FOR NEW IMAGE')