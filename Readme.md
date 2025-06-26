
# NmapX - Nmap Automation CLI Tool

NmapX is a powerful and user-friendly command-line tool built with Python that automates various Nmap scans and generates beautiful, colour-coded reports in .txt, .json, and .html formats.
It's designed for security researchers, penetration testers, sysadmins, and ethical hackers who want fast and organised scan automation.





## Features

- 🎯 Supports IP addresses and domain names
- ✅ Scan Types:
- Quick Scan
- Regular Scan
- Version Detection (-sV)
- OS Detection (-O)
- Aggressive Scan (-A)
- Full TCP Port Scan (-p-)
- 🌈 Colourful, interactive CLI with colorama
- ⚡ Multithreaded scan execution
- 📁 Automatically saves scan results in:
- .txt (raw output)
- .json (structured data)
- .html (nicely formatted)
- 🧠 Intelligent target validation (IP/domain)
- 📂 All reports saved in reports/ folder


## 🛠️ Getting Started

To run this project, follow the steps:

```bash
git clone https://github.com/PriyanshYawalkar/NmapX

cd NmapX

chmod +x nmapx.py

python3 nmapx.py
```




## Optimizations

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

This tool is for educational and authorised security testing only.
Unauthorised scanning is illegal and unethical.
