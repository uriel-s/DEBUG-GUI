"""
Simplified Control Switch Panel for Debug GUI
Clean and focused UI for the 3 main control switches
"""

import streamlit as st

def create_control_switches():
    """Create 3 simple, clean control switches"""
    
    # Simple Header
    st.markdown("""
    <div style="background-color: #333; color: white; padding: 10px; 
               text-align: center; border-radius: 5px; margin-bottom: 15px;">
        <h3 style="margin: 0; font-size: 1.3em;">🎛️ System Controls</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # System ON/OFF Switch
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("<p style='font-weight: bold; margin-bottom: 0;'>🔌 Main Power</p>", unsafe_allow_html=True)
        system_on = st.toggle("ON/OFF", value=True, key="system_switch")
    
    with col2:
        if system_on:
            st.markdown("""
            <div style="background-color: #28a745; color: white; text-align: center;
                      border-radius: 5px; padding: 5px; margin-top: 23px;">
                🟢 ONLINE
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background-color: #dc3545; color: white; text-align: center;
                      border-radius: 5px; padding: 5px; margin-top: 23px;">
                🔴 OFFLINE
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)
    
    # EOM Switch 
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("<p style='font-weight: bold; margin-bottom: 0;'>📤 EOM</p>", unsafe_allow_html=True)
        st.caption("End of Message Detection")
        eom_enabled = st.toggle("Enable", value=False, key="eom_switch")
    
    with col2:
        if eom_enabled:
            st.markdown("""
            <div style="background-color: #17a2b8; color: white; text-align: center;
                      border-radius: 5px; padding: 5px; margin-top: 23px;">
                ACTIVE
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background-color: #6c757d; color: white; text-align: center;
                      border-radius: 5px; padding: 5px; margin-top: 23px;">
                INACTIVE
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)
    
    # SOM Switch
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("<p style='font-weight: bold; margin-bottom: 0;'>📥 SOM</p>", unsafe_allow_html=True)
        st.caption("Start of Message Detection") 
        som_enabled = st.toggle("Enable", value=True, key="som_switch")
    
    with col2:
        if som_enabled:
            st.markdown("""
            <div style="background-color: #28a745; color: white; text-align: center;
                      border-radius: 5px; padding: 5px; margin-top: 23px;">
                ACTIVE
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background-color: #6c757d; color: white; text-align: center;
                      border-radius: 5px; padding: 5px; margin-top: 23px;">
                INACTIVE
            </div>
            """, unsafe_allow_html=True)
    
    # Only show simple status - no metrics or extra information
    if system_on:
        status = "Active" if (som_enabled or eom_enabled) else "Standby"
        color = "#28a745" if (som_enabled and eom_enabled) else "#ffc107"
    else:
        status = "Offline"
        color = "#dc3545"
        
    st.markdown(f"""
    <div style="margin: 15px 0 5px 0; border: 1px solid {color}; border-radius: 5px; padding: 8px;">
        <p style="text-align: center; margin: 0; color: {color}; font-weight: bold;">
            Communication: {status}
        </p>
    </div>
    """, unsafe_allow_html=True)
