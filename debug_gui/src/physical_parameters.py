#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Physical Parameters Configuration
--------------------------------
This file defines the physical parameters and their acceptable thresholds 
for the RS422 communication & hardware monitoring system.

Each parameter includes:
- Normal range: Optimal operating values
- Warning range: Values that require attention but are still functional
- Icon: Visual representation in the interface
- Sample data generation parameters (mean and standard deviation)

These values can be easily updated to match specific hardware requirements.
"""

# Dictionary of physical parameters with their thresholds and display properties
PHYSICAL_PARAMETERS = {
    "Temperature": {
        "unit": "°C",
        "normal_min": 15,
        "normal_max": 35,
        "warning_min": 10,
        "warning_max": 40,
        "icon": "🌡️",
        "mean": 25,       # Mean value for sample data generation
        "std_dev": 5      # Standard deviation for sample data
    },
    "Voltage": {
        "unit": "V",
        "normal_min": 4.8,
        "normal_max": 5.2,
        "warning_min": 4.5,
        "warning_max": 5.5,
        "icon": "⚡",
        "mean": 5.0,
        "std_dev": 0.3
    },
    "Humidity": {
        "unit": "%",
        "normal_min": 30,
        "normal_max": 60,
        "warning_min": 20,
        "warning_max": 70,
        "icon": "💧",
        "mean": 45,
        "std_dev": 10
    },
    "Resistance": {
        "unit": "Ω",
        "normal_min": 95,
        "normal_max": 105,
        "warning_min": 90,
        "warning_max": 110,
        "icon": "Ω",
        "mean": 100,
        "std_dev": 5
    }
}

# Communication parameters
COMMUNICATION_THRESHOLDS = {
    "excellent": 8.0,    # Excellent rate (Mbit/s)
    "good": 5.0,         # Good rate (Mbit/s)
    "fair": 3.0,         # Fair rate (Mbit/s)
    "max_rate": 10.0     # Maximum theoretical rate
}

# Color codes for different statuses
STATUS_COLORS = {
    "normal": "#28a745",    # Green
    "warning": "#ffc107",   # Yellow
    "critical": "#dc3545",  # Red
    "inactive": "#6c757d"   # Gray
}

def get_parameter_thresholds(parameter_name):
    """
    Get thresholds for a specific parameter.
    
    Args:
        parameter_name (str): Name of the parameter
        
    Returns:
        dict: Parameter thresholds or None if not found
    """
    return PHYSICAL_PARAMETERS.get(parameter_name)

def get_all_parameters():
    """
    Get all defined physical parameters.
    
    Returns:
        dict: All physical parameters
    """
    return PHYSICAL_PARAMETERS

def get_status_color(value, parameter_name):
    """
    Get color code for parameter value based on its status.
    
    Args:
        value (float): The parameter value
        parameter_name (str): Name of the parameter
        
    Returns:
        str: Color code for the status
    """
    param = get_parameter_thresholds(parameter_name)
    
    if not param:
        return STATUS_COLORS["inactive"]
        
    if param["normal_min"] <= value <= param["normal_max"]:
        return STATUS_COLORS["normal"]
    elif param["warning_min"] <= value <= param["warning_max"]:
        return STATUS_COLORS["warning"]
    else:
        return STATUS_COLORS["critical"]
