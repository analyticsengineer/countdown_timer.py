import streamlit as st
import base64
import time
from PIL import Image

image = Image.open('image.png')

col1, col2 = st.columns(2)

col1.header("Count Down Timer App")
col2.image(image)




def countdown(t):
    while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}: {:02d}'.format(mins, secs)
            st.write(timer, end="\r")
            time.sleep(1)
            t -= 1
try:
   t = st.text_input('Enter the time in seconds: ' )
   countdown(int(float(t)))

   st.write('Timer Completed!')
   st.balloons()

except:
      pass



