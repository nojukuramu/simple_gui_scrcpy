# Contributing to Scrcpy GUI Wrapper

First off, thank you for considering contributing to Scrcpy GUI Wrapper! It's people like you that make this tool better for everyone.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)

## 🤝 Code of Conduct

This project and everyone participating in it is governed by respect and professionalism. Please be kind and courteous to others.

## 🎯 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Description:** Clear and concise description of the bug
- **Steps to Reproduce:** Detailed steps to reproduce the behavior
- **Expected Behavior:** What you expected to happen
- **Actual Behavior:** What actually happened
- **Environment:**
  - OS version (Windows 10/11)
  - Python version
  - Environment type (conda/venv/system)
  - Scrcpy version
- **Logs:** Output from `launchers/launch_gui_debug.bat`

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use Case:** Clear description of the problem you're trying to solve
- **Proposed Solution:** Your idea for how to address it
- **Alternatives:** Other solutions you've considered
- **Additional Context:** Screenshots, mockups, or examples

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Make your changes**
4. **Test thoroughly**
5. **Commit with clear messages**
6. **Push to your fork**
7. **Open a Pull Request**

## 🛠️ Development Setup

### Prerequisites

- Python 3.7+
- Conda or venv
- Git
- scrcpy installed

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/simple_gui_scrcpy.git
cd simple_gui_scrcpy

# Configure environment
# Edit config/env_config.json with your settings

# Test the application
launchers\launch_gui_debug.bat
```

### Running Tests

```bash
# Run diagnostic tests
tools\test_setup.bat

# Test GUI manually
python src\scrcpy_gui.py
```

## 🔄 Pull Request Process

1. **Update Documentation:** Ensure docs are updated for any changes
2. **Test Thoroughly:** Test on a clean environment
3. **Follow Style Guide:** Maintain consistent code style
4. **Update CHANGELOG:** Add notes about your changes
5. **Request Review:** Wait for maintainer review

### Pull Request Checklist

- [ ] Code follows the project's style guidelines
- [ ] Self-reviewed the code
- [ ] Commented code, particularly complex areas
- [ ] Updated documentation as needed
- [ ] No new warnings generated
- [ ] Tested on Windows 10/11
- [ ] Works with conda, venv, and system Python

## 📝 Style Guidelines

### Python Code

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small
- Comment complex logic

### Batch Scripts

- Use clear variable names
- Add comments for complex sections
- Include error handling
- Provide user feedback

### Documentation

- Use clear, concise language
- Include code examples where helpful
- Keep formatting consistent
- Update relevant files in `docs/`

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests

Example:
```
Add device refresh button to main tab

- Adds auto-refresh every 30 seconds
- Includes manual refresh button
- Updates device list in real-time

Fixes #123
```

## 🏗️ Project Structure

Familiarize yourself with the structure:

```
src/           - Python source code
launchers/     - Batch and VBS launch scripts
config/        - Configuration templates
docs/          - Documentation files
tools/         - Utility scripts
```

## 🧪 Testing

Before submitting a PR:

1. Test with multiple Python environments (conda, venv, system)
2. Verify all launchers work correctly
3. Check documentation accuracy
4. Run `tools\test_setup.bat` successfully
5. Test GUI functionality end-to-end

## 📞 Questions?

Feel free to:
- Open an issue for discussion
- Reach out to maintainers
- Check existing documentation in `docs/`

## 🎉 Recognition

Contributors will be recognized in:
- Repository contributors page
- Release notes (for significant contributions)
- Special thanks section

---

Thank you for contributing! 🙏
