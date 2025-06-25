# 🔍 NmapX - Nmap Automation CLI Tool

**NmapX** is a powerful and user-friendly command-line tool built with Python that automates various Nmap scans and generates beautiful, color-coded reports in `.txt`, `.json`, and `.html` formats.  
It's designed for security researchers, penetration testers, sysadmins, and ethical hackers who want fast and organized scan automation.

---

## 🚀 Features

- 🎯 Supports IP addresses and domain names
- ✅ Scan Types:
  - Quick Scan
  - Regular Scan
  - Version Detection (`-sV`)
  - OS Detection (`-O`)
  - Aggressive Scan (`-A`)
  - Full TCP Port Scan (`-p-`)
- 🌈 Colorful, interactive CLI with `colorama`
- ⚡ Multithreaded scan execution
- 📁 Automatically saves scan results in:
  - `.txt` (raw output)
  - `.json` (structured data)
  - `.html` (nicely formatted)
- 🧠 Intelligent target validation (IP/domain)
- 📂 All reports saved in `reports/` folder

---

## 📸 Preview

```bash
$ py nmapx.py

 _   _                      __  __  __
| \ | |  __ _  __ _  ___   \ \/ / / _|_ __ ___
|  \| | / _` |/ _` |/ _ \   \  / | |_| '__/ _ \
| |\  || (_| | (_| | (_) |  /  \ |  _| | |  __/
|_| \_| \__,_|\__, |\___/  /_/\_\|_| |_|  \___|
               |___/       by NmapX Scanner CLI

Enter IP address or domain name to scan: scanme.nmap.org
Enter your choice(s) (comma-separated): 1,3,5

[+] Running Quick Scan...
[✔] Saved output to reports/nmapx_scanme_nmap_org_Quick_Scan_20250625.txt
[✓] HTML report saved at reports/nmapx_scanme_nmap_org_report.html

📦 Installation
🔧 Requirements

    Python 3.x

    nmap installed on your system

    colorama Python module

✅ Install Python dependencies:

pip install colorama

    💡 Make sure nmap is installed and accessible from the command line.
    Download: https://nmap.org/download.html

🧪 How to Use

# Run the tool
py nmapx.py

Then follow the interactive prompts:

    Enter a target (e.g. scanme.nmap.org or 192.168.1.1)

    Choose scan types (comma-separated like 1,3,5 or 0 for all)

All reports are saved to the /reports folder.
📝 Output

For each scan, NmapX generates:

    ✅ nmapx_<target>_<scan_type>_<timestamp>.txt

    ✅ nmapx_<target>_<scan_type>_<timestamp>.json

    ✅ One combined nmapx_<target>_report.html

🛠️ Project Structure

nmapx/
├── reports/                 # Generated reports saved here
├── nmapx.py                 # Main script
├── README.md                # You're reading it

💡 Future Features

Output PDF reports

Web dashboard UI (Flask-based)

Subnet scanning and import from .txt or .csv

Email notification of reports

    Plugin support (e.g. NSE scripts, vulnerability scanning)

👨‍💻 Author

NmapX was built with ❤️ using Python and Nmap
Customizable for any Red Team or Blue Team workflow
🛡️ Disclaimer

This tool is for educational and authorized security testing only.
Unauthorized scanning is illegal and unethical.
📜 License

MIT License — free to use, modify, and share.


---

Would you like a logo image or badge icons (like "Made with Python", "MIT License", etc.) included 