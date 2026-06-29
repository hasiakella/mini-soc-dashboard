services = []
open_ports = 0

with open("../logs/nmap_scan.txt", "r") as file:
    for line in file:

        if "/tcp" in line and "open" in line:

            open_ports += 1

            parts = line.split()

            if len(parts) >= 3:
                services.append(parts[2])

print("\n===== NETWORK SECURITY REPORT =====\n")

print("Open Ports:", open_ports)
print("Services:", ", ".join(services))

risk = "LOW"

if "ftp" in services or "telnet" in services:
    risk = "HIGH"

elif open_ports >= 4:
    risk = "HIGH"

elif open_ports >= 1:
    risk = "MEDIUM"

print("Risk Level:", risk)