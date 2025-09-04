"""
Data Import Component for Debug GUI
Allows uploading external parameter data from CSV files
"""

import streamlit as st
import pandas as pd
import io
import os
from datetime import datetime

# This module is kept for compatibility but most functionality has been moved to the main application file
# The process_external_data function is still used

def create_data_uploader():
    """This function is deprecated. Functionality moved to streamlit_debug_gui.py"""
    st.warning("This component is deprecated. Please use the uploader in the main application.")
    return None

def process_external_data(df, parameter_configs):
    """
    Process external data to match the format needed for visualization
    
    Args:
        df (pd.DataFrame): DataFrame with external data
        parameter_configs (dict): Parameter configurations with thresholds
        
    Returns:
        dict: Processed parameters with data for visualization
    """
    if df is None or df.empty:
        return {}
    
    # Get unique parameters in the uploaded data
    unique_params = df["Parameter"].unique()
    
    # Create processed parameters dictionary
    processed_params = {}
    
    for param in unique_params:
        # Skip if parameter is not in our configuration
        if param not in parameter_configs:
            continue
            
        # Filter data for this parameter
        param_data = df[df["Parameter"] == param].copy()
        
        # Sort by timestamp and get the values
        param_data = param_data.sort_values("Timestamp")
        
        # Get time labels and values
        time_labels = [ts.strftime("%H:%M") for ts in param_data["Timestamp"]]
        values = param_data["Value"].values
        
        # Create parameter data structure
        processed_params[param] = {
            **parameter_configs[param],  # Copy all config parameters
            "data": values,
            "time_labels": time_labels
        }
    
    return processed_params
