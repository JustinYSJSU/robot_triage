import pandas as pd
from pathlib import Path

def calculate_mission_time(df):
    '''
    Calculate total time of the mission
    
    :param fd: data frame from pandas read_csv
    '''

    # in dataframe, timestamp is type str

    mission_start_time = pd.to_datetime(df['timestamp'].iloc[0]) # from the timestamp column, get the 0th (first) index
    mission_end_time = pd.to_datetime(df['timestamp'].iloc[-1]) # from the timestamp column, get the last index

    duration = mission_end_time - mission_start_time
    seconds = int(duration.total_seconds())
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    mission_time_string = f"{hours} hours {minutes} minutes {seconds} seconds"
    return mission_time_string

def calculate_status_count(df):
    '''
    Calculate total count of each status (INFO, WARN, ERROR)
    
    :param fd: data frame from pandas read_csv
    '''
    status_dict = {}

    for row in df.itertuples():
        if row.component_status in status_dict:
            status_dict[row.component_status] += 1
        else:
            status_dict[row.component_status] = 1
    return status_dict

def calculate_status_by_component(df):
    '''
    Calcualte the frequency of each status by component
    
    :param fd: data frame from pandas read_csv
    '''
    culprit_dict = {"INFO":{}, "WARN":{}, "ERROR":{}}
    
    for row in df.itertuples():
        row_status = row.component_status
        row_component = row.component

        if row_component not in culprit_dict[row_status]:
            culprit_dict[row_status][row_component] = 1
        else:
            culprit_dict[row_status][row_component] += 1
    return pd.DataFrame(data=culprit_dict)




