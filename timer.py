import streamlit as st
import time
from PIL import Image

# Set page config
st.set_page_config(page_title="Countdown Timer", layout="centered")

# Load and display image
image = Image.open('image.png')
col1, col2 = st.columns(2)
col1.header("⏱️ Countdown Timer App")
col2.image(image)

# Alarm URL (RAW GitHub audio file)
ALARM_URL = "https://raw.githubusercontent.com/analyticsengineer/countdown_timer.py/main/alarm.mp3"

# Initialize session state
if "alarm_triggered" not in st.session_state:
    st.session_state.alarm_triggered = False

# Countdown function
def countdown(total_seconds):
    placeholder = st.empty()
    while total_seconds > 0:
        hrs, rem = divmod(total_seconds, 3600)
        mins, secs = divmod(rem, 60)
        timer = f"{hrs:02d}:{mins:02d}:{secs:02d}"
        placeholder.markdown(f"### ⏳ Time Left: `{timer}`")
        time.sleep(1)
        total_seconds -= 1
    placeholder.markdown("### ⏰ Time's up!")
    st.session_state.alarm_triggered = True  # Mark alarm to play after rerun

# UI for input
st.subheader("Enter Countdown Time")
h_col, m_col, s_col = st.columns(3)

with h_col:
    hours = st.number_input("Hours", min_value=0, max_value=23, step=1, value=0)
with m_col:
    minutes = st.number_input("Minutes", min_value=0, max_value=59, step=1, value=0)
with s_col:
    seconds = st.number_input("Seconds", min_value=0, max_value=59, step=1, value=0)

# Compute total seconds
total_time = hours * 3600 + minutes * 60 + seconds

# Start timer button
if total_time > 0:
    if st.button("Start Timer"):
        st.session_state.alarm_triggered = False  # Reset alarm state
        countdown(total_time)
        st.success("Timer Completed!")
        st.balloons()
else:
    st.info("Please set a valid countdown time.")

# 🔊 Alarm autoplay HTML (only appears after timer completes)
if st.session_state.alarm_triggered:
    st.markdown(f"""
        <audio autoplay>
            <source src="{ALARM_URL}" type="audio/mpeg">
        </audio>
        <p>🔔 Alarm is playing...</p>
    """, unsafe_allow_html=True)
