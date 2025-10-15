# 🔧 TROUBLESHOOTING GUIDE - GUI Won't Launch

## Problem
When clicking `launch_gui.bat` or `launch_gui.vbs`, the tkinter GUI doesn't load and the command window closes immediately.

## Solutions Applied

### ✅ Fixed Files

1. **`scrcpy_gui.py`** - Made subprocess STARTUPINFO cross-platform compatible
2. **`launch_gui.bat`** - Improved error handling and user feedback
3. **`launch_gui.vbs`** - Now properly calls `launch_gui_silent.bat`
4. **`launch_gui_debug.bat`** - NEW! Debug launcher with detailed error messages

### 🎯 How to Fix Your Issue

#### Step 1: Run the Debug Launcher
Double-click **`launch_gui_debug.bat`** 

This will:
- ✅ Show all error messages
- ✅ Keep the console window open
- ✅ Display what's happening at each step
- ✅ Tell you exactly what's wrong

#### Step 2: Check Common Issues

**Issue: "tkinter NOT found"**
```bash
# Fix for conda:
conda activate aisa_env
conda install tk

# Fix for pip:
pip install tk
```

**Issue: "Python NOT found"**
- Edit `env_config.json`
- Make sure environment name is correct
- Try running: `conda env list` to see available environments

**Issue: "scrcpy_gui.py not found"**
- Make sure all files are in the same folder
- Don't move files separately

**Issue: GUI starts then immediately closes**
- Check if there's a Python syntax error
- Run: `python scrcpy_gui.py` directly to see errors
- Make sure you have all required imports

#### Step 3: Verify Your Environment

Run these commands manually:
```bash
# Activate your environment
conda activate aisa_env

# Check Python
python --version

# Check tkinter
python -c "import tkinter; print('tkinter OK')"

# Try launching GUI directly
python scrcpy_gui.py
```

### 📁 Updated Launcher Files

#### For Debugging (See Errors):
- **`launch_gui_debug.bat`** ⭐ **USE THIS FIRST**
  - Shows everything that's happening
  - Displays all error messages
  - Keeps window open

- **`launch_gui.bat`**
  - Standard launcher with some error messages
  - Good for normal use once everything works

#### For Silent Operation (No Console):
- **`launch_gui_vbs`**
  - Completely silent
  - No console window
  - Use only after confirming everything works

- **`launch_gui_silent.bat`**
  - Alternative silent launcher
  - Reads env_config.json properly

### 🔍 Diagnostic Steps

1. **First time / Having issues?**
   ```
   Run: launch_gui_debug.bat
   Look for errors in red
   Follow the suggestions shown
   ```

2. **Want to test manually?**
   ```
   Open PowerShell or CMD
   cd C:\Users\almae\Desktop\SCREEN
   conda activate aisa_env
   python scrcpy_gui.py
   ```

3. **Check your configuration:**
   ```
   Open: env_config.json
   Verify: environment name matches your conda env
   Test: Run `conda env list` to confirm
   ```

### ⚙️ Environment Configuration

Make sure your `env_config.json` looks like this:

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

**Critical Points:**
- `"name"` must match your actual conda environment name
- `"activate_command"` must use the correct environment name
- For debugging, set `"use_pythonw": false`

### 🚀 Recommended Workflow

```
1. Edit env_config.json (if needed)
   ↓
2. Run launch_gui_debug.bat
   ↓
3. Fix any errors shown
   ↓
4. Once working, use launch_gui.bat or launch_gui.vbs
```

### 📊 Comparison of Launchers

| Launcher | Shows Errors | Console Window | When to Use |
|----------|-------------|----------------|-------------|
| **launch_gui_debug.bat** | ✅ Full | ✅ Stays open | Troubleshooting |
| **launch_gui.bat** | ✅ Some | ✅ Auto-closes | Normal use |
| **launch_gui_silent.bat** | ❌ None | ❌ Hidden | After confirmed working |
| **launch_gui.vbs** | ❌ None | ❌ Hidden | After confirmed working |
| **test_setup.bat** | ✅ Full tests | ✅ Stays open | Deep diagnostics |

### 💡 Quick Fixes

**"GUI worked before but not now"**
```bash
# Your environment might have changed
conda activate aisa_env
conda install tk
```

**"Console closes immediately"**
```bash
# Use debug launcher instead
launch_gui_debug.bat
```

**"Python version mismatch"**
```bash
# Check which Python is being used
python -c "import sys; print(sys.executable)"

# Should point to your conda environment
# Example: C:\Users\almae\.conda\envs\aisa_env\python.exe
```

**"Module not found errors"**
```bash
# Make sure you're in the right environment
conda activate aisa_env

# Install missing packages
conda install tk
```

### 📞 Still Having Issues?

1. Run `test_setup.bat` for comprehensive diagnostics
2. Run `launch_gui_debug.bat` and read all messages
3. Copy the error message you see
4. Check if tkinter is installed: `python -c "import tkinter"`
5. Verify Python path: `python -c "import sys; print(sys.executable)"`

### ✅ Success Checklist

- [ ] `env_config.json` exists and has correct environment name
- [ ] Can run `conda activate aisa_env` without errors
- [ ] `python --version` shows Python is available
- [ ] `python -c "import tkinter"` works without errors
- [ ] `scrcpy_gui.py` exists in the same folder
- [ ] `launch_gui_debug.bat` shows "[OK]" for all checks
- [ ] GUI window appears when running debug launcher

Once all checkmarks are complete, you can use any launcher!

---

**Last Updated:** October 15, 2025
**Version:** 1.1 (Fixed STARTUPINFO compatibility)
