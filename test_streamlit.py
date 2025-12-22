import streamlit as st
from src.generate_logs import generate_logs
from pathlib import Path

current_dir = Path(__file__).parent 
p = current_dir / "data" / "robot_data.log"

p.parent.mkdir(parents=True, exist_ok=True)

st.title("Robotics Log Triage")

generate_logs(p)
