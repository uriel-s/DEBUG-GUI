"""
System Norms Configuration File for Debug GUI
--------------------------------------------
This file contains the normal operating ranges and warning thresholds
for the physical parameters monitored in the debug GUI.

Each parameter has:
- normal_min, normal_max: The range for normal operation (displayed in green)
- warning_min, warning_max: The range for warning level (displayed in yellow)
- Values outside warning range are considered critical (displayed in red)

These values should be adjusted according to the specific requirements
of the hardware being tested.
"""

# Temperature norms (°C)
TEMPERATURE_NORMS = {
    "normal_min": 15,   # Minimum normal operating temperature
    "normal_max": 35,   # Maximum normal operating temperature
    "warning_min": 10,  # Lower threshold for warning
    "warning_max": 40,  # Upper threshold for warning
    "unit": "°C",
    "icon": "🌡️"
}

# Voltage norms (V) - Assuming 5V system
VOLTAGE_NORMS = {
    "normal_min": 4.8,  # Minimum normal voltage (within 4% of 5V)
    "normal_max": 5.2,  # Maximum normal voltage (within 4% of 5V)
    "warning_min": 4.5, # Lower threshold for warning (within 10% of 5V)
    "warning_max": 5.5, # Upper threshold for warning (within 10% of 5V)
    "unit": "V",
    "icon": "⚡"
}

# Humidity norms (%)
HUMIDITY_NORMS = {
    "normal_min": 30,   # Minimum normal humidity
    "normal_max": 60,   # Maximum normal humidity
    "warning_min": 20,  # Lower threshold for warning
    "warning_max": 70,  # Upper threshold for warning
    "unit": "%",
    "icon": "💧"
}

# Resistance norms (Ω) - Assuming 100Ω component
RESISTANCE_NORMS = {
    "normal_min": 95,   # Minimum normal resistance (within 5%)
    "normal_max": 105,  # Maximum normal resistance (within 5%)
    "warning_min": 90,  # Lower threshold for warning (within 10%)
    "warning_max": 110, # Upper threshold for warning (within 10%)
    "unit": "Ω",
    "icon": "Ω"
}

# All parameters in a single dictionary for easy access
ALL_PARAMETER_NORMS = {
    "Temperature": TEMPERATURE_NORMS,
    "Voltage": VOLTAGE_NORMS,
    "Humidity": HUMIDITY_NORMS,
    "Resistance": RESISTANCE_NORMS
}

# RS422 Communication norms
RS422_NORMS = {
    "excellent_min": 8.0,  # Minimum rate for excellent performance (Mbit/s)
    "good_min": 5.0,       # Minimum rate for good performance (Mbit/s)
    "fair_min": 3.0,       # Minimum rate for fair performance (Mbit/s)
    "max_rate": 10.0,      # Maximum theoretical rate (Mbit/s)
    "success_excellent": 95.0,  # Success rate % for excellent
    "success_good": 80.0,       # Success rate % for good
}
