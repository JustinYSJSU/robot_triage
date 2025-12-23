# Robotics Log Triage

## Objective
A diagnostic tool designed to improve Root Cause Analysis (RCA) for an autonomous system.. This tool analyzes raw telemetry .log from an autonomous system and identifies system failures across Perception, Navigation, Acuators, and Power components.


## Features 
## Folder / File Structure
- `src/` -> Contains files for log generation and log triage
  - `generate_logs.py` -> File for generating robot telemetry logs
  - `triage.py` -> File for "triaging" the give telemetry logs. Returns analytics for mission time, log result distribution, and log results by component
- `app.py` -> File for streamlit app. Displays triage data via streamlit charts.
- `requirements.txt` -> File containing project dependencies.
