# -------------------------------------------------------------
# Imports
# -------------------------------------------------------------
import pandas as pd
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Helper Functions for ERP Analysis
# -------------------------------------------------------------

def validate_ints_df(df):
    """
    Ensures that all values in the DataFrame are integers. 
    If non-integer values are found, attempts to convert them to integers.
    
    Parameters:
    -----------
    df : pd.DataFrame
        The input DataFrame to validate and convert.

    Returns:
    --------
    pd.DataFrame
        A DataFrame with all values converted to integers.
    """
    if not pd.api.types.is_integer_dtype(df):
        print(f"Warning: Non-integer values found in file. Attempting to convert.")    
        df = df.apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)
    return df


def plot_averages(df):
    """
    Plots the averaged brain response for each finger.

    Parameters:
    -----------
    df : dict or pd.DataFrame
        Dictionary or DataFrame where each key/column represents a finger (1–5),
        and values/rows represent averaged signal amplitudes over time.

    Returns:
    --------
    None
        Displays the plot of ERP averages.
    """
    # Variables
    figure_start = -200
    figure_end = 1000
    time_points = range(figure_start, figure_end+1) 

    plt.figure(figsize=(14,6))

    for finger, averages in df.items():
        plt.plot(time_points, averages, label=f'Finger {finger}')
    
    plt.xlim(figure_start, figure_end)
    plt.title("ERP Averages For Each Finger")
    plt.xlabel("Time [ms]")
    plt.ylabel("Average Signal Amplitude")
    plt.legend(title = "Finger")
    plt.show()
