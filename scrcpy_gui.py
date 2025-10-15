import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
import subprocess
import threading

class ScrcpyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Scrcpy GUI Wrapper")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        
        # Configuration file path
        self.config_file = "scrcpy_config.json"
        self.config = self.load_config()
        
        # Create main notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_main_tab()
        self.create_settings_tab()
        self.create_pairing_tab()
        self.create_instructions_tab()
        
    def load_config(self):
        """Load configuration from JSON file"""
        default_config = {
            "scrcpy_path": "C:\\Program Files\\scrcpy-win64-v3.3.1",
            "device_ip": "192.168.1.2",
            "device_port": "33963",
            "adb_path": ""
        }
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    loaded_config = json.load(f)
                    default_config.update(loaded_config)
            except:
                pass
        
        return default_config
    
    def save_config(self):
        """Save configuration to JSON file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
            messagebox.showinfo("Success", "Configuration saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save configuration: {str(e)}")
    
    def create_main_tab(self):
        """Create the main connection tab"""
        main_frame = ttk.Frame(self.notebook)
        self.notebook.add(main_frame, text="Connect")
        
        # Title
        title_label = ttk.Label(main_frame, text="Scrcpy Connection Manager", 
                               font=('Arial', 16, 'bold'))
        title_label.pack(pady=20)
        
        # Quick connect frame
        quick_frame = ttk.LabelFrame(main_frame, text="Quick Connect", padding=10)
        quick_frame.pack(fill='x', padx=20, pady=10)
        
        ttk.Label(quick_frame, text="Device IP:").grid(row=0, column=0, sticky='w', pady=5)
        self.ip_entry = ttk.Entry(quick_frame, width=30)
        self.ip_entry.insert(0, self.config.get("device_ip", ""))
        self.ip_entry.grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(quick_frame, text="Port:").grid(row=1, column=0, sticky='w', pady=5)
        self.port_entry = ttk.Entry(quick_frame, width=30)
        self.port_entry.insert(0, self.config.get("device_port", ""))
        self.port_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Connect button
        connect_btn = ttk.Button(quick_frame, text="Connect to Device", 
                                command=self.connect_device, style='Accent.TButton')
        connect_btn.grid(row=2, column=0, columnspan=2, pady=15)
        
        # Paired devices frame
        devices_frame = ttk.LabelFrame(main_frame, text="Paired Devices", padding=10)
        devices_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Listbox for devices
        self.devices_listbox = tk.Listbox(devices_frame, height=8)
        self.devices_listbox.pack(fill='both', expand=True, pady=5)
        
        # Buttons frame
        btn_frame = ttk.Frame(devices_frame)
        btn_frame.pack(fill='x', pady=5)
        
        ttk.Button(btn_frame, text="Refresh Devices", 
                  command=self.refresh_devices).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Connect Selected", 
                  command=self.connect_selected_device).pack(side='left', padx=5)
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="Ready", 
                                     foreground='green', font=('Arial', 10))
        self.status_label.pack(pady=10)
        
    def create_settings_tab(self):
        """Create the settings tab"""
        settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(settings_frame, text="Settings")
        
        # Settings title
        title_label = ttk.Label(settings_frame, text="Configuration Settings", 
                               font=('Arial', 14, 'bold'))
        title_label.pack(pady=20)
        
        # Settings form
        form_frame = ttk.Frame(settings_frame)
        form_frame.pack(fill='x', padx=30, pady=10)
        
        # Scrcpy directory
        ttk.Label(form_frame, text="Scrcpy Directory:", 
                 font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky='w', pady=10)
        
        scrcpy_frame = ttk.Frame(form_frame)
        scrcpy_frame.grid(row=1, column=0, sticky='ew', pady=5)
        
        self.scrcpy_path_entry = ttk.Entry(scrcpy_frame, width=50)
        self.scrcpy_path_entry.insert(0, self.config.get("scrcpy_path", ""))
        self.scrcpy_path_entry.pack(side='left', fill='x', expand=True)
        
        ttk.Button(scrcpy_frame, text="Browse", 
                  command=self.browse_scrcpy).pack(side='left', padx=5)
        
        ttk.Label(form_frame, text="Example: C:\\Program Files\\scrcpy-win64-v3.3.1", 
                 foreground='gray').grid(row=2, column=0, sticky='w', pady=2)
        
        # ADB directory
        ttk.Label(form_frame, text="ADB Directory (optional):", 
                 font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky='w', pady=(20, 10))
        
        adb_frame = ttk.Frame(form_frame)
        adb_frame.grid(row=4, column=0, sticky='ew', pady=5)
        
        self.adb_path_entry = ttk.Entry(adb_frame, width=50)
        self.adb_path_entry.insert(0, self.config.get("adb_path", ""))
        self.adb_path_entry.pack(side='left', fill='x', expand=True)
        
        ttk.Button(adb_frame, text="Browse", 
                  command=self.browse_adb).pack(side='left', padx=5)
        
        ttk.Label(form_frame, text="Leave empty if ADB is in scrcpy directory", 
                 foreground='gray').grid(row=5, column=0, sticky='w', pady=2)
        
        # Default IP and Port
        ttk.Label(form_frame, text="Default Device Settings:", 
                 font=('Arial', 10, 'bold')).grid(row=6, column=0, sticky='w', pady=(20, 10))
        
        ip_port_frame = ttk.Frame(form_frame)
        ip_port_frame.grid(row=7, column=0, sticky='w', pady=5)
        
        ttk.Label(ip_port_frame, text="IP:").pack(side='left')
        self.default_ip_entry = ttk.Entry(ip_port_frame, width=20)
        self.default_ip_entry.insert(0, self.config.get("device_ip", ""))
        self.default_ip_entry.pack(side='left', padx=5)
        
        ttk.Label(ip_port_frame, text="Port:").pack(side='left', padx=(10, 0))
        self.default_port_entry = ttk.Entry(ip_port_frame, width=15)
        self.default_port_entry.insert(0, self.config.get("device_port", ""))
        self.default_port_entry.pack(side='left', padx=5)
        
        # Save button
        ttk.Button(settings_frame, text="Save Configuration", 
                  command=self.save_settings, style='Accent.TButton').pack(pady=30)
        
    def create_pairing_tab(self):
        """Create the ADB pairing tab"""
        pairing_frame = ttk.Frame(self.notebook)
        self.notebook.add(pairing_frame, text="Pair Device")
        
        # Title
        title_label = ttk.Label(pairing_frame, text="Wireless ADB Pairing", 
                               font=('Arial', 14, 'bold'))
        title_label.pack(pady=20)
        
        # Instructions frame
        inst_frame = ttk.LabelFrame(pairing_frame, text="Quick Guide", padding=15)
        inst_frame.pack(fill='x', padx=20, pady=10)
        
        instructions = """1. Enable 'Wireless debugging' on your Android device
