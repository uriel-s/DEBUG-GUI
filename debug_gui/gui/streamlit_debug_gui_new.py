#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Debug GUI Tool - Streamlit Interface
A simplified, clean debugging interface for RS422 communication and hardware monitoring

Features:
- 8 Colored LEDs status indicators
- 3 Control switches (ON/OFF, EOM, SOM)
- RS422 communication monitoring
- Clear relationship between switches
"""

import streamlit as st
import sys
import os

# Import our modular components
from gui.control_switches import create_control_switches
from gui.led_panel import create_led_panel

# Add src directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

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

    # Main layout with two columns - Controls and LEDs
    col1, col2 = st.columns([1, 1])
    
    with col1:
        create_control_switches()
    
    with col2:
        create_led_panel()
    
    # Footer
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 10px; border-radius: 5px; margin-top: 20px; text-align: center;">
        <p style="margin: 0; font-size: 0.8em;">Debug GUI Tool | RS422 Communication Monitor</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
