# Autonomous System Root Cause Analysis (RCA) Tool
## Objective
A diagnostic tool designed to drive Root Cause Analysis (RCA) for an autonomous system. This tool generates and analyzes raw telemetry `.log` files from an autonomous system and identifies system failures across Perception, Navigation, Actuators, and Power components.

## Features 
- Telemetry Log Generation
  - Generate 500 line long `.log` files to simulate autonomous system performance.
  - Each line includes timestamp, component status (`INFO`, `WARN`, `ERROR`), component affected, and component status message.
  - Logs are generaeted with realistic rates for component stauts (90% `INFO`, 7% `WARN`, 3% `ERROR`).
 
- Log Triage
  - Mission Time: Total time taken for mission completion.
  - Status Occurence: Occurance rate of each statue across the given missison.
  - Status by Component: Total number of statues per component.
   
## Folder / File Structure
```
.
├── data/                 # Generated telemetry logs (not committed to repository)
├── src/
│   ├── generate_logs.py  # Log Generation
│   └── triage.py         # Triage + Analysis
├── app.py                # Streamlit
└── requirements.txt      # Dependencies
```
