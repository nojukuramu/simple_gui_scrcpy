# Environment Configuration Examples

This file contains ready-to-use configuration examples for different Python setups.

## How to Use

1. Copy the configuration that matches your setup
2. Paste it into `env_config.json`
3. Modify the values to match your specific environment
4. Save the file

---

## Example 1: Conda Environment (Most Common)

**Use this if:** You have Anaconda or Miniconda installed

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

**To customize:**
- Replace `"aisa_env"` with your conda environment name (appears twice)
- Keep everything else the same

---

## Example 2: Conda Base Environment

**Use this if:** You want to use conda's base environment

```json
{
    "environment": {
        "type": "conda",
        "name": "base",
        "activate_command": "conda activate base"
    },
    "python": {
        "executable": "python",
        "use_pythonw": true
    }
}
```

---

## Example 3: Python Virtual Environment (venv)

**Use this if:** You created a virtual environment with `python -m venv`

```json
{
    "environment": {
        "type": "venv",
        "name": "scrcpy_venv",
        "activate_command": "C:\\Users\\YourName\\Desktop\\SCREEN\\scrcpy_venv\\Scripts\\activate"
    },
    "python": {
        "executable": "python",
        "use_pythonw": true
    }
}
```

**To customize:**
- Replace `"scrcpy_venv"` with your venv folder name
- Replace the path with your actual venv location
- Use double backslashes `\\` in Windows paths

---

## Example 4: System Python (No Virtual Environment)

**Use this if:** You have Python installed system-wide and don't use virtual environments

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

**Note:** No customization needed, use as-is

---

## Example 5: Multiple Python Installations

**Use this if:** You have multiple Python versions and want to specify which one

```json
{
    "environment": {
        "type": "system",
        "name": "python39",
        "activate_command": ""
    },
    "python": {
        "executable": "C:\\Python39\\python.exe",
        "use_pythonw": true
    }
}
```

**To customize:**
- Replace `"C:\\Python39\\python.exe"` with your Python executable path
- Use double backslashes `\\` in paths

---

## Example 6: PyEnv or Custom Environment Manager

**Use this if:** You use pyenv, poetry, or another environment manager

```json
{
    "environment": {
        "type": "custom",
        "name": "my_custom_env",
        "activate_command": "pyenv activate my_custom_env"
    },
    "python": {
        "executable": "python",
        "use_pythonw": true
    }
}
```

**To customize:**
- Replace the `activate_command` with your specific activation command
- Examples:
  - PyEnv: `"pyenv activate env_name"`
  - Poetry: `"poetry shell"`
  - Pipenv: `"pipenv shell"`

---

## Example 7: With Console Window (For Debugging)

**Use this if:** You want to see console output for troubleshooting

```json
{
    "environment": {
        "type": "conda",
        "name": "aisa_env",
        "activate_command": "conda activate aisa_env"
    },
    "python": {
        "executable": "python",
        "use_pythonw": false
    }
}
```

**Key change:** `"use_pythonw": false` - This shows the console window

---

## Example 8: Specific Python Version with Conda

**Use this if:** You have multiple conda environments with different Python versions

```json
{
    "environment": {
        "type": "conda",
        "name": "py310_env",
        "activate_command": "conda activate py310_env"
    },
    "python": {
        "executable": "python",
        "use_pythonw": true
    },
    "notes": {
        "python_version": "3.10",
        "created_for": "scrcpy GUI with Python 3.10"
    }
}
```

---

## Common Paths Reference

### Typical Conda Environment Locations:

**Windows:**
- User environments: `C:\Users\YourName\.conda\envs\env_name`
- Miniconda: `C:\ProgramData\Miniconda3\envs\env_name`
- Anaconda: `C:\ProgramData\Anaconda3\envs\env_name`

### Typical venv Locations:

**Project-based:**
- `C:\Projects\MyProject\venv`
- `C:\Users\YourName\Desktop\SCREEN\venv`

**Centralized:**
- `C:\Python\Virtualenvs\env_name`

---

## Verification Commands

Before configuring, verify your setup:

### Find Conda Environments:
```bash
conda env list
conda info --envs
```

### Find Python Executable:
```bash
where python        # Windows CMD
Get-Command python  # PowerShell
```

### Check Python in Current Environment:
```bash
python --version
python -c "import sys; print(sys.executable)"
```

### Check if tkinter is Available:
```bash
python -c "import tkinter; print('tkinter OK')"
```

---

## Troubleshooting Tips

1. **Path Errors:**
   - Always use double backslashes: `C:\\path\\to\\folder`
   - Or use forward slashes: `C:/path/to/folder`

2. **Environment Not Found:**
   - Run `conda env list` to verify environment name
   - Environment names are case-sensitive

3. **Activation Fails:**
   - Test activation manually in CMD/PowerShell first
   - Make sure conda is initialized in your shell

4. **GUI Doesn't Start:**
   - Set `"use_pythonw": false` to see error messages
   - Check if tkinter is installed: `conda install tk` or `pip install tk`

---

## Need More Help?

- See **ENVIRONMENT_SETUP.md** for step-by-step guide
- See **README.md** for complete documentation
- Run `launch_gui.bat` (not .vbs) to see detailed error messages
