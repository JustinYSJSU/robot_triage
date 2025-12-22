import datetime
import random
from datetime import timedelta
from pathlib import Path

FILE_PATH_AND_NAME = "../data/robot_data.log"
FILE_LENGTH = 500
COMPONENTS = [
    "PERCEPTION",
    "NAVIGATION",
    "ACTUATORS",
    "POWER"
]

p = Path("../data/robot_data.log")
p.parent.mkdir(parents=True, exist_ok=True)

COMPONENT_STATUS_MESSAGES = {
    "PERCEPTION":{
        "INFO": [f"Object detection active - {random.randint(1,5)} objects in view", 
                 f"Lidar spinning at {random.randint(60,100)}Hz - publishing point cloud", 
                 f"Camera exposure normalized - confidence score: {random.randint(0,100)}",
                 f"Scanning for Waypoint markers... complete"],
        "WARN":[f"Lidar point cloud density below threshold - distance {random.randint(10,20)}m",
                f"Sun glare detected on Front_Camera - reducing confidence threshold]",
                f"High latency in bounding box projection: {random.randint(100,200)}ms"],
        "ERROR":["Lidar sensor timeout - no data on /scan topic",
                 "Obstruction detected: Sensor lens obscured or dirty",
                 "Perception pipeline crash - auto-restart sequence initiated"]
    },
    "NAVIGATION":{
        "INFO":[f"Route calculated to Waypoint_{random.randint(1,10)} - distance: {round(random.uniform(1.0, 15.0), 1)}m", 
                f"GPS Fix: 3D Fix acquired - satellites: {random.randint(5,10)}",
                "Global costmap updated successfully",
                f"Executing turn sequence - target angle: {round(random.uniform(10.0, 45.0), 1)}°"],
        "WARN":[f"Deviation from planned path: {round(random.uniform(1.0, 5.0), 1)}m",
                f"GPS signal weak - tall buildings nearby (HDOP: {round(random.uniform(2.0, 3.0), 1)}",
                f"Re-planning route due to static obstacle at coord [{random.randint(0, 99)}, {random.randint(0,99)}."],
        "ERROR":["Path planning failed: No valid route found to target",
                 f"Global localization lost - particle filter divergence > {random.randint(10,50)}",
                 "IMU calibration drift detected - navigation suspended"],
    },
    "ACTUATORS":{
        "INFO":["Motor torque nominal on all 4 drives",
                "Brake pressure check passed - system ready",
                "Steering actuator aligned to zero-point"],
        "WARN":[f"Motor_{random.randint(1,4)} temperature rising: {round(random.uniform(70.0, 100.0), 1)}°C",
                "Slight friction detected in Steering_Rack - check alignment",
                f"Non-critical vibration detected in Drive_Train - frequency {random.randint(60,100)}Hz"],
        "ERROR":[f"Motor_{random.randint(1,4)} over-current: {random.randint(350,500)}A - engaging E-Stop",
                 f"Brake fluid pressure below safety threshold: {random.randint(19,29)}psi",
                 "Steering actuator unresponsive to command - Hardware Fault"]
    },
    "POWER":{
        "INFO":[f"Battery Level: {round(random.uniform(60.0,100.0), 1)}% - voltage stable",
                f"Cooling fans active - current RPM: {random.randint(500,600)}",
                "Power distribution board (PDB) reporting healthy rails"],
        "WARN":[f"Low battery warning: {round(random.uniform(10.0, 30.0), 1)}% remaining",
                f"Cell imbalance detected in Bank_{random.randint(1,5)}: {random.randint(50,100)}V difference", 
                f"High power draw from PERCEPTION suite - {random.randint(100,200)}W"],
        "ERROR":[f"Critical voltage drop: {random.randint(100,150)}V - system shutdown imminent",
                "Battery temperature exceeded 90°C - Safety Cutoff triggered",
                f"Internal short detected in Power_Module_{random.randint(1,5)}"]
    }
}

# [TIMESTAMP][STATUS][COMPONENT][MESSAGE]

with p.open('w') as file:
    utc_timestamp = datetime.datetime.now(datetime.timezone.utc)
    for x in range (0,FILE_LENGTH):
        component = random.choice(COMPONENTS)

        component_status = ""
        component_message = ""
        status_probability = round(random.random(), 2)
        
        if status_probability < 0.9:
            component_status = "INFO"
        elif status_probability < 0.97:
            component_status = "WARN"
        else:
            component_status = "ERROR"

        # triage logic for component + status -> message

        if component == 'PERCEPTION':
            if component_status == 'INFO':
                component_message = random.choice(COMPONENT_STATUS_MESSAGES['PERCEPTION']['INFO'])
            elif component_status == 'WARN':
                component_message = random.choice(COMPONENT_STATUS_MESSAGES['PERCEPTION']['WARN'])
            else:
                component_message = random.choice(COMPONENT_STATUS_MESSAGES['PERCEPTION']['ERROR'])
        elif component == 'NAVIGATION':
            if component_status == 'INFO':
                component_message = random.choice(COMPONENT_STATUS_MESSAGES['NAVIGATION']['INFO'])
            elif component_status == 'WARN':
                component_message = random.choice(COMPONENT_STATUS_MESSAGES['NAVIGATION']['WARN'])
            else:
                component_message = random.choice(COMPONENT_STATUS_MESSAGES['NAVIGATION']['ERROR'])
        elif component == 'ACTUATORS':
            if component_status == 'INFO':
                component_message = random.choice(COMPONENT_STATUS_MESSAGES['ACTUATORS']['INFO'])
            elif component_status == 'WARN':
                component_message = random.choice(COMPONENT_STATUS_MESSAGES['ACTUATORS']['WARN'])
            else:
                component_message = random.choice(COMPONENT_STATUS_MESSAGES['ACTUATORS']['ERROR'])
        else:
            if component_status == 'INFO':
                component_message = random.choice(COMPONENT_STATUS_MESSAGES['POWER']['INFO'])
            elif component_status == 'WARN':
                component_message = random.choice(COMPONENT_STATUS_MESSAGES['POWER']['WARN'])
            else:
                component_message = random.choice(COMPONENT_STATUS_MESSAGES['POWER']['ERROR'])
        file.write(f"{utc_timestamp} | {component_status} | {component} | {component_message} \n")
        utc_timestamp += timedelta(seconds=random.randint(5, 10))
        
        

        



        

