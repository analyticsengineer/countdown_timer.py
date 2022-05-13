import streamlit as st
import base64
import time

st.header("Count Down Timer App")

file_ = open("image.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="dashboard gif">',
     unsafe_allow_html=True
)


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

except:
      pass



