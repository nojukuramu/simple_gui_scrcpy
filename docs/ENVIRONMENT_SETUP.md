# Quick Environment Setup Guide

## 🚀 Getting Started

### 1. First Time Setup

1. **Edit `env_config.json`** to match your Python setup
2. **Run `launch_gui.bat`** to test (shows console for errors)
3. **Use `launch_gui.vbs`** for normal use (no console)

---

## 📝 Common Environment Configurations

### ✅ Conda Environment (Default)

**If you use Anaconda/Miniconda:**

1. Find your environment name:
   ```bash
   conda env list
   ```

2. Edit `env_config.json`:
   ```json
   {
       "environment": {
           "type": "conda",
           "name": "YOUR_ENV_NAME_HERE",
           "activate_command": "conda activate YOUR_ENV_NAME_HERE"
       },
       "python": {
           "executable": "python",
           "use_pythonw": true
       }
   }
   ```

**Example** (environment named "myenv"):
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

---

### ✅ Virtual Environment (venv)

**If you use Python venv:**

1. Find your venv folder (e.g., `C:\Projects\myvenv`)

2. Edit `env_config.json`:
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

⚠️ **Important**: Use double backslashes `\\` in paths!

---

### ✅ System Python

**If you use system Python (no virtual environment):**

Edit `env_config.json`:
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

---

## 🔧 Configuration Options

| Option | Description | Values |
|--------|-------------|--------|
| `type` | Environment type | `conda`, `venv`, `system`, `custom` |
| `name` | Environment name | Your environment's name |
| `activate_command` | Activation command | Full command to activate |
| `use_pythonw` | Hide console window | `true` (hide), `false` (show) |

---

## 🎯 Quick Checklist

- [ ] Python is installed
- [ ] Scrcpy is downloaded and extracted
- [ ] `env_config.json` is configured for your environment
- [ ] Test with `launch_gui.bat` first
- [ ] Use `launch_gui.vbs` for everyday use

---

## ❓ Need Help?

**See console errors:**
- Set `"use_pythonw": false` in `env_config.json`
- Run `launch_gui.bat` (not the .vbs file)

**Verify environment:**
- Open CMD/PowerShell
- Run: `conda env list` (for conda)
- Run: `python --version` (to check Python)

**Check configuration:**
- Make sure `env_config.json` exists in the same folder as launchers
- Verify paths use double backslashes: `C:\\path\\to\\folder`
- Environment name matches exactly (case-sensitive)

---

## 📚 Full Documentation

For complete instructions, see **README.md**
