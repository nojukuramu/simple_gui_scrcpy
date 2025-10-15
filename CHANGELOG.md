# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-10-15

### Added
- Professional project structure with organized folders
- Comprehensive documentation suite in `docs/` folder
- Multiple launcher options (debug, silent, standard)
- Environment configuration system (`config/env_config.json`)
- Support for conda, venv, system, and custom Python environments
- Diagnostic tool (`tools/test_setup.bat`)
- Wireless ADB pairing interface in GUI
- Paired devices list and management
- Configuration persistence for scrcpy paths and device settings
- In-app help and troubleshooting guides
- MIT License
- Contributing guidelines
- This changelog

### Changed
- Reorganized file structure for better maintainability
- Moved source code to `src/` directory
- Moved launchers to `launchers/` directory
- Moved documentation to `docs/` directory
- Moved configuration to `config/` directory
- Improved error handling and user feedback
- Enhanced launcher scripts with better path handling
- Updated all documentation for new structure

### Fixed
- subprocess.STARTUPINFO compatibility issues across Python versions
- Silent failures when GUI doesn't launch
- VBS launcher path resolution
- Console window hiding on Windows
- Environment activation in batch scripts
- Path handling for relocated files

## [1.0.0] - 2025-10-12

### Added
- Initial release
- Basic GUI with tkinter
- Quick connect functionality
- Settings tab for configuration
- Device pairing support
- Connection status indicators
- README documentation
- Basic batch launcher

---

## Version History

- **v1.1.0** - Professional reorganization and enhanced features
- **v1.0.0** - Initial working release

---

For more details on each version, see the [Releases](https://github.com/nojukuramu/simple_gui_scrcpy/releases) page.
