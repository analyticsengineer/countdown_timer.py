import streamlit as st
import base64
import time
from PIL import Image

# Load and display image
image = Image.open('image.png')
col1, col2 = st.columns(2)
col1.header("⏱️ Countdown Timer App")
col2.image(image)

# Countdown logic
def countdown(total_seconds):
    placeholder = st.empty()
    while total_seconds > 0:
        hrs, remainder = divmod(total_seconds, 3600)
        mins, secs = divmod(remainder, 60)
        timer = f"{hrs:02d}:{mins:02d}:{secs:02d}"
        placeholder.markdown(f"### ⏳ Time Left: `{timer}`")
        time.sleep(1)
        total_seconds -= 1
    placeholder.markdown("### ⏰ Time's up!")

# UI for time input
st.subheader("Enter Countdown Time")
h_col, m_col, s_col = st.columns(3)

with h_col:
    hours = st.number_input("Hours", min_value=0, max_value=23, step=1, value=0)
with m_col:
    minutes = st.number_input("Minutes", min_value=0, max_value=59, step=1, value=0)
with s_col:
    seconds = st.number_input("Seconds", min_value=0, max_value=59, step=1, value=0)

# Calculate total time in seconds
total_time = hours * 3600 + minutes * 60 + seconds

if total_time > 0:
    if st.button("Start Timer"):
        countdown(total_time)
        st.success("Timer Completed!")
        st.balloons()
else:
    st.info("Please set a valid countdown time.")
