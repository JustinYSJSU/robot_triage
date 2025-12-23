# Robotics Log Triage

## Objective
A diagnostic tool designed to drive Root Cause Analysis (RCA) for an autonomous system.. This tool generates and analyzes raw telemetry `.log` files from an autonomous system and identifies system failures across Perception, Navigation, Acuators, and Power components.

## Features 
- Telemetry Log Generation
  - Generate 500 line long `.log` files to simulate autonomous system performance.
  - Each line includes timestamp, component status (`INFO`, `WARN`, `ERROR`), component affected, and component status message.
  - Logs are generaeted with realistic rates for component stauts (90% `INFO`, 7% `WARN`, 3% `ERROR`).
 
- Log Triage
  - Mission Time: Total time taken for mission completion.
  - Status Occurence: Occurate rate of each statue across the given missison.
  - Status by Component: Total number of statues per component.
   
## Folder / File Structure
- `src/` -> Contains files for log generation and log triage.
  - `generate_logs.py` -> File for generating robot telemetry logs.
  - `triage.py` -> File for "triaging" the give telemetry logs. Returns analytics for mission time, log result distribution, and log results by component.
- `app.py` -> File for streamlit app. Displays triage data via streamlit charts.
- `requirements.txt` -> File containing project dependencies.
