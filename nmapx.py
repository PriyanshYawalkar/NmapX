import subprocess
import sys
import re
import os
import json
import threading
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Output directory
OUTPUT_DIR = "reports"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def is_valid_ip_or_domain(target):
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    domain_pattern = re.compile(r'^([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')
    return bool(ip_pattern.match(target) or domain_pattern.match(target))

def print_banner():
    banner = rf"""{Fore.CYAN}{Style.BRIGHT}
 _   _                      __  __  __
| \ | |  __ _  __ _  ___   \ \/ / / _|_ __ ___
|  \| | / _` |/ _` |/ _ \   \  / | |_| '__/ _ \
| |\  || (_| | (_| | (_) |  /  \ |  _| | |  __/
|_| \_| \__,_|\__, |\___/  /_/\_\|_| |_|  \___|
               |___/       by NmapX Scanner CLI
{Style.RESET_ALL}"""
    print(banner)

def show_menu():
    print(f"{Fore.YELLOW}Select scan type(s):")
    print(f"{Fore.GREEN}[1]{Style.RESET_ALL} Quick Scan")
    print(f"{Fore.GREEN}[2]{Style.RESET_ALL} Regular Scan")
    print(f"{Fore.GREEN}[3]{Style.RESET_ALL} Version Detection")
    print(f"{Fore.GREEN}[4]{Style.RESET_ALL} OS Detection")
    print(f"{Fore.GREEN}[5]{Style.RESET_ALL} Aggressive Scan")
    print(f"{Fore.GREEN}[6]{Style.RESET_ALL} Full TCP Port Scan")
    print(f"{Fore.GREEN}[0]{Style.RESET_ALL} All of the above")

def get_scan_commands(target):
    return {
        "Quick Scan": ["nmap", "-T4", "-F", target],
        "Regular Scan": ["nmap", target],
        "Version Detection": ["nmap", "-sV", target],
        "OS Detection": ["nmap", "-O", target],
        "Aggressive Scan": ["nmap", "-A", target],
        "Full TCP Port Scan": ["nmap", "-p-", target]
    }

def save_to_file(target, scan_type, output):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = f"nmapx_{target.replace('.', '_')}_{scan_type.replace(' ', '_')}_{timestamp}"
    txt_path = os.path.join(OUTPUT_DIR, base_name + ".txt")
    json_path = os.path.join(OUTPUT_DIR, base_name + ".json")

    with open(txt_path, "w") as f:
        f.write(output)

    with open(json_path, "w") as f:
        json.dump({
            "target": target,
            "scan_type": scan_type,
            "timestamp": timestamp,
            "output": output
        }, f, indent=2)

    print(f"{Fore.MAGENTA}[✔] Saved output to {txt_path} and {json_path}{Style.RESET_ALL}")
    return txt_path

def run_nmap_scan(target, scan_type, lock):
    command = get_scan_commands(target).get(scan_type)
    if not command:
        print(f"{Fore.RED}[!] Invalid scan type: {scan_type}")
        return

    with lock:
        print(f"\n{Fore.BLUE}[+] Running {scan_type} on {target}...{Style.RESET_ALL}\n")

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        with lock:
            print(Fore.LIGHTWHITE_EX + output + Style.RESET_ALL)
        return (scan_type, output)
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}[!] Error running {scan_type}:\n{e.output}")
        return (scan_type, e.output)

def generate_html_report(target, scan_results):
    html_path = os.path.join(OUTPUT_DIR, f"nmapx_{target.replace('.', '_')}_report.html")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>NmapX Report for {target}</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: #f4f4f4; color: #333; padding: 20px; }}
        h1 {{ color: #0275d8; }}
        pre {{ background: #222; color: #0f0; padding: 10px; overflow-x: auto; }}
    </style>
</head>
<body>
    <h1>NmapX Scan Report</h1>
    <p><strong>Target:</strong> {target}</p>
    <p><strong>Date:</strong> {timestamp}</p>
"""

    for scan_type, output in scan_results:
        html += f"<h2>{scan_type}</h2>\n<pre>{output}</pre>\n"

    html += "</body></html>"

    with open(html_path, "w") as f:
        f.write(html)

    print(f"{Fore.GREEN}[✓] HTML report saved at {html_path}{Style.RESET_ALL}")

def main():
    print_banner()
    target = input(f"{Fore.CYAN}Enter IP address or domain name to scan: {Style.RESET_ALL}").strip()

    if not is_valid_ip_or_domain(target):
        print(f"{Fore.RED}[!] Invalid IP or domain.")
        sys.exit(1)

    show_menu()
    choices = input(f"{Fore.CYAN}Enter your choice(s) (comma-separated): {Style.RESET_ALL}").strip().split(',')

    scan_types = {
        "1": "Quick Scan",
        "2": "Regular Scan",
        "3": "Version Detection",
        "4": "OS Detection",
        "5": "Aggressive Scan",
        "6": "Full TCP Port Scan",
        "0": "All"
    }

    selected_scans = []
    if "0" in choices:
        selected_scans = list(scan_types.values())[0:6]
    else:
        for choice in choices:
            scan_name = scan_types.get(choice.strip())
            if scan_name and scan_name != "All":
                selected_scans.append(scan_name)

    if not selected_scans:
        print(f"{Fore.RED}[!] No valid scan selected.")
        sys.exit(1)

    lock = threading.Lock()
    threads = []
    results = []

    def threaded_scan(scan_type):
        result = run_nmap_scan(target, scan_type, lock)
        if result:
            results.append(result)
            save_to_file(target, result[0], result[1])

    for scan in selected_scans:
        t = threading.Thread(target=threaded_scan, args=(scan,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    generate_html_report(target, results)

    print(f"\n{Fore.CYAN}[✓] All scans and reports completed successfully for {target}.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
