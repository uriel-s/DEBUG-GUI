# 🔧 Debug GUI Tool

Professional RS422 communication and hardware monitoring system with visual debugging interface.

## 🚀 Quick Start

**Easy way:** Double-click `start.bat`

**Manual way:**

```bash
python -m streamlit run gui/streamlit_debug_gui.py --server.port 8502
```

## 📤 Using External Data

You can upload external data in CSV format to visualize on the Physical Parameters tab:

1. Go to the "Physical Parameters" tab
2. Select "Upload External Data" option
3. Upload a CSV file with columns: Timestamp, Parameter, Value
4. The system will automatically plot your data with appropriate color coding

A sample CSV file is available in `data/sample_parameters.csv`

Then open: http://localhost:8502

## 📁 Project Structure

```
debug_gui/
├── src/                          # Core logic (future expansion)
├── gui/                          # Streamlit interface
│   └── streamlit_debug_gui.py    # Main GUI application
├── data/                         # CSV/Excel data files (future)
├── requirements.txt              # Dependencies
├── start.bat                     # Easy launcher
└── README.md                     # This file
```

## ✨ Features

### 🚦 **8 Colored LEDs**

- Real-time status indicators
- 3-color system: 🟢 Green (OK), 🟡 Yellow (Warning), 🔴 Red (Error)
- Categories: Power, Temperature, Voltage, RS422, Memory, CPU, I/O, Network

### ⚙️ **3 Control Switches**

1. **ON/OFF** - System power control
2. **EOM** - End of Message detection
3. **SOM** - Start of Message detection

### 📡 **RS422 Communication Monitor**

- Current data rate (up to 10 Mbit/s)
- Valid message count tracking
- Success rate percentage
- Status indicators based on performance

### 📊 **Physical Parameter Graphs**

- **Temperature**: Normal range 18-35°C
- **Voltage**: Normal range 4.5-5.5V
- **Resistance**: Monitored in Ohms
- **Humidity**: Normal range 30-60%
- Real-time graphs with 30-minute history
- Color-coded status based on operational norms
- **External Data Upload**: Import data from CSV files for analysis

### 🔄 **Auto-Refresh**

- Configurable refresh intervals (1-10 seconds)
- Real-time data updates
- Live monitoring capabilities

## 🎨 Color Coding System

- 🟢 **Green**: Normal operation, within acceptable limits
- 🟡 **Yellow**: Warning state, approaching limits
- 🔴 **Red**: Critical state, outside safe operating range

## 🔧 Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Launch the application:

```bash
python -m streamlit run gui/streamlit_debug_gui.py --server.port 8502
```

## 📈 Technical Specifications

- **RS422 Data Rate**: 0.1 - 10 Mbit/s
- **Temperature Range**: -10°C to +60°C (monitoring)
- **Voltage Range**: 3.0V to 7.0V (monitoring)
- **Update Frequency**: 1-10 seconds (configurable)
- **Message Tracking**: Real-time valid/invalid message counts

---

Created for: RDT R&D Hardware Testing  
Last Updated: September 2024
