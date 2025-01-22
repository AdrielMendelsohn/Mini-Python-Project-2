import pandas as pd
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

# Helper Functions

def validate_ints_df(df):
    if not pd.api.types.is_integer_dtype(df):
        print(f"Warning: Non-integer values found in file. Attempting to convert.")    
        df = df.apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)
    return df


def extract_signal_slices(trial_points, ecog_data):
# Group signal slices by finger
    finger_dict = {finger: defaultdict(list) for finger in range(1, 6)}

    for _, row in trial_points.iterrows():
        finger = row['finger']
        start = row['start'] - 200
        end = row['start'] + 1000
        if start >= 0 and end < len(ecog_data):
            signal_slice = list(ecog_data.loc[start:end + 1])  #ecog_data[start:end + 1].tolist()
            finger_dict[finger].append(signal_slice)
        else:
            print(f"Skipping invalid range for finger {finger}: start={start}, end={end}")
            
    return finger_dict

def plot_averages(df):
    figure_start = -200
    figure_end = 1000

    plt.figure(figsize=(14,6))

    time_points = range(figure_start, figure_end+1) 

    for finger, averages in df.items():
        plt.plot(time_points, averages, label=f'Finger {finger}')
    
    plt.xlim(figure_start, figure_end)

    plt.title("ERP Averages For Each Finger")
    plt.xlabel("Time [ms]")
    plt.ylabel("Average Signal Amplitude")
    plt.legend(title = "Finger")
    plt.show()
