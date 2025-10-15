# Scrcpy GUI Wrapper

A user-friendly graphical interface for scrcpy that simplifies wireless Android screen mirroring.

## Features

✨ **Easy Connection Management**
- Quick connect with IP and port
- View and connect to paired devices
- Wireless ADB pairing support

⚙️ **Configuration**
- Save scrcpy directory path
- Store default device IP and port
- Persistent settings across sessions

📱 **Wireless Pairing**
- Built-in ADB pairing interface
- Step-by-step guidance
- Real-time pairing output

📖 **Comprehensive Help**
- Detailed setup instructions
- Troubleshooting guide
- Multiple connection methods

## Requirements

- Windows OS
- Python 3.7 or higher
- scrcpy (includes ADB)
- Android device with USB debugging or Wireless debugging enabled

## Installation

### Step 1: Install Python
1. Download Python from https://www.python.org/downloads/
2. During installation, check "Add Python to PATH"
3. Complete the installation

### Step 2: Install scrcpy
1. Download scrcpy from https://github.com/Genymobile/scrcpy/releases
2. Extract to a folder (e.g., `C:\Program Files\scrcpy-win64-v3.3.1`)
3. Note the installation path

### Step 3: Setup the GUI
1. Place all files in a folder (e.g., `C:\Users\YourName\Desktop\SCREEN`)
2. Double-click `launch_gui.bat` to start the application

## Quick Start

### First Time Setup
1. Launch the application using `launch_gui.bat`
2. Go to the **Settings** tab
3. Click **Browse** next to "Scrcpy Directory"
4. Select your scrcpy installation folder
5. Enter your default device IP and port (if known)
6. Click **Save Configuration**

### Connecting Your Device

#### Method 1: USB to Wireless (Easiest)
1. Connect your Android device via USB
2. Enable USB debugging on your device
3. Open Command Prompt and run: `adb tcpip 5555`
4. Disconnect USB cable
5. Find your device's IP address (Settings → About → Status)
6. In the GUI's **Connect** tab, enter IP and port 5555
7. Click **Connect to Device**

#### Method 2: Wireless Pairing (Android 11+)
1. On your device: Settings → Developer Options → Wireless Debugging
2. Enable Wireless Debugging
3. Tap "Pair device with pairing code"
4. In the GUI, go to **Pair Device** tab
5. Enter the IP, pairing port, and code from your device
6. Click **Pair Device**
7. After pairing, note the IP:port shown in Wireless Debugging
8. Use these in the **Connect** tab

## File Structure

```
SCREEN/
├── scrcpy_gui.py          # Main GUI application
├── launch_gui.bat         # Launcher script
├── screen.bat             # Your original batch file (kept as backup)
├── scrcpy_config.json     # Auto-generated configuration file
└── README.md              # This file
```

## Configuration File

The application automatically creates `scrcpy_config.json` to store:
- Scrcpy installation path
- ADB path (if different from scrcpy)
- Default device IP address
- Default device port

Example:
```json
{
    "scrcpy_path": "C:\\Program Files\\scrcpy-win64-v3.3.1",
    "device_ip": "192.168.1.2",
    "device_port": "33963",
    "adb_path": ""
}
```

## Troubleshooting

### "Python is not installed or not in PATH"
- Install Python from python.org
- Make sure to check "Add Python to PATH" during installation
- Restart your computer after installation

### "scrcpy not found"
- Go to Settings tab and verify the scrcpy directory path
- Make sure scrcpy.exe exists in that folder

### "Cannot connect to device"
- Ensure device and computer are on the same Wi-Fi network
- Check if wireless debugging is enabled on your device
- Verify the IP address is correct
- Try refreshing devices in the Connect tab

### "Device unauthorized"
- Check your Android device screen
- Accept the authorization popup
- Try connecting again

## Tips

💡 Keep your device and computer on the same Wi-Fi network
💡 Use 5GHz Wi-Fi for better performance
💡 The wireless connection persists until device reboot
💡 You can connect multiple times without re-pairing
💡 Use "Refresh Devices" to see all connected devices

## Support

For scrcpy issues, visit: https://github.com/Genymobile/scrcpy
For ADB documentation: https://developer.android.com/tools/adb

## License

This GUI wrapper is provided as-is. scrcpy is licensed under Apache License 2.0.
