# Robotics Log Triage

## Objective
- An interactive triage dashboard for (simulated) robotics telemetry logs
- Automatically generate randomized triage logs for a robot with the following components:
  - Perception, Navigation, Actuators, Power
- Generage analytics from triage logs regarding:
  - Total Mission Time
  - Distribution of log results 
    - INFO: Standard component behavior
    - WARN: Potentially damaging component behavior
    - ERROR: Damaging component behavior
  - Distribution of log results by component