2. Go to Settings → Developer Options → Wireless debugging
3. Tap 'Pair device with pairing code'
4. Enter the IP address and pairing code below
5. Click 'Pair Device'"""
        
        ttk.Label(inst_frame, text=instructions, justify='left').pack()
        
        # Pairing form
        pair_form = ttk.LabelFrame(pairing_frame, text="Pairing Details", padding=15)
        pair_form.pack(fill='x', padx=20, pady=10)
        
        ttk.Label(pair_form, text="IP Address:").grid(row=0, column=0, sticky='w', pady=5)
        self.pair_ip_entry = ttk.Entry(pair_form, width=25)
        self.pair_ip_entry.grid(row=0, column=1, padx=10, pady=5, sticky='ew')
        ttk.Label(pair_form, text="(e.g., 192.168.1.2)").grid(row=0, column=2, sticky='w')
        
        ttk.Label(pair_form, text="Pairing Port:").grid(row=1, column=0, sticky='w', pady=5)
        self.pair_port_entry = ttk.Entry(pair_form, width=25)
        self.pair_port_entry.grid(row=1, column=1, padx=10, pady=5, sticky='ew')
        ttk.Label(pair_form, text="(6-digit port number)").grid(row=1, column=2, sticky='w')
        
        ttk.Label(pair_form, text="Pairing Code:").grid(row=2, column=0, sticky='w', pady=5)
        self.pair_code_entry = ttk.Entry(pair_form, width=25)
        self.pair_code_entry.grid(row=2, column=1, padx=10, pady=5, sticky='ew')
        ttk.Label(pair_form, text="(6-digit code)").grid(row=2, column=2, sticky='w')
        
        pair_form.columnconfigure(1, weight=1)
        
        # Pair button
        ttk.Button(pairing_frame, text="Pair Device", 
                  command=self.pair_device, style='Accent.TButton').pack(pady=15)
        
        # Output frame
        output_frame = ttk.LabelFrame(pairing_frame, text="Output", padding=10)
        output_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.pair_output = tk.Text(output_frame, height=6, wrap='word')
        self.pair_output.pack(fill='both', expand=True)
        
    def create_instructions_tab(self):
        """Create detailed instructions tab"""
        inst_frame = ttk.Frame(self.notebook)
        self.notebook.add(inst_frame, text="Help")
        
        # Create scrollable text
        text_frame = ttk.Frame(inst_frame)
        text_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side='right', fill='y')
        
        help_text = tk.Text(text_frame, wrap='word', yscrollcommand=scrollbar.set, 
                           font=('Arial', 10))
        help_text.pack(fill='both', expand=True)
        scrollbar.config(command=help_text.yview)
        
        instructions = """
