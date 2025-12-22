import pandas as pd
from pathlib import Path

current_dir = Path(__file__).parent.parent # 'root directory'
robot_data = current_dir / "data" / "robot_data.log"

pd.read_csv(robot_data)