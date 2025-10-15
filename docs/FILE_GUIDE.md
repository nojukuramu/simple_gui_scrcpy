# 📁 File Guide - What Each File Does

## 🚀 Launcher Files (Pick One to Start the App)

### `launch_gui.vbs` ⭐ RECOMMENDED
- **What it does:** Starts the app with NO console window
- **When to use:** Normal everyday use
- **Pros:** Clean, no command windows
- **Cons:** Can't see error messages if something goes wrong

### `launch_gui_silent.bat`
- **What it does:** Batch file version of silent launcher
- **When to use:** Alternative to .vbs file
- **Pros:** Pure batch, no VBScript
- **Cons:** Brief flash of console window on startup

### `launch_gui.bat`
- **What it does:** Starts the app WITH console window showing
- **When to use:** Troubleshooting, first-time setup, debugging
- **Pros:** Shows detailed status messages and errors
- **Cons:** Console window stays open

---

## ⚙️ Configuration Files (Edit These)

### `env_config.json` ⚙️ IMPORTANT - EDIT THIS FIRST!
- **What it does:** Tells the launcher which Python environment to use
- **When to edit:** 
  - First time setup (REQUIRED)
  - When changing Python environments
  - When switching computers
- **What to configure:**
  - Environment type (conda, venv, system)
  - Environment name
  - Activation command
  - Console visibility preference

**Example content:**
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

### `scrcpy_config.json` (Auto-generated)
- **What it does:** Stores scrcpy installation path and device settings
- **When to edit:** Usually through the GUI Settings tab
- **Auto-created:** Created automatically when you first use the app
- **What it stores:**
  - Scrcpy installation directory
  - Default device IP and port
  - ADB path (if custom)

---

## 🖥️ Application Files (Don't Edit Unless You Know Python)

### `scrcpy_gui.py`
- **What it does:** The main GUI application code
- **Written in:** Python with tkinter
- **Features:**
  - Connect tab - Quick device connection
  - Settings tab - Configure paths
  - Pair Device tab - Wireless ADB pairing
  - Help tab - Complete documentation
- **When to edit:** Only if you want to modify the GUI or add features

---

## 📖 Documentation Files (Read These for Help)

### `README.md` 📘
- **What it is:** Complete documentation
- **Contains:**
  - Full installation guide
  - Environment configuration details
  - All features explained
  - Troubleshooting guide
  - Tips and best practices

### `ENVIRONMENT_SETUP.md` 🚀 Quick Start Guide
- **What it is:** Simplified setup guide
- **Best for:** First-time users
- **Contains:**
  - Step-by-step environment setup
  - Common configurations
  - Quick checklist
  - Fast troubleshooting

### `CONFIG_EXAMPLES.md` 📝 Configuration Templates
- **What it is:** Ready-to-use configuration examples
- **Best for:** Copy-paste configurations
- **Contains:**
  - 8+ example configurations
  - Conda, venv, system Python examples
  - Path reference guide
  - Verification commands

### `FILE_GUIDE.md` 📁 This File!
- **What it is:** Quick reference for all files
- **Best for:** Understanding the project structure
- **Contains:** What you're reading now!

---

## 🗃️ Legacy/Backup Files

### `screen.bat`
- **What it is:** Your original batch file (backup)
- **Purpose:** Kept as reference or fallback
- **Contains:** Original scrcpy connection command
- **Status:** Not used by the GUI (you can keep or delete)

---

## 📊 File Priority - What to Check First

### For First-Time Setup:
1. ✅ `env_config.json` - Configure your Python environment
2. ✅ `ENVIRONMENT_SETUP.md` - Read setup guide
3. ✅ `launch_gui.bat` - Test with console visible
4. ✅ GUI Settings tab - Configure scrcpy path
5. ✅ `launch_gui.vbs` - Use for normal operation

### When Troubleshooting:
1. ✅ `launch_gui.bat` - Check console for errors
2. ✅ `env_config.json` - Verify environment settings
3. ✅ `README.md` - Check troubleshooting section
4. ✅ `scrcpy_config.json` - Verify scrcpy path

### For Reference:
1. 📘 `README.md` - Complete documentation
2. 🚀 `ENVIRONMENT_SETUP.md` - Quick setup
3. 📝 `CONFIG_EXAMPLES.md` - Configuration examples
4. 📁 `FILE_GUIDE.md` - This guide

---

## 🎯 Quick Decision Tree

**"I want to start the app"**
→ Use `launch_gui.vbs`

**"I'm setting up for the first time"**
→ Edit `env_config.json` → Run `launch_gui.bat` → Check for errors

**"The app won't start"**
→ Run `launch_gui.bat` → Read error messages → Check `env_config.json`

**"I need to change my Python environment"**
→ Edit `env_config.json` → See `CONFIG_EXAMPLES.md` for templates

**"I need to configure scrcpy path"**
→ Launch app → Go to Settings tab → Browse for scrcpy directory

**"I don't know which configuration to use"**
→ Read `ENVIRONMENT_SETUP.md` or `CONFIG_EXAMPLES.md`

**"Something's wrong but I don't know what"**
→ Read `README.md` troubleshooting section

---

## 💡 Pro Tips

1. **Always test with `launch_gui.bat` first** before using silent launchers
2. **Keep `env_config.json` backed up** if you have a complex setup
3. **Use `CONFIG_EXAMPLES.md`** to quickly copy working configurations
4. **Check `scrcpy_config.json`** is created after first GUI launch
5. **Read `ENVIRONMENT_SETUP.md`** for the fastest setup experience

---

## 🔄 Typical Workflow

### Initial Setup:
```
1. Edit env_config.json (use CONFIG_EXAMPLES.md as reference)
2. Run launch_gui.bat (verify no errors)
3. Configure scrcpy path in Settings tab
4. Test device connection
5. Switch to launch_gui.vbs for daily use
```

### Daily Use:
```
1. Double-click launch_gui.vbs
2. Connect to device
3. Mirror your screen!
```

### When Issues Occur:
```
1. Switch to launch_gui.bat to see errors
2. Check env_config.json settings
3. Consult README.md troubleshooting
4. Verify Python environment is activated
```

---

## 📞 Need More Help?

- **Setup Issues:** See `ENVIRONMENT_SETUP.md`
- **Configuration Examples:** See `CONFIG_EXAMPLES.md`  
- **Complete Guide:** See `README.md`
- **Application Errors:** Run `launch_gui.bat` to see detailed messages
- **Environment Problems:** Verify with `conda env list` or `python --version`

---

**Last Updated:** For scrcpy GUI v1.0
**Configuration Version:** env_config.json v1.0
