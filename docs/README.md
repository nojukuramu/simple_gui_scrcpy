# Scrcpy GUI Wrapper

A user-friendly graphical interface for scrcpy that simplifies wireless Android screen mirroring.

## 🎯 Quick Start

**First time?** See **[ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md)** for a quick configuration guide!

**Not sure which file does what?** See **[FILE_GUIDE.md](FILE_GUIDE.md)** for a complete file reference!

1. Edit `env_config.json` to match your Python environment (conda/venv/system)
2. Run `launch_gui.bat` to test
3. Use `launch_gui.vbs` for normal use (no console window)

**Need configuration examples?** See **[CONFIG_EXAMPLES.md](CONFIG_EXAMPLES.md)** for ready-to-use templates!

---

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
- **Python Environment**: Conda, venv, or system Python (configurable)

## Installation

### Step 1: Install Python
1. Download Python from https://www.python.org/downloads/
   **OR** install Anaconda/Miniconda from https://www.anaconda.com/
2. During installation, check "Add Python to PATH"
3. Complete the installation

### Step 2: Install scrcpy
1. Download scrcpy from https://github.com/Genymobile/scrcpy/releases
2. Extract to a folder (e.g., `C:\Program Files\scrcpy-win64-v3.3.1`)
3. Note the installation path

### Step 3: Configure Python Environment
1. Place all files in a folder (e.g., `C:\Users\YourName\Desktop\SCREEN`)
2. **IMPORTANT**: Edit `env_config.json` to match your Python environment
3. See [Python Environment Configuration](#python-environment-configuration) below

### Step 4: Launch the Application
- **With Console** (for troubleshooting): Double-click `launch_gui.bat`
- **Without Console** (clean): Double-click `launch_gui.vbs` or `launch_gui_silent.bat`

## Python Environment Configuration

The application uses `env_config.json` to determine which Python environment to use.

### Configuration File: `env_config.json`

```json
{
    "environment": {
        "type": "conda",
        "name": "aisa_env",
        "activate_command": "conda activate aisa_env"
    },
    "python": {
        "executable": "python",
        "use_pythonw": true
    }
}
```

### Environment Types

#### 1. **Conda Environment** (Anaconda/Miniconda)
```json
{
    "environment": {
        "type": "conda",
        "name": "your_env_name",
        "activate_command": "conda activate your_env_name"
    },
    "python": {
        "executable": "python",
        "use_pythonw": true
    }
}
```

**Example**: If your conda environment is named `myenv`:
```json
{
    "environment": {
        "type": "conda",
        "name": "myenv",
        "activate_command": "conda activate myenv"
    },
    "python": {
        "executable": "python",
        "use_pythonw": true
    }
}
```

#### 2. **Virtual Environment (venv)**
```json
{
    "environment": {
        "type": "venv",
        "name": "my_venv",
        "activate_command": "C:\\path\\to\\your\\venv\\Scripts\\activate"
    },
    "python": {
        "executable": "python",
        "use_pythonw": true
    }
}
```

**Example**: If your venv is at `C:\Projects\myvenv`:
```json
{
    "environment": {
        "type": "venv",
        "name": "myvenv",
        "activate_command": "C:\\Projects\\myvenv\\Scripts\\activate"
    },
    "python": {
        "executable": "python",
        "use_pythonw": true
    }
}
```

#### 3. **System Python** (No environment activation)
```json
{
    "environment": {
        "type": "system",
        "name": "system",
        "activate_command": ""
    },
    "python": {
        "executable": "python",
        "use_pythonw": true
    }
}
```

#### 4. **Custom Environment**
```json
{
    "environment": {
        "type": "custom",
        "name": "custom_env",
        "activate_command": "your_custom_activation_command_here"
    },
    "python": {
        "executable": "python",
        "use_pythonw": true
    }
}
```

### Configuration Options Explained

| Field | Description | Example Values |
|-------|-------------|----------------|
| `type` | Type of Python environment | `"conda"`, `"venv"`, `"system"`, `"custom"` |
| `name` | Name of your environment | `"aisa_env"`, `"myenv"`, `"base"` |
| `activate_command` | Command to activate the environment | `"conda activate myenv"`, `"C:\\path\\to\\venv\\Scripts\\activate"` |
| `use_pythonw` | Use pythonw to hide console window | `true` (recommended), `false` |

### How to Find Your Environment Name

**For Conda:**
```bash
conda env list
```
Look for your environment name in the list.

**For venv:**
Your virtual environment folder name is the environment name.
The activate script is located at: `YourVenvFolder\Scripts\activate`

### Default Configuration

If `env_config.json` doesn't exist, the launcher will create one with these defaults:
- Type: `conda`
- Name: `aisa_env`
- Activate: `conda activate aisa_env`
- Use pythonw: `true`

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
├── scrcpy_gui.py              # Main GUI application
├── env_config.json            # Python environment configuration
├── launch_gui.bat             # Launcher with console (for debugging)
├── launch_gui_silent.bat      # Silent launcher without console
├── launch_gui.vbs             # VBScript silent launcher
├── screen.bat                 # Your original batch file (backup)
├── scrcpy_config.json         # Auto-generated scrcpy settings
└── README.md                  # This file
```

## Configuration Files

### 1. `env_config.json` - Python Environment Settings
Controls which Python environment the application uses.

**Location**: Same folder as the launcher scripts

**Purpose**: 
- Specify Python environment type (conda, venv, system, custom)
- Set environment name and activation command
- Configure console window visibility

**When to Edit**:
- First time setup
- When switching between Python environments
- When moving to a different computer

### 2. `scrcpy_config.json` - Application Settings
Stores scrcpy and device configuration (auto-created by the GUI).

**Location**: Same folder as scrcpy_gui.py

**Purpose**:
- Scrcpy installation path
- ADB path (if different from scrcpy)
- Default device IP address
- Default device port

**When to Edit**:
- Usually edited through the GUI Settings tab
- Can be manually edited if needed

## Troubleshooting

### Environment Configuration Issues

**Problem: "Could not activate conda environment"**
Solution:
- Open `env_config.json` and verify the environment name is correct
- Run `conda env list` to see available environments
- Make sure conda is in your PATH
- Try running `conda activate your_env_name` manually first

**Problem: "Python is not installed or not in PATH"**
Solution:
- Check if Python is installed: Open CMD and type `python --version`
- Verify `env_config.json` has the correct environment settings
- For conda: Make sure conda is initialized in your terminal
- For venv: Check that the activate script path is correct

**Problem: Environment activates but GUI doesn't launch**
Solution:
- Set `"use_pythonw": false` in `env_config.json` to see error messages
- Check if tkinter is installed in your environment:
  - For conda: `conda install tk`
  - For pip: `pip install tk` (usually included with Python)
- Run `launch_gui.bat` (not the silent version) to see detailed errors

### Application Issues

**Problem: "Python is not installed or not in PATH"**
- Install Python from python.org
- Make sure to check "Add Python to PATH" during installation
- Restart your computer after installation

**Problem: "scrcpy not found"**
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
