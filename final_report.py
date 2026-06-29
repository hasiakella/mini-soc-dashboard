with open("../reports/report.txt", "r") as threat_file:
    threat_report = threat_file.read()

with open("../logs/nmap_scan.txt", "r") as network_file:
    network_report = network_file.read()

final_report = f"""
==========================
 MINI SOC FINAL REPORT
==========================

THREAT ANALYSIS

{threat_report}

--------------------------

NETWORK ANALYSIS

{network_report}

==========================
END OF REPORT
==========================
"""

with open("../reports/final_soc_report.txt", "w") as file:
    file.write(final_report)

print(final_report)
print("Final SOC Report Generated Successfully!")