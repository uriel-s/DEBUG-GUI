"""
SSL Table Component for Debug GUI
Displays SSL (Secure Socket Layer) table information for debugging purposes
"""

import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

def generate_ssl_data(rows=10):
    """
    Generate sample SSL connection data for demonstration
    
    Args:
        rows (int): Number of SSL connection rows to generate
        
    Returns:
        pd.DataFrame: DataFrame containing SSL connection information
    """
    # Generate random timestamps within the last hour
    now = datetime.now()
    timestamps = [now - timedelta(minutes=random.randint(1, 60)) for _ in range(rows)]
    timestamps.sort(reverse=True)  # Sort in descending order (most recent first)
    
    # SSL versions
    ssl_versions = ["TLS 1.2", "TLS 1.3", "TLS 1.2", "TLS 1.3", "TLS 1.1", "TLS 1.2"]
    
    # Cipher suites
    cipher_suites = [
        "ECDHE-RSA-AES256-GCM-SHA384",
        "ECDHE-RSA-AES128-GCM-SHA256",
        "DHE-RSA-AES256-GCM-SHA384",
        "AES256-GCM-SHA384",
        "ECDHE-ECDSA-AES256-GCM-SHA384"
    ]
    
    # Connection statuses
    statuses = ["Established", "Closed", "Established", "Terminated", "Established", "Negotiating"]
    status_colors = {
        "Established": "#28a745",  # Green
        "Closed": "#6c757d",       # Gray
        "Terminated": "#dc3545",   # Red
        "Negotiating": "#ffc107"   # Yellow
    }
    
    # Generate source and destination IPs
    source_ips = [f"192.168.1.{random.randint(2, 254)}" for _ in range(rows)]
    dest_ips = [f"10.0.0.{random.randint(1, 100)}" for _ in range(rows)]
    
    # Generate random ports
    source_ports = [random.randint(49152, 65535) for _ in range(rows)]
    dest_ports = [443 if random.random() > 0.3 else random.choice([8443, 4433, 9443]) for _ in range(rows)]
    
    # Create DataFrame
    data = {
        "Timestamp": [ts.strftime("%H:%M:%S") for ts in timestamps],
        "Source IP": source_ips,
        "Source Port": source_ports,
        "Destination IP": dest_ips,
        "Destination Port": dest_ports,
        "SSL Version": [random.choice(ssl_versions) for _ in range(rows)],
        "Cipher Suite": [random.choice(cipher_suites) for _ in range(rows)],
        "Status": [random.choice(statuses) for _ in range(rows)],
        "Status Color": [status_colors[random.choice(statuses)] for _ in range(rows)]
    }
    
    return pd.DataFrame(data)

def create_ssl_table():
    """Create SSL connection table for monitoring SSL/TLS connections"""
    st.markdown("""
    <div style="background: linear-gradient(45deg, #004d40 0%, #00796b 100%); 
                padding: 15px; border-radius: 10px; margin-bottom: 15px;">
        <h3 style="color: white; text-align: center; margin: 0; font-size: 1.3em;">
            🔐 SSL CONNECTION MONITORING
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate SSL connection data
    ssl_data = generate_ssl_data(rows=8)
    
    # Columns for filters and controls
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("##### SSL Version Filter")
        versions = ["All"] + list(ssl_data["SSL Version"].unique())
        selected_version = st.selectbox("Select Version", versions, index=0)
    
    with col2:
        st.markdown("##### Connection Status Filter")
        statuses = ["All"] + list(ssl_data["Status"].unique())
        selected_status = st.selectbox("Select Status", statuses, index=0)
    
    with col3:
        st.markdown("##### Auto-Refresh")
        refresh = st.checkbox("Enable Auto-Refresh", value=False)
        if refresh:
            st.caption("Refreshing every 5 seconds")
    
    # Filter data based on selections
    filtered_data = ssl_data.copy()
    if selected_version != "All":
        filtered_data = filtered_data[filtered_data["SSL Version"] == selected_version]
    if selected_status != "All":
        filtered_data = filtered_data[filtered_data["Status"] == selected_status]
    
    # Format the table with colored status
    st.markdown("""
    <style>
    .ssl-table {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-top: 15px;
    }
    .ssl-table thead {
        background-color: #37474f;
        color: white;
    }
    .ssl-table th, .ssl-table td {
        padding: 10px;
        text-align: left;
        border-bottom: 1px solid #e0e0e0;
    }
    .ssl-table tr:nth-child(even) {
        background-color: #f8f9fa;
    }
    .ssl-table tr:hover {
        background-color: #f1f1f1;
    }
    .status-badge {
        border-radius: 4px;
        padding: 3px 8px;
        font-size: 0.8em;
        font-weight: bold;
        color: white;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Build HTML table
    table_html = """
    <table class="ssl-table">
        <thead>
            <tr>
                <th>Time</th>
                <th>Source</th>
                <th>Destination</th>
                <th>SSL Version</th>
                <th>Cipher Suite</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
    """
    
    # Add table rows
    for _, row in filtered_data.iterrows():
        table_html += f"""
        <tr>
            <td>{row['Timestamp']}</td>
            <td>{row['Source IP']}:{row['Source Port']}</td>
            <td>{row['Destination IP']}:{row['Destination Port']}</td>
            <td>{row['SSL Version']}</td>
            <td style="font-size: 0.9em;">{row['Cipher Suite']}</td>
            <td><span class="status-badge" style="background-color: {row['Status Color']};">{row['Status']}</span></td>
        </tr>
        """
    
    table_html += """
        </tbody>
    </table>
    """
    
    st.markdown(table_html, unsafe_allow_html=True)
    
    # SSL/TLS Security Information
    with st.expander("SSL/TLS Security Information"):
        st.markdown("""
        ### SSL/TLS Protocol Security Ratings
        
        | Protocol | Security | Recommendation |
        | --- | --- | --- |
        | SSL 3.0 | ⚠️ Insecure | Do not use |
        | TLS 1.0 | ⚠️ Insecure | Do not use |
        | TLS 1.1 | ⚠️ Vulnerable | Avoid if possible |
        | TLS 1.2 | ✅ Secure | Recommended |
        | TLS 1.3 | ✅ Highly Secure | Preferred |
        
        ### Cipher Suite Information
        
        Strong cipher suites typically include:
        - ECDHE or DHE for key exchange (forward secrecy)
        - RSA or ECDSA for authentication
        - AES256-GCM for encryption
        - SHA384 for message authentication
        """)
    
    # SSL metrics in cards
    st.markdown("<hr style='margin: 20px 0;'>", unsafe_allow_html=True)
    
    metric_cols = st.columns(4)
    
    with metric_cols[0]:
        active_count = sum(filtered_data["Status"] == "Established")
        st.markdown(f"""
        <div style="border: 1px solid #28a745; border-radius: 5px; padding: 10px; text-align: center;">
            <h4 style="margin: 0; color: #28a745;">Active Connections</h4>
            <p style="font-size: 1.8em; font-weight: bold; margin: 10px 0;">{active_count}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_cols[1]:
        tls12_count = sum(filtered_data["SSL Version"] == "TLS 1.2")
        st.markdown(f"""
        <div style="border: 1px solid #17a2b8; border-radius: 5px; padding: 10px; text-align: center;">
            <h4 style="margin: 0; color: #17a2b8;">TLS 1.2</h4>
            <p style="font-size: 1.8em; font-weight: bold; margin: 10px 0;">{tls12_count}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_cols[2]:
        tls13_count = sum(filtered_data["SSL Version"] == "TLS 1.3")
        st.markdown(f"""
        <div style="border: 1px solid #6f42c1; border-radius: 5px; padding: 10px; text-align: center;">
            <h4 style="margin: 0; color: #6f42c1;">TLS 1.3</h4>
            <p style="font-size: 1.8em; font-weight: bold; margin: 10px 0;">{tls13_count}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_cols[3]:
        other_count = len(filtered_data) - tls12_count - tls13_count
        st.markdown(f"""
        <div style="border: 1px solid #fd7e14; border-radius: 5px; padding: 10px; text-align: center;">
            <h4 style="margin: 0; color: #fd7e14;">Other Versions</h4>
            <p style="font-size: 1.8em; font-weight: bold; margin: 10px 0;">{other_count}</p>
        </div>
        """, unsafe_allow_html=True)
