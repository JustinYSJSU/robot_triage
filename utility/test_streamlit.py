import streamlit as st

def hi():
    st.write("hello!")

st.title("Robot Log Triage")
st.write("Hello world")

st.button("Generate Robot Logs", on_click=hi)