# Scrcpy GUI Wrapper# Scrcpy GUI Wrapper



[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)A user-friendly graphical interface for scrcpy that simplifies wireless Android screen mirroring.

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

[![Platform: Windows](https://img.shields.io/badge/platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)## 🎯 Quick Start



A professional, user-friendly graphical interface for [scrcpy](https://github.com/Genymobile/scrcpy) that simplifies wireless Android screen mirroring on Windows.**First time?** See **[ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md)** for a quick configuration guide!



![Scrcpy GUI](https://img.shields.io/badge/GUI-Tkinter-green.svg)**Not sure which file does what?** See **[FILE_GUIDE.md](FILE_GUIDE.md)** for a complete file reference!



---1. Edit `env_config.json` to match your Python environment (conda/venv/system)

2. Run `launch_gui.bat` to test

## 🌟 Features3. Use `launch_gui.vbs` for normal use (no console window)



- **🔌 Easy Connection Management****Need configuration examples?** See **[CONFIG_EXAMPLES.md](CONFIG_EXAMPLES.md)** for ready-to-use templates!

  - Quick connect with IP address and port

  - View and manage paired devices---

  - One-click connection to saved devices

## Features

- **⚙️ Flexible Environment Support**

  - Conda environments✨ **Easy Connection Management**

  - Python virtual environments (venv)- Quick connect with IP and port

  - System Python- View and connect to paired devices

  - Custom environment managers- Wireless ADB pairing support



- **📱 Wireless ADB Pairing**⚙️ **Configuration**

  - Built-in wireless pairing interface for Android 11+- Save scrcpy directory path

  - Step-by-step pairing instructions- Store default device IP and port

  - Real-time pairing status feedback- Persistent settings across sessions



- **💾 Persistent Configuration**📱 **Wireless Pairing**

  - Save scrcpy installation path- Built-in ADB pairing interface

  - Store device IP addresses and ports- Step-by-step guidance

  - Configurable Python environment settings- Real-time pairing output



- **📚 Comprehensive Documentation**📖 **Comprehensive Help**

  - In-app help and troubleshooting- Detailed setup instructions

  - Multiple connection method guides- Troubleshooting guide

  - Detailed setup instructions- Multiple connection methods



---## Requirements



## 📋 Requirements- Windows OS

- Python 3.7 or higher

- **Operating System:** Windows 10/11- scrcpy (includes ADB)

- **Python:** 3.7 or higher (Anaconda/Miniconda recommended)- Android device with USB debugging or Wireless debugging enabled

- **scrcpy:** Latest version ([Download](https://github.com/Genymobile/scrcpy/releases))- **Python Environment**: Conda, venv, or system Python (configurable)

- **Android Device:** USB debugging or Wireless debugging enabled

## Installation

---

### Step 1: Install Python

## 🚀 Quick Start1. Download Python from https://www.python.org/downloads/

   **OR** install Anaconda/Miniconda from https://www.anaconda.com/

### 1. Clone or Download2. During installation, check "Add Python to PATH"

3. Complete the installation

```bash

git clone https://github.com/nojukuramu/simple_gui_scrcpy.git### Step 2: Install scrcpy

cd simple_gui_scrcpy1. Download scrcpy from https://github.com/Genymobile/scrcpy/releases

```2. Extract to a folder (e.g., `C:\Program Files\scrcpy-win64-v3.3.1`)

3. Note the installation path

### 2. Configure Your Environment

### Step 3: Configure Python Environment

Edit `config/env_config.json` to match your Python setup:1. Place all files in a folder (e.g., `C:\Users\YourName\Desktop\SCREEN`)

2. **IMPORTANT**: Edit `env_config.json` to match your Python environment

```json3. See [Python Environment Configuration](#python-environment-configuration) below

{

    "environment": {### Step 4: Launch the Application

        "type": "conda",- **With Console** (for troubleshooting): Double-click `launch_gui.bat`

        "name": "your_env_name",- **Without Console** (clean): Double-click `launch_gui.vbs` or `launch_gui_silent.bat`

        "activate_command": "conda activate your_env_name"

    },## Python Environment Configuration

    "python": {

        "executable": "python",The application uses `env_config.json` to determine which Python environment to use.

        "use_pythonw": true

    }### Configuration File: `env_config.json`

}

``````json

{

### 3. Launch the Application    "environment": {

        "type": "conda",

**First Time (with console for debugging):**        "name": "aisa_env",

```bash        "activate_command": "conda activate aisa_env"

launch_gui.bat    },

```    "python": {

        "executable": "python",

**Normal Use (silent, no console):**        "use_pythonw": true

```    }

Double-click: launch_gui.vbs}

``````



### 4. Configure Scrcpy Path### Environment Types



1. Launch the GUI#### 1. **Conda Environment** (Anaconda/Miniconda)

2. Go to **Settings** tab```json

3. Browse and select your scrcpy installation directory{

4. Click **Save Configuration**    "environment": {

        "type": "conda",

---        "name": "your_env_name",

        "activate_command": "conda activate your_env_name"

## 📁 Project Structure    },

    "python": {

```        "executable": "python",

simple_gui_scrcpy/        "use_pythonw": true

├── 📂 src/                      # Source code    }

│   └── scrcpy_gui.py           # Main GUI application}

│```

├── 📂 launchers/                # Launch scripts

│   ├── launch_gui.bat          # Standard launcher (verbose)**Example**: If your conda environment is named `myenv`:

│   ├── launch_gui_silent.bat   # Silent launcher```json

│   └── launch_gui_debug.bat    # Debug launcher (troubleshooting){

│    "environment": {

├── 📂 config/                   # Configuration files        "type": "conda",

│   └── env_config.json         # Python environment settings        "name": "myenv",

│        "activate_command": "conda activate myenv"

├── 📂 docs/                     # Documentation    },

│   ├── README.md               # Main documentation    "python": {

│   ├── ENVIRONMENT_SETUP.md    # Quick setup guide        "executable": "python",

│   ├── CONFIG_EXAMPLES.md      # Configuration templates        "use_pythonw": true

│   ├── FILE_GUIDE.md           # File reference    }

│   ├── TROUBLESHOOTING_LAUNCH.md}

│   ├── FIXES_APPLIED.md```

│   └── QUICK_REFERENCE.txt     # Cheat sheet

│#### 2. **Virtual Environment (venv)**

├── 📂 tools/                    # Utilities```json

│   ├── test_setup.bat          # Diagnostic tool{

│   └── screen.bat              # Legacy launcher (backup)    "environment": {

│        "type": "venv",

├── launch_gui.bat               # Root launcher (redirects to launchers/)        "name": "my_venv",

├── launch_gui.vbs               # Root VBS launcher (silent)        "activate_command": "C:\\path\\to\\your\\venv\\Scripts\\activate"

├── LICENSE                      # MIT License    },

└── README.md                    # This file    "python": {

```        "executable": "python",

        "use_pythonw": true

---    }

}

## 🎯 Usage```



### Connecting to Your Device**Example**: If your venv is at `C:\Projects\myvenv`:

```json

#### Method 1: USB to Wireless (Easiest){

    "environment": {

1. Connect Android device via USB        "type": "venv",

2. Enable USB debugging on your device        "name": "myvenv",

3. Run in terminal: `adb tcpip 5555`        "activate_command": "C:\\Projects\\myvenv\\Scripts\\activate"

4. Disconnect USB    },

5. Find device IP: Settings → About → Status → IP Address    "python": {

6. In GUI, enter IP and port `5555`, click **Connect**        "executable": "python",

        "use_pythonw": true

#### Method 2: Wireless Pairing (Android 11+)    }

}

1. On device: Settings → Developer Options → Wireless Debugging```

2. Enable and tap "Pair device with pairing code"

3. In GUI, go to **Pair Device** tab#### 3. **System Python** (No environment activation)

4. Enter IP, port, and pairing code```json

5. Click **Pair Device**{

6. After pairing, use the connection IP:port in **Connect** tab    "environment": {

        "type": "system",

---        "name": "system",

        "activate_command": ""

## ⚙️ Configuration    },

    "python": {

### Python Environment Setup        "executable": "python",

        "use_pythonw": true

The application supports multiple Python environment types:    }

}

**Conda (Default):**```

```json

{#### 4. **Custom Environment**

    "environment": {```json

        "type": "conda",{

        "name": "myenv",    "environment": {

        "activate_command": "conda activate myenv"        "type": "custom",

    }        "name": "custom_env",

}        "activate_command": "your_custom_activation_command_here"

```    },

    "python": {

**Virtual Environment:**        "executable": "python",

```json        "use_pythonw": true

{    }

    "environment": {}

        "type": "venv",```

        "name": "myvenv",

        "activate_command": "C:\\path\\to\\venv\\Scripts\\activate"### Configuration Options Explained

    }

}| Field | Description | Example Values |

```|-------|-------------|----------------|

| `type` | Type of Python environment | `"conda"`, `"venv"`, `"system"`, `"custom"` |

**System Python:**| `name` | Name of your environment | `"aisa_env"`, `"myenv"`, `"base"` |

```json| `activate_command` | Command to activate the environment | `"conda activate myenv"`, `"C:\\path\\to\\venv\\Scripts\\activate"` |

{| `use_pythonw` | Use pythonw to hide console window | `true` (recommended), `false` |

    "environment": {

        "type": "system",### How to Find Your Environment Name

        "name": "system",

        "activate_command": ""**For Conda:**

    }```bash

}conda env list

``````

Look for your environment name in the list.

See [`docs/CONFIG_EXAMPLES.md`](docs/CONFIG_EXAMPLES.md) for more examples.

**For venv:**

---Your virtual environment folder name is the environment name.

The activate script is located at: `YourVenvFolder\Scripts\activate`

## 🔧 Troubleshooting

### Default Configuration

### GUI Won't Start

If `env_config.json` doesn't exist, the launcher will create one with these defaults:

1. Run `launchers/launch_gui_debug.bat` to see detailed errors- Type: `conda`

2. Check if tkinter is installed: `python -c "import tkinter"`- Name: `aisa_env`

3. Verify `config/env_config.json` settings- Activate: `conda activate aisa_env`

4. See [`docs/TROUBLESHOOTING_LAUNCH.md`](docs/TROUBLESHOOTING_LAUNCH.md)- Use pythonw: `true`



### Common Fixes## Quick Start



**Missing tkinter:**### First Time Setup

```bash1. Launch the application using `launch_gui.bat`

conda install tk        # For Conda2. Go to the **Settings** tab

pip install tk          # For pip (usually included)3. Click **Browse** next to "Scrcpy Directory"

```4. Select your scrcpy installation folder

5. Enter your default device IP and port (if known)

**Wrong environment:**6. Click **Save Configuration**

```bash

# List conda environments### Connecting Your Device

conda env list

#### Method 1: USB to Wireless (Easiest)

# Edit config/env_config.json with correct name1. Connect your Android device via USB

```2. Enable USB debugging on your device

3. Open Command Prompt and run: `adb tcpip 5555`

**Can't connect to device:**4. Disconnect USB cable

- Ensure device and PC are on same Wi-Fi network5. Find your device's IP address (Settings → About → Status)

- Check wireless debugging is enabled6. In the GUI's **Connect** tab, enter IP and port 5555

- Verify IP address is correct7. Click **Connect to Device**



---#### Method 2: Wireless Pairing (Android 11+)

1. On your device: Settings → Developer Options → Wireless Debugging

## 📚 Documentation2. Enable Wireless Debugging

3. Tap "Pair device with pairing code"

- **[Quick Setup Guide](docs/ENVIRONMENT_SETUP.md)** - Get started in 5 minutes4. In the GUI, go to **Pair Device** tab

- **[Configuration Examples](docs/CONFIG_EXAMPLES.md)** - Ready-to-use templates5. Enter the IP, pairing port, and code from your device

- **[File Guide](docs/FILE_GUIDE.md)** - Understanding the project structure6. Click **Pair Device**

- **[Troubleshooting](docs/TROUBLESHOOTING_LAUNCH.md)** - Common issues and solutions7. After pairing, note the IP:port shown in Wireless Debugging

- **[Quick Reference](docs/QUICK_REFERENCE.txt)** - One-page cheat sheet8. Use these in the **Connect** tab



---## File Structure



## 🛠️ Development```

SCREEN/

### Running from Source├── scrcpy_gui.py              # Main GUI application

├── env_config.json            # Python environment configuration

```bash├── launch_gui.bat             # Launcher with console (for debugging)

# Activate your environment├── launch_gui_silent.bat      # Silent launcher without console

conda activate your_env├── launch_gui.vbs             # VBScript silent launcher

├── screen.bat                 # Your original batch file (backup)

# Install dependencies (if needed)├── scrcpy_config.json         # Auto-generated scrcpy settings

conda install tk└── README.md                  # This file

```

# Run directly

python src/scrcpy_gui.py## Configuration Files

```

### 1. `env_config.json` - Python Environment Settings

### TestingControls which Python environment the application uses.



```bash**Location**: Same folder as the launcher scripts

# Run comprehensive diagnostics

tools/test_setup.bat**Purpose**: 

- Specify Python environment type (conda, venv, system, custom)

# Debug mode with full output- Set environment name and activation command

launchers/launch_gui_debug.bat- Configure console window visibility

```

**When to Edit**:

---- First time setup

- When switching between Python environments

## 🤝 Contributing- When moving to a different computer



Contributions are welcome! Please feel free to submit a Pull Request.### 2. `scrcpy_config.json` - Application Settings

Stores scrcpy and device configuration (auto-created by the GUI).

1. Fork the repository

2. Create your feature branch (`git checkout -b feature/AmazingFeature`)**Location**: Same folder as scrcpy_gui.py

3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)

4. Push to the branch (`git push origin feature/AmazingFeature`)**Purpose**:

5. Open a Pull Request- Scrcpy installation path

- ADB path (if different from scrcpy)

---- Default device IP address

- Default device port

## 📄 License

**When to Edit**:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.- Usually edited through the GUI Settings tab

- Can be manually edited if needed

---

## Troubleshooting

## 🙏 Acknowledgments

### Environment Configuration Issues

- [scrcpy](https://github.com/Genymobile/scrcpy) - The excellent screen mirroring tool this GUI wraps

- [Android Debug Bridge (ADB)](https://developer.android.com/tools/adb) - Android debugging tools**Problem: "Could not activate conda environment"**

Solution:

---- Open `env_config.json` and verify the environment name is correct

- Run `conda env list` to see available environments

## 📞 Support- Make sure conda is in your PATH

- Try running `conda activate your_env_name` manually first

- **Issues:** [GitHub Issues](https://github.com/nojukuramu/simple_gui_scrcpy/issues)

- **Documentation:** See [`docs/`](docs/) folder**Problem: "Python is not installed or not in PATH"**

- **Quick Help:** Run `launchers/launch_gui_debug.bat` for diagnostic infoSolution:

- Check if Python is installed: Open CMD and type `python --version`

---- Verify `env_config.json` has the correct environment settings

- For conda: Make sure conda is initialized in your terminal

## 🔖 Version- For venv: Check that the activate script path is correct



**Version:** 1.1  **Problem: Environment activates but GUI doesn't launch**

**Last Updated:** October 15, 2025  Solution:

**Status:** ✅ Stable- Set `"use_pythonw": false` in `env_config.json` to see error messages

- Check if tkinter is installed in your environment:

---  - For conda: `conda install tk`

  - For pip: `pip install tk` (usually included with Python)

Made with ❤️ for easier Android screen mirroring- Run `launch_gui.bat` (not the silent version) to see detailed errors


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
