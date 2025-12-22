import streamlit as st
import pandas as pd
from src.generate_logs import generate_logs
from src.triage import calculate_culprits, calculate_mission_time, calculate_status_count
from pathlib import Path


current_dir = Path(__file__).parent 
p = current_dir / "data" / "robot_data.log"
p.parent.mkdir(parents=True, exist_ok=True)


st.title("Robotics Log Triage")

st.write("Hello")
if st.button("Generate Triage", type="primary"):
    generate_logs(p)
    df = pd.read_csv(p, sep='|', names=['timestamp', 'component_status', 'component', 'component_status_message'], encoding='ISO-8859-1')
    calculate_mission_time(df)
    calculate_status_count(df)
    (calculate_culprits(df))

    
