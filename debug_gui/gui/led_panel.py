"""
Enhanced LED Panel Component for Debug GUI
Large, bold LED indicators with improved visual design
"""

import streamlit as st

def create_led_panel():
    """Create 8 large, prominent colored LEDs status panel"""
    st.markdown("""
    <div style="background: linear-gradient(45deg, #1a237e 0%, #283593 100%); 
                padding: 20px; border-radius: 15px; margin: 10px 0 25px 0; 
                border: 3px solid #0d47a1; box-shadow: 0 8px 20px rgba(13,71,161,0.3);">
        <h3 style="color: white; text-align: center; margin: 0; font-size: 1.5em;">
            💡 SYSTEM STATUS INDICATORS
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Create LED status (example data)
    led_statuses = [
        {"id": 1, "name": "POWER", "status": "green", "description": "System Power OK"},
        {"id": 2, "name": "TEMP", "status": "green", "description": "Temperature Normal"},
        {"id": 3, "name": "VOLTAGE", "status": "yellow", "description": "Voltage Warning"},
        {"id": 4, "name": "RS422", "status": "green", "description": "Communication Active"},
        {"id": 5, "name": "MEMORY", "status": "red", "description": "Memory Error"},
        {"id": 6, "name": "CPU", "status": "green", "description": "CPU Normal"},
        {"id": 7, "name": "I/O", "status": "green", "description": "I/O Ports OK"},
        {"id": 8, "name": "NET", "status": "yellow", "description": "Network Slow"},
    ]
    
    # Display LEDs in a grid with larger indicators
    cols = st.columns(4)
    for i, led in enumerate(led_statuses):
        with cols[i % 4]:
            color_map = {
                "green": "#28a745",
                "yellow": "#ffc107", 
                "red": "#dc3545"
            }
            
            color = color_map[led["status"]]
            glow_intensity = "70" if led["status"] == "green" else "90"
            
            st.markdown(f"""
            <div style="text-align: center; padding: 15px; margin: 10px 5px; 
                     background: linear-gradient(45deg, {color}40, {color}20);
                     border: 3px solid {color}; border-radius: 12px; 
                     box-shadow: 0 5px 15px rgba(0,0,0,0.2);">
                <div style="width: 35px; height: 35px; background-color: {color}; 
                         border-radius: 50%; margin: 0 auto 10px auto; 
                         box-shadow: 0 0 15px {color}{glow_intensity};"></div>
                <div style="font-weight: bold; font-size: 14px; margin: 5px 0;">
                    {led["name"]}
                </div>
                <div style="font-size: 12px; color: #555;">
                    {led["description"]}
                </div>
            </div>
            """, unsafe_allow_html=True)
