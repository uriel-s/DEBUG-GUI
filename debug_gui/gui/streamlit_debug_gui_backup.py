#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Debug GUI Tool - Streamlit Interface
A simplified, clean debugging interface for RS422 communication and hardware monitoring

Features:
- 8 Colored LEDs status indicators
- 3 Control switches (ON/OFF, EOM, SOM)
- RS422 communication monitoring
- SSL table injection for security monitoring
- Clear relationship between switches
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
from gui.ssl_table import create_ssl_table

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
    tab1, tab2, tab3, tab4 = st.tabs(["🎛️ Controls & Status", "📡 RS422 Communication", "📊 Physical Parameters", "🔐 SSL Monitoring"])
    
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
        
        # Generate sample time series data
        now = datetime.now()
        times = [now - timedelta(minutes=x) for x in range(30, 0, -1)]
        time_labels = [t.strftime("%H:%M") for t in times]
        
        # Get parameters from configuration
        physical_params = get_all_parameters()
        
        # Generate data for each parameter
        parameters = {}
        for name, config in physical_params.items():
            param_data = config.copy()  # Copy the config to avoid modifying the original
            # Generate random data based on parameter's mean and standard deviation
            param_data["data"] = np.random.normal(
                config["mean"], 
                config["std_dev"], 
                30
            )
            parameters[name] = param_data
        
        # Create tabs for each parameter
        param_tabs = st.tabs([f"{param_info['icon']} {param}" for param, param_info in parameters.items()])
        
        for i, (param, param_info) in enumerate(parameters.items()):
            with param_tabs[i]:
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
                
                # Display current value and status
                st.markdown(f"""
                <div style="display: flex; justify-content: space-between; align-items: center; 
                            padding: 15px; border-radius: 10px; border: 2px solid {status_color}; margin-bottom: 15px;">
                    <span style="font-size: 1.3em;">Current Value:</span>
                    <div>
                        <span style="font-size: 1.5em; font-weight: bold;">{current_value:.1f} {param_info['unit']}</span>
                        <span style="display: block; color: {status_color}; font-weight: bold;">{status_text}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
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
                
                # Create and display the plot
                fig = px.line(df, x="Time", y="Value", title=f"{param} Over Time")
                fig.update_layout(
                    height=300,
                    margin=dict(l=20, r=20, t=40, b=20),
                    plot_bgcolor="#f8f9fa",
                    paper_bgcolor="#f8f9fa"
                )
                
                # Add scatter points with colors
                fig.add_scatter(
                    x=df["Time"], 
                    y=df["Value"], 
                    mode="markers", 
                    marker=dict(color=df["Color"], size=8),
                    showlegend=False
                )
                
                # Add threshold lines
                fig.add_hline(y=param_info["normal_max"], line_dash="dash", line_color="#28a745", annotation_text="Normal Max")
                fig.add_hline(y=param_info["normal_min"], line_dash="dash", line_color="#28a745", annotation_text="Normal Min")
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Parameter norms explanation
                st.markdown(f"""
                <div style="background-color: #f8f9fa; border-radius: 10px; padding: 10px; margin-top: 10px;">
                    <h5 style="margin: 0 0 10px 0;">Parameter Norms</h5>
                    <div style="display: flex; margin-bottom: 5px;">
                        <div style="width: 20px; height: 20px; background-color: #28a745; border-radius: 50%; margin-right: 10px;"></div>
                        <span>Normal: {param_info["normal_min"]} - {param_info["normal_max"]} {param_info["unit"]}</span>
                    </div>
                    <div style="display: flex; margin-bottom: 5px;">
                        <div style="width: 20px; height: 20px; background-color: #ffc107; border-radius: 50%; margin-right: 10px;"></div>
                        <span>Warning: {param_info["warning_min"]} - {param_info["warning_max"]} {param_info["unit"]} (excluding normal range)</span>
                    </div>
                    <div style="display: flex;">
                        <div style="width: 20px; height: 20px; background-color: #dc3545; border-radius: 50%; margin-right: 10px;"></div>
                        <span>Critical: Below {param_info["warning_min"]} or above {param_info["warning_max"]} {param_info["unit"]}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # Sidebar with helpful information
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
    
    # Footer with darker color
    st.markdown("""
    <div style="background: linear-gradient(90deg, #2c3e50 0%, #34495e 100%); 
               padding: 12px; border-radius: 5px; margin-top: 20px; text-align: center;">
        <p style="margin: 0; font-size: 0.9em; color: white;">Debug GUI Tool | RS422 Communication Monitor</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
