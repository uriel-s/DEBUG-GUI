# Debug GUI 🛠️

Interactive debugging interface for RDT hardware systems with external data upload capabilities.

## Key Features ✨

- 📊 **Real-time Parameter Display** - Temperature, Voltage, Humidity, Resistance
- 📁 **External Data Upload** - CSV file support
- 🎨 **Interactive Graphs** - Color-coded status indicators (Green/Yellow/Red)
- ⚡ **Control Switches** - Including LED panel display
- 📱 **User-friendly Interface** - Streamlit-based with tab navigation

## Quick Setup 🚀

```bash
pip install -r requirements.txt
```

## Launch 

```bash
streamlit run gui/streamlit_debug_gui.py
```

Or use the batch file:
```bash
start.bat
```

## Project Structure 📁

```
debug_gui/
├── gui/                         # User Interface
│   ├── streamlit_debug_gui.py   # Main application
│   ├── control_switches.py     # Switch controls
│   └── led_panel.py            # LED panel
├── src/                        # Core logic
│   └── physical_parameters.py  # Parameter definitions
├── data/                       # Sample data
└── requirements.txt            # Python dependencies
```

## Usage 💡

1. **Launch the application** - `streamlit run gui/streamlit_debug_gui.py`
2. **Upload CSV file** - Click "Browse files" and upload your data
3. **View graphs** - Data displayed with color-coded status
4. **Select parameters** - Use tabs to switch between different parameters

---
*Developed for RDT R&D Systems* 🔬