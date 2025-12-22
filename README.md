# Robotics Log Triage

## Objective
- An interactive triage dashboard for (simulated) robotics telemetry logs
- Automatically create randomized triage logs for a robot with the following components:
  - Perception, Navigation, Actuators, Power
- Generate analytics from triage logs regarding:
  - Total Mission Time
  - Distribution of log results 
    - INFO: Standard component behavior
    - WARN: Potentially damaging component behavior
    - ERROR: Damaging component behavior
  - Distribution of log results by component

## Folder / File Structure
- `src/` -> Contains files for log generation and log triage
  - `generate_logs.py` -> File for generating robot telemetry logs
  - `triage.py` -> File for "triaging" the give telemetry logs. Returns analytics for mission time, log result distribution, and log results by component
- `app.py` -> File for streamlit app. Displays triage data via streamlit charts.
- `requirements.txt` -> File containing project dependencies.