SCRCPY GUI WRAPPER - COMPLETE GUIDE

═══════════════════════════════════════════════════════════════════

📋 SETUP INSTRUCTIONS

1. INSTALL SCRCPY
   • Download scrcpy from: https://github.com/Genymobile/scrcpy
   • Extract to a directory (e.g., C:\\Program Files\\scrcpy-win64-v3.3.1)
   • Note: ADB is included in scrcpy, no separate installation needed

2. CONFIGURE THIS APPLICATION
   • Go to the 'Settings' tab
   • Set the Scrcpy Directory path
   • Set your default device IP and port
   • Click 'Save Configuration'

═══════════════════════════════════════════════════════════════════

📱 WIRELESS CONNECTION SETUP

METHOD 1: USB THEN WIRELESS (EASIEST)

1. Connect your Android device via USB cable
2. Enable USB debugging on your device:
   Settings → About Phone → Tap 'Build Number' 7 times
   Settings → Developer Options → Enable 'USB Debugging'
3. Run this command in terminal:
   adb tcpip 5555
4. Disconnect USB cable
5. Get your device's IP address:
   Settings → About Phone → Status → IP Address
   OR: Settings → Wi-Fi → Current Network → IP Address
6. In the 'Connect' tab, enter IP and port 5555, then click Connect

METHOD 2: WIRELESS PAIRING (ANDROID 11+)

1. Enable Wireless Debugging on your device:
   Settings → Developer Options → Wireless Debugging (turn ON)
2. Tap 'Pair device with pairing code'
3. Note the IP address, port, and 6-digit code
4. Go to 'Pair Device' tab in this application
5. Enter the IP, pairing port, and code
6. Click 'Pair Device'
7. After successful pairing, go back to Wireless Debugging screen
8. Note the IP and port shown at the top (e.g., 192.168.1.2:33963)
9. Use this IP and port in the 'Connect' tab

═══════════════════════════════════════════════════════════════════

🔌 USING THE APPLICATION

CONNECT TAB:
• Quick Connect: Enter IP and port manually, then click 'Connect to Device'
• Paired Devices: Shows all connected ADB devices
  - Click 'Refresh Devices' to scan for devices
  - Select a device and click 'Connect Selected' to mirror

SETTINGS TAB:
• Configure scrcpy installation directory
• Set default IP and port for quick access
• All settings are saved automatically

