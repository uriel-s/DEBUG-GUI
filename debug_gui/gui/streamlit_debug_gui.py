#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Debug GUI Tool - Streamlit Interface
A clean, professional debugging interface for RS422 communication and hardware monitoring

Features:
- 8 Colored LEDs status indicators with real-time feedback
- 3 Control switches (ON/OFF, EOM, SOM) for system control
- RS422 communication monitoring with performance metrics
- Physical parameter visualization with status indicators
- External data upload for CSV-based parameter analysis
- Comprehensive parameter threshold monitoring
"""

import streamlit as st
import sys
import os
import numpy as np
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Add src directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import UI components
from led_panel import create_led_panel
from control_switches import create_control_switches

# Import parameter configurations
from physical_parameters import (
    get_all_parameters, 
    get_status_color,
    COMMUNICATION_THRESHOLDS, 
    STATUS_COLORS
)

# Import our modular components
from gui.control_switches import create_control_switches
from gui.led_panel import create_led_panel

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

def main():
    """Main function to run the Streamlit Debug GUI application"""
    # Page configuration
    st.set_page_config(
        page_title="🔧 Debug GUI Tool",
        page_icon="🔧",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Main header
    st.markdown("""
    <div style="background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%); padding: 25px; border-radius: 15px; margin-bottom: 20px;">
        <h1 style="color: white; text-align: center; margin: 0; font-size: 2.5em;">🎛️ CONTROL & DEBUG CENTER</h1>
        <p style="color: #e8f4f8; text-align: center; margin: 15px 0 0 0; font-size: 1.2em;">Professional RS422 Communication & Hardware Monitoring System</p>
    </div>
    """, unsafe_allow_html=True)

    # Create tabs for better organization
    tab1, tab2, tab3 = st.tabs(["🎛️ Controls & Status", "📡 RS422 Communication", "📊 Physical Parameters"])
    
    # Tab 1: Controls and LEDs
    with tab1:
        col1, col2 = st.columns([1, 1])
        with col1:
            create_control_switches()
        with col2:
            create_led_panel()
    
    # Tab 2: RS422 Communication
    with tab2:
        st.markdown("""
        <div style="background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%); 
                  padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <h3 style="color: white; text-align: center; margin: 0;">📡 RS422 Communication Metrics</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Create RS422 metrics - Message rates, validity, etc.
        col1, col2 = st.columns(2)
        
        with col1:
            # Current and Maximum Rates
            current_rate = 8.5  # Simulated value in Mbit/s
            max_rate = COMMUNICATION_THRESHOLDS["max_rate"]  # Maximum specified RS422 rate
            rate_percentage = (current_rate / max_rate) * 100
            
            # Display rate with appropriate color coding based on performance thresholds
            if current_rate >= COMMUNICATION_THRESHOLDS["excellent"]:
                rate_color = STATUS_COLORS["normal"]
            elif current_rate >= COMMUNICATION_THRESHOLDS["good"]:
                rate_color = STATUS_COLORS["warning"]
            else:
                rate_color = STATUS_COLORS["critical"]
            
            st.markdown(f"""
            <div style="border: 2px solid {rate_color}; border-radius: 10px; padding: 15px; margin-bottom: 15px;">
                <h4 style="margin: 0 0 10px 0;">Data Rate</h4>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 1.2em;">Current:</span>
                    <span style="font-size: 1.2em; font-weight: bold; color: {rate_color};">{current_rate:.2f} Mbit/s</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 5px;">
                    <span style="font-size: 1.2em;">Maximum:</span>
                    <span style="font-size: 1.2em; font-weight: bold;">{max_rate:.1f} Mbit/s</span>
                </div>
                <div style="background-color: #e9ecef; border-radius: 5px; height: 15px; margin-top: 10px;">
                    <div style="background-color: {rate_color}; width: {rate_percentage}%; height: 100%; border-radius: 5px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Message validation statistics
            valid_messages = 975    # Simulated value
            total_messages = 1000
            success_rate = (valid_messages / total_messages) * 100
            
            # Color coding based on success rate
            if success_rate >= 95:
                success_color = STATUS_COLORS["normal"]
            elif success_rate >= 80:
                success_color = STATUS_COLORS["warning"]
            else:
                success_color = STATUS_COLORS["critical"]
            
            st.markdown(f"""
            <div style="border: 2px solid {success_color}; border-radius: 10px; padding: 15px;">
                <h4 style="margin: 0 0 10px 0;">Message Validation</h4>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 1.2em;">Valid Messages:</span>
                    <span style="font-size: 1.2em; font-weight: bold; color: {success_color};">{valid_messages}/{total_messages}</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 5px;">
                    <span style="font-size: 1.2em;">Success Rate:</span>
                    <span style="font-size: 1.2em; font-weight: bold; color: {success_color};">{success_rate:.1f}%</span>
                </div>
                <div style="background-color: #e9ecef; border-radius: 5px; height: 15px; margin-top: 10px;">
                    <div style="background-color: {success_color}; width: {success_rate}%; height: 100%; border-radius: 5px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Communication status with color indicators
        st.markdown("<h4>Communication Status</h4>", unsafe_allow_html=True)
        status_cols = st.columns(4)
        
        with status_cols[0]:
            st.markdown("""
            <div style="background-color: #28a745; color: white; text-align: center; 
                       padding: 15px; border-radius: 5px;">
                <h5 style="margin:0;">EXCELLENT</h5>
                <p style="margin:0;">8-10 Mbit/s</p>
            </div>
            """, unsafe_allow_html=True)
            
        with status_cols[1]:
            st.markdown("""
            <div style="background-color: #ffc107; color: white; text-align: center; 
                       padding: 15px; border-radius: 5px;">
                <h5 style="margin:0;">GOOD</h5>
                <p style="margin:0;">5-8 Mbit/s</p>
            </div>
            """, unsafe_allow_html=True)
            
        with status_cols[2]:
            st.markdown("""
            <div style="background-color: #fd7e14; color: white; text-align: center; 
                       padding: 15px; border-radius: 5px;">
                <h5 style="margin:0;">FAIR</h5>
                <p style="margin:0;">3-5 Mbit/s</p>
            </div>
            """, unsafe_allow_html=True)
            
        with status_cols[3]:
            st.markdown("""
            <div style="background-color: #dc3545; color: white; text-align: center; 
                       padding: 15px; border-radius: 5px;">
                <h5 style="margin:0;">POOR</h5>
                <p style="margin:0;">0-3 Mbit/s</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Tab 3: Physical Parameters
    with tab3:
        st.markdown("""
        <div style="background: linear-gradient(90deg, #134e5e 0%, #71b280 100%); 
                  padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <h3 style="color: white; text-align: center; margin: 0;">📊 Physical Parameters</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Initialize parameters dictionary
        parameters = {}
        
        # Get parameters from configuration for reference values
        physical_params = get_all_parameters()
        
        # Clean file uploader interface
        st.markdown("### Upload Parameter Data")
        st.markdown("Upload a CSV file with your parameter measurements.")
                
        # Create two columns for uploader and instructions
        upload_col, info_col = st.columns([2, 1])
        
        with upload_col:
            uploaded_data = st.file_uploader(
                "Select CSV file", 
                type="csv",
                help="File must have columns: Timestamp, Parameter, Value"
            )
            
            if uploaded_data is None:
                st.info("No file uploaded. Please select a CSV file.")
        
        with info_col:
            # Sample data download button
            st.markdown("#### Need a template?")
            sample_data = open("data/sample_parameters.csv", "r").read()
            st.download_button(
                label="Download Sample CSV",
                data=sample_data,
                file_name="sample_parameters.csv",
                mime="text/csv",
            )
            
            st.markdown("**Required format:**")
            st.markdown("""
            - Timestamp (YYYY-MM-DD HH:MM:SS)
            - Parameter (must match system parameters)
            - Value (numeric measurements)
            """)
        
        # Process uploaded data
        if uploaded_data is not None:
            try:
                # Read and validate the CSV
                df = pd.read_csv(uploaded_data)
                
                # Check columns
                required_columns = ["Timestamp", "Parameter", "Value"]
                if not all(col in df.columns for col in required_columns):
                    st.error("CSV file must contain columns: Timestamp, Parameter, Value")
                else:
                    # Convert timestamp to datetime
                    try:
                        df["Timestamp"] = pd.to_datetime(df["Timestamp"])
                        
                        # Process the data
                        parameters = process_external_data(df, physical_params)
                        
                        # If no matching parameters were found
                        if not parameters:
                            st.warning("No matching parameters found in the uploaded data. Make sure parameter names match the system configuration.")
                            st.markdown("**Valid parameter names:** " + ", ".join(physical_params.keys()))
                        else:
                            st.success(f"Successfully loaded data for {len(parameters)} parameters")
                    except:
                        st.error("Could not parse timestamp format. Use YYYY-MM-DD HH:MM:SS format.")
            except Exception as e:
                st.error(f"Error processing file: {str(e)}")
        
        # Show a message if no parameters are available to display
        if not parameters:
            st.warning("No parameter data available. Please upload a CSV file with valid data.")
            
            # Show example parameters for reference
            st.markdown("### Available Parameters")
            st.markdown("Your CSV file should contain data for one or more of the following parameters:")
            
            # Create a nice table of available parameters
            param_info_list = []
            for name, config in physical_params.items():
                param_info_list.append({
                    "Parameter": f"{config['icon']} {name}",
                    "Unit": config["unit"],
                    "Normal Range": f"{config['normal_min']} - {config['normal_max']}"
                })
            
            # Display parameter reference table
            st.dataframe(
                pd.DataFrame(param_info_list),
                hide_index=True,
                use_container_width=True
            )
        
        # Show parameter data with tabs - one parameter per tab
        if parameters:
            # Parameter visualization with tabs
            st.markdown("### Parameter Visualization")
            
            # Get the list of parameters and create tabs
            param_list = list(parameters.keys())
            tab_names = [f"{parameters[param]['icon']} {param}" for param in param_list]
            param_tabs = st.tabs(tab_names)
            
            # Create a tab for each parameter
            for i, param in enumerate(param_list):
                with param_tabs[i]:
                    # Show selected parameter data
                    param_info = parameters[param]
                    data = param_info["data"]
                    current_value = data[-1]
                    
                    # Get status color from the helper function
                    status_color = get_status_color(current_value, param)
                    
                    # Determine status text based on color
                    if status_color == STATUS_COLORS["normal"]:
                        status_text = "NORMAL"
                    elif status_color == STATUS_COLORS["warning"]:
                        status_text = "WARNING"
                    else:
                        status_color = STATUS_COLORS["critical"]
                        status_text = "CRITICAL"
            
                    # Create columns for displaying current value and parameter details
                    curr_col, detail_col = st.columns([1, 2])
                    
                    with curr_col:
                        # Display current value and status
                        st.markdown(f"""
                        <div style="display: flex; flex-direction: column; align-items: center; 
                                    padding: 15px; border-radius: 10px; border: 2px solid {status_color}; height: 100%;">
                            <span style="font-size: 1.2em; margin-bottom: 10px;">Current Value</span>
                            <span style="font-size: 2em; font-weight: bold;">{current_value:.1f}</span>
                            <span style="font-size: 1.2em;">{param_info['unit']}</span>
                            <span style="display: block; color: {status_color}; font-weight: bold; margin-top: 10px;">{status_text}</span>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with detail_col:
                        # Parameter details and ranges
                        st.markdown(f"### {param_info['icon']} {param} Information")
                        st.markdown(f"**Description:** {param_info.get('description', 'Physical parameter measurement')}")
                        
                        # Display parameter ranges in a simpler format
                        st.markdown("**Parameter Ranges:**")
                        st.markdown(f"""
                        - 🟢 **Normal**: {param_info["normal_min"]} - {param_info["normal_max"]} {param_info["unit"]}
                        - 🟡 **Warning**: {param_info["warning_min"]} - {param_info["warning_max"]} {param_info["unit"]} (excluding normal range)
                        - 🔴 **Critical**: Below {param_info["warning_min"]} or above {param_info["warning_max"]} {param_info["unit"]}
                        """)
            
                    # Get time labels from parameter info or use default
                    time_labels = param_info.get("time_labels", [f"Point {i}" for i in range(len(data))])
                    
                    # Generate colors for data points
                    # Get color for each data point based on its value
                    colors = []
                    for val in data:
                        colors.append(get_status_color(val, param))
                    
                    # Create DataFrame for plotting
                    df = pd.DataFrame({
                        "Time": time_labels,
                        "Value": data,
                        "Color": colors
                    })
                            
                    # Create and display the plot with improved styling
                    st.markdown("### Time Series Data")
                    
                    # Options for graph display
                    point_size = st.select_slider("Point size", options=[4, 6, 8, 10, 12], value=8, key=f"size_{param}")
                    
                    # Create the plot
                    fig = px.line(df, x="Time", y="Value", title=f"{param} Measurements Over Time")
                    fig.update_layout(
                        height=400,
                        margin=dict(l=20, r=20, t=40, b=20),
                        plot_bgcolor="#f8f9fa",
                        paper_bgcolor="#f8f9fa",
                        xaxis_title="Time",
                        yaxis_title=f"Value ({param_info['unit']})",
                        font=dict(
                            family="Arial, sans-serif",
                            size=12
                        )
                    )
            
                    # Add scatter points with colors
                    fig.add_scatter(
                        x=df["Time"], 
                        y=df["Value"], 
                        mode="markers", 
                        marker=dict(color=df["Color"], size=point_size),
                        showlegend=False,
                        hovertemplate=f"Time: %{{x}}<br>Value: %{{y:.2f}} {param_info['unit']}<extra></extra>"
                    )
                    
                    # Display the chart
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Additional options for data analysis
                    with st.expander("Data Statistics"):
                        stats_col1, stats_col2, stats_col3 = st.columns(3)
                        with stats_col1:
                            st.metric("Average", f"{np.mean(data):.2f} {param_info['unit']}")
                        with stats_col2:
                            st.metric("Min", f"{np.min(data):.2f} {param_info['unit']}")
                        with stats_col3:
                            st.metric("Max", f"{np.max(data):.2f} {param_info['unit']}")    # Sidebar with helpful information
    st.sidebar.markdown("""
    <div style="background: linear-gradient(45deg, #1e3c72 0%, #2a5298 100%); 
               padding: 15px; border-radius: 10px;">
        <h3 style="color: white; text-align: center; margin: 0; font-size: 1.3em;">ℹ️ Help Information</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.sidebar.markdown("### 📋 Switch Controls")
    st.sidebar.markdown("""
    - **🔌 Main Power**: System power on/off
    - **📤 EOM**: End of Message detection
    - **📥 SOM**: Start of Message detection
    """)
    
    st.sidebar.markdown("### 🚥 System Status")
    system_on = st.session_state.get("system_switch", False)
    eom_state = st.session_state.get("eom_switch", False)
    som_state = st.session_state.get("som_switch", False)
    
    st.sidebar.markdown(f"🔌 System: {'🟢 ACTIVE' if system_on else '🔴 INACTIVE'}")
    st.sidebar.markdown(f"📤 EOM: {'🟢 ENABLED' if eom_state else '⚪ DISABLED'}")
    st.sidebar.markdown(f"📥 SOM: {'🟢 ENABLED' if som_state else '⚪ DISABLED'}")
    
    st.sidebar.markdown("### � Parameter Data")
    st.sidebar.markdown("""
    **Data Sources:**
    
    - **Generate Data**: Creates simulated parameter values within realistic ranges based on normal distributions with defined means and standard deviations.
    
    - **Upload External Data**: Import your own parameter measurements from a CSV file for visualization and analysis.
    
    **CSV Format Requirements:**
    
    - **Timestamp**: Date and time (YYYY-MM-DD HH:MM:SS)
    - **Parameter**: Must match system parameters (Temperature, Voltage, etc.)
    - **Value**: Numeric measurement values
    """)
    
    # Footer with darker color
    st.markdown("""
    <div style="background: linear-gradient(90deg, #2c3e50 0%, #34495e 100%); 
               padding: 12px; border-radius: 5px; margin-top: 20px; text-align: center;">
        <p style="margin: 0; font-size: 0.9em; color: white;">Debug GUI Tool | RS422 Communication Monitor</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
