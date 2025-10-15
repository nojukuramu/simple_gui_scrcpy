# Project Overview

## 📦 Scrcpy GUI Wrapper - Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    USER INTERACTION LAYER                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  Root Directory Launchers:                                        │
│  • launch_gui.bat  ────►  Redirects to launchers/launch_gui.bat │
│  • launch_gui.vbs  ────►  Redirects to launchers/launch_gui_silent.bat │
│  • setup.bat       ────►  First-time configuration wizard        │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     LAUNCHER LAYER                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  launchers/                                                       │
│  ├── launch_gui.bat         ─┐                                   │
│  ├── launch_gui_silent.bat  ─┼─► Read config/env_config.json    │
│  └── launch_gui_debug.bat   ─┘   Activate Python environment    │
│                                   Launch src/scrcpy_gui.py       │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   CONFIGURATION LAYER                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  config/                                                          │
│  ├── env_config.json          ─► Python environment settings    │
│  └── env_config.json.template ─► Template for users             │
│                                                                   │
│  Auto-generated:                                                 │
│  └── scrcpy_config.json       ─► Scrcpy paths & device settings │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  src/                                                             │
│  └── scrcpy_gui.py  ─► Main GUI Application (Tkinter)           │
│                                                                   │
│      Features:                                                    │
│      • Connect Tab       - Quick device connection               │
│      • Settings Tab      - Configure paths                       │
│      • Pair Device Tab   - Wireless ADB pairing                  │
│      • Help Tab          - Documentation                         │
│                                                                   │
│      Interacts with:                                             │
│      • scrcpy.exe        - Screen mirroring                      │
│      • adb.exe           - Android debugging                     │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     UTILITIES LAYER                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  tools/                                                           │
│  ├── test_setup.bat  ─► Comprehensive diagnostic tests          │
│  └── screen.bat      ─► Legacy launcher (backup)                │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   DOCUMENTATION LAYER                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  docs/                                                            │
│  ├── README.md                 ─► Main documentation             │
│  ├── ENVIRONMENT_SETUP.md      ─► Quick setup guide             │
│  ├── CONFIG_EXAMPLES.md        ─► Configuration templates        │
│  ├── FILE_GUIDE.md             ─► File reference                │
│  ├── TROUBLESHOOTING_LAUNCH.md ─► Launch issues                 │
│  ├── FIXES_APPLIED.md          ─► Changelog of fixes            │
│  └── QUICK_REFERENCE.txt       ─► One-page cheat sheet          │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

## 🔄 Execution Flow

### Standard Launch Flow

```
User double-clicks
launch_gui.vbs
      │
      ▼
Calls launchers/
launch_gui_silent.bat
      │
      ▼
Reads config/
env_config.json
      │
      ▼
Activates Python
environment (conda/venv/system)
      │
      ▼
Launches src/
scrcpy_gui.py with pythonw
      │
      ▼
GUI window appears
(no console)
```

### Debug Launch Flow

```
User double-clicks
launch_gui.bat
      │
      ▼
Calls launchers/
launch_gui_debug.bat
      │
      ▼
Reads config/
env_config.json
      │
      ▼
Displays environment info
in console window
      │
      ▼
Runs diagnostic checks
      │
      ▼
Activates Python
environment
      │
      ▼
Launches src/
scrcpy_gui.py with python
      │
      ▼
GUI window appears
+ Console shows errors
```

## 📊 Data Flow

### Configuration Management

```
User edits               GUI Settings Tab
config/env_config.json   modifies scrcpy_config.json
      │                         │
      ▼                         ▼
Launchers read on       GUI reads on startup
each startup            and saves on changes
      │                         │
      ▼                         ▼
Environment activated   Scrcpy path configured
Python launched         Device settings saved
```

### Device Connection Flow

```
User enters IP:Port
in GUI Connect Tab
      │
      ▼
GUI executes:
adb.exe connect IP:PORT
      │
      ▼
Connection established
      │
      ▼
GUI launches:
scrcpy.exe --tcpip=IP:PORT
      │
      ▼
Screen mirroring active
```

## 🗂️ File Dependencies

```
Root Launchers
│
├─► launchers/launch_gui*.bat
│   │
│   ├─► config/env_config.json
│   │
│   └─► src/scrcpy_gui.py
│       │
│       ├─► scrcpy_config.json (auto-created)
│       │
│       ├─► scrcpy.exe (external)
│       │
│       └─► adb.exe (external)
│
└─► tools/test_setup.bat
    │
    └─► config/env_config.json
```

## 🎨 GUI Architecture

```
ScrcpyGUI Class
│
├─► Notebook Widget (Tabs)
│   │
│   ├─► Connect Tab
│   │   ├─ Quick Connect Frame
│   │   │  ├─ IP Entry
│   │   │  └─ Port Entry
│   │   │
│   │   └─ Paired Devices Frame
│   │      ├─ Devices Listbox
│   │      └─ Action Buttons
│   │
│   ├─► Settings Tab
│   │   ├─ Scrcpy Path Config
│   │   ├─ ADB Path Config
│   │   └─ Default Device Settings
│   │
│   ├─► Pair Device Tab
│   │   ├─ Pairing Instructions
│   │   ├─ IP/Port/Code Inputs
│   │   └─ Pairing Output
│   │
│   └─► Help Tab
│       └─ Complete Documentation
│
└─► Methods
    ├─ load_config()
    ├─ save_config()
    ├─ connect_device()
    ├─ refresh_devices()
    ├─ pair_device()
    └─ run_command()
```

## 🔧 Environment Support Matrix

| Type   | Activation Command           | Use Case                    |
|--------|-----------------------------|-----------------------------|
| conda  | `conda activate env_name`   | Anaconda/Miniconda users    |
| venv   | `path\Scripts\activate`     | Python venv users           |
| system | (none)                      | System-wide Python          |
| custom | User-defined                | Poetry, pipenv, pyenv, etc. |

## 📝 Configuration Priority

```
1. User-edited config/env_config.json
   ↓
2. Auto-generated defaults in launchers
   ↓
3. Hardcoded fallback values
```

## 🚀 Launch Methods Comparison

| Method              | Console | Errors Visible | Use Case           |
|---------------------|---------|----------------|--------------------|
| launch_gui.vbs      | ❌      | ❌             | Daily use          |
| launch_gui.bat      | ✅      | ⚠️ Some        | Normal use         |
| launch_gui_debug.bat| ✅      | ✅ All         | Troubleshooting    |
| test_setup.bat      | ✅      | ✅ All         | Deep diagnostics   |
| setup.bat           | ✅      | ✅ All         | First-time setup   |

---

**Version:** 1.1  
**Architecture:** Modular, layered design  
**Platform:** Windows  
**Language:** Python 3.7+ (GUI), Batch (Launchers)