PAIR DEVICE TAB:
• Use for wireless pairing on Android 11+
• Follow the on-screen instructions
• Check output window for pairing status

═══════════════════════════════════════════════════════════════════

❓ TROUBLESHOOTING

Problem: "scrcpy not found"
Solution: Check Settings tab and verify scrcpy directory path

Problem: "Cannot connect to device"
Solution: 
• Ensure device and computer are on the same Wi-Fi network
• Check if wireless debugging is enabled
• Verify IP address is correct
• Try restarting wireless debugging on device

Problem: "Device unauthorized"
Solution: Check your device screen for authorization popup

Problem: ADB commands not working
Solution: Make sure ADB path is correct in Settings, or leave empty
         if using ADB from scrcpy directory

═══════════════════════════════════════════════════════════════════

💡 TIPS

• Keep your device and computer on the same Wi-Fi network
• Use a 5GHz Wi-Fi connection for better performance
• The wireless connection persists until device reboot
• You can save multiple device IPs by using the Paired Devices list
• For best quality, ensure strong Wi-Fi signal strength

═══════════════════════════════════════════════════════════════════
"""
        
        help_text.insert('1.0', instructions)
        help_text.config(state='disabled')
        
    def browse_scrcpy(self):
        """Browse for scrcpy directory"""
        directory = filedialog.askdirectory(title="Select Scrcpy Directory")
        if directory:
            self.scrcpy_path_entry.delete(0, tk.END)
            self.scrcpy_path_entry.insert(0, directory)
            
    def browse_adb(self):
        """Browse for ADB directory"""
        directory = filedialog.askdirectory(title="Select ADB Directory")
        if directory:
            self.adb_path_entry.delete(0, tk.END)
            self.adb_path_entry.insert(0, directory)
            
    def save_settings(self):
        """Save settings from the settings tab"""
        self.config["scrcpy_path"] = self.scrcpy_path_entry.get()
        self.config["adb_path"] = self.adb_path_entry.get()
        self.config["device_ip"] = self.default_ip_entry.get()
        self.config["device_port"] = self.default_port_entry.get()
        
        # Update main tab entries
        self.ip_entry.delete(0, tk.END)
        self.ip_entry.insert(0, self.config["device_ip"])
        self.port_entry.delete(0, tk.END)
        self.port_entry.insert(0, self.config["device_port"])
        
        self.save_config()
        
    def get_adb_path(self):
        """Get the full path to ADB executable"""
        adb_path = self.config.get("adb_path", "")
        if adb_path and os.path.exists(adb_path):
            return os.path.join(adb_path, "adb.exe")
        else:
            # Use ADB from scrcpy directory
            scrcpy_path = self.config.get("scrcpy_path", "")
            return os.path.join(scrcpy_path, "adb.exe")
            
    def get_scrcpy_path(self):
        """Get the full path to scrcpy executable"""
        scrcpy_path = self.config.get("scrcpy_path", "")
        return os.path.join(scrcpy_path, "scrcpy.exe")
        
    def run_command(self, command, show_output=True):
        """Run a command and return output"""
        try:
            # Hide console window for subprocess
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
            
            result = subprocess.run(command, capture_output=True, text=True, 
                                   shell=True, timeout=10, startupinfo=startupinfo)
            output = result.stdout + result.stderr
            if show_output:
                return output, result.returncode == 0
            return "", result.returncode == 0
        except subprocess.TimeoutExpired:
            return "Command timeout", False
        except Exception as e:
            return f"Error: {str(e)}", False
            
    def refresh_devices(self):
        """Refresh the list of connected devices"""
        self.status_label.config(text="Scanning for devices...", foreground='orange')
        self.devices_listbox.delete(0, tk.END)
        
        def scan():
            adb_path = self.get_adb_path()
            output, success = self.run_command(f'"{adb_path}" devices')
            
            devices = []
            for line in output.split('\n'):
                if '\tdevice' in line:
                    device_id = line.split('\t')[0].strip()
                    devices.append(device_id)
            
            self.root.after(0, lambda: self.update_devices_list(devices))
            
        threading.Thread(target=scan, daemon=True).start()
        
    def update_devices_list(self, devices):
        """Update the devices listbox"""
        self.devices_listbox.delete(0, tk.END)
        if devices:
            for device in devices:
                self.devices_listbox.insert(tk.END, device)
            self.status_label.config(text=f"Found {len(devices)} device(s)", 
                                    foreground='green')
        else:
            self.status_label.config(text="No devices found", foreground='red')
            
    def connect_device(self):
        """Connect to device using IP and port from entries"""
        ip = self.ip_entry.get().strip()
        port = self.port_entry.get().strip()
        
        if not ip or not port:
            messagebox.showerror("Error", "Please enter both IP address and port")
            return
            
        self.status_label.config(text="Connecting...", foreground='orange')
        
        def connect():
            adb_path = self.get_adb_path()
            
            # First, connect via ADB
            output, success = self.run_command(f'"{adb_path}" connect {ip}:{port}')
            
            if success or 'connected' in output.lower():
                # Launch scrcpy without console window
                scrcpy_path = self.get_scrcpy_path()
                
                # Use CREATE_NO_WINDOW flag to hide console
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE
                
                subprocess.Popen(f'"{scrcpy_path}" --tcpip={ip}:{port}', 
                               shell=True, startupinfo=startupinfo)
                
                self.root.after(0, lambda: self.status_label.config(
                    text="Connected! Scrcpy launched", foreground='green'))
            else:
                self.root.after(0, lambda: messagebox.showerror(
                    "Connection Failed", f"Could not connect to device:\n{output}"))
                self.root.after(0, lambda: self.status_label.config(
                    text="Connection failed", foreground='red'))
                    
        threading.Thread(target=connect, daemon=True).start()
        
    def connect_selected_device(self):
        """Connect to selected device from list"""
        selection = self.devices_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a device from the list")
            return
            
        device = self.devices_listbox.get(selection[0])
        
        self.status_label.config(text="Launching scrcpy...", foreground='orange')
        
        def launch():
            scrcpy_path = self.get_scrcpy_path()
            
            # Use CREATE_NO_WINDOW flag to hide console
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE
            
            # If device is IP:PORT format, use --tcpip, otherwise use -s
            if ':' in device:
                subprocess.Popen(f'"{scrcpy_path}" --tcpip={device}', 
                               shell=True, startupinfo=startupinfo)
            else:
                subprocess.Popen(f'"{scrcpy_path}" -s {device}', 
                               shell=True, startupinfo=startupinfo)
            
            self.root.after(0, lambda: self.status_label.config(
                text="Scrcpy launched", foreground='green'))
                
        threading.Thread(target=launch, daemon=True).start()
        
    def pair_device(self):
        """Pair device using wireless debugging"""
        ip = self.pair_ip_entry.get().strip()
        port = self.pair_port_entry.get().strip()
        code = self.pair_code_entry.get().strip()
        
        if not ip or not port or not code:
            messagebox.showerror("Error", "Please fill in all pairing fields")
            return
            
        self.pair_output.delete('1.0', tk.END)
        self.pair_output.insert('1.0', "Pairing...\n")
        
        def pair():
            adb_path = self.get_adb_path()
            output, success = self.run_command(f'"{adb_path}" pair {ip}:{port} {code}')
            
            self.root.after(0, lambda: self.pair_output.insert(tk.END, output))
            
            if success or 'successfully paired' in output.lower():
                self.root.after(0, lambda: messagebox.showinfo(
                    "Success", "Device paired successfully!\n\n"
                    "Now go back to Wireless Debugging screen on your device,\n"
                    "note the IP and port, and use them in the Connect tab."))
            else:
                self.root.after(0, lambda: messagebox.showerror(
                    "Pairing Failed", "Could not pair with device. Check the details."))
                    
        threading.Thread(target=pair, daemon=True).start()

def main():
    root = tk.Tk()
    app = ScrcpyGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
