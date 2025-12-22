import streamlit as st
import pandas as pd
import plotly.express as px
from src.generate_logs import generate_logs
from src.triage import calculate_status_by_component, calculate_mission_time, calculate_status_count
from pathlib import Path

st.set_page_config(
    page_title="Robot Triage",
    layout="wide"
)

current_dir = Path(__file__).parent 
p = current_dir / "data" / "robot_data.log"
p.parent.mkdir(parents=True, exist_ok=True)

with st.sidebar:
    st.header("New Mission")
    st.write("Press the button below to simulate real-time telemetry logs.")
    generate_btn = st.button("Generate New Mission", type="primary", use_container_width=True)
    st.divider()

st.title("Robotics Log Triage")
st.markdown("### Mission Diagnostics")
st.divider()

if generate_btn:
    generate_logs(p)
    
    df = pd.read_csv(p, sep='|', names=['timestamp', 'component_status', 'component', 'component_status_message'], encoding='ISO-8859-1')
    
    mission_time = calculate_mission_time(df)
    status_counts = calculate_status_count(df)
    status_by_component = calculate_status_by_component(df)

    st.markdown("#### Mission Performance")
    m_col1, m_col2, m_col3 = st.columns(3)
    
    with m_col1:
        st.metric(label="Total Duration", value=mission_time)
    
    with m_col2:
        error_val = len(df[df['component_status'].str.contains('ERROR')])
        st.metric(label="Total Errors", value=error_val, delta=f"{error_val} issues", delta_color="inverse")

    with m_col3:
        warn_val = len(df[df['component_status'].str.contains('WARN')])
        st.metric(label="Total Warnings", value=warn_val)

    st.divider()

    chart_col1, chart_col2 = st.columns([3, 2])

    with chart_col1:
        st.markdown("#### Status Count by Component")
        plotly_bar_chart = px.bar(
            status_by_component, 
            x=["INFO", "WARN", "ERROR"], 
            y=["NAVIGATION", "ACTUATORS", "PERCEPTION", "POWER"], 
            labels={"value": "Count", "y": "Component"}
        )
        st.plotly_chart(plotly_bar_chart, use_container_width=True)

    with chart_col2:
        st.markdown("#### Status Distribution")
        status_data = df['component_status'].value_counts()
        fig = px.pie(
            values=status_data.values, 
            names=status_data.index,
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig.update_layout(margin=dict(t=20, b=20, l=0, r=0), showlegend=True)
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    st.markdown("#### Mission Logs")
    with st.expander("Click to view raw telemetry logs", expanded=False):
        st.dataframe(df, use_container_width=True, height=500)

else:
    st.warning("Please use the sidebar to generate mission data and begin triage.")
