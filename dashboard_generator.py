services = []
open_ports = 0

with open("../logs/nmap_scan.txt", "r") as file:
    for line in file:

        if "/tcp" in line and "open" in line:
            open_ports += 1

            parts = line.split()

            if len(parts) >= 3:
                services.append(parts[2])

if open_ports == 0:
    risk = "LOW"
    risk_class = "low"

elif open_ports <= 3:
    risk = "MEDIUM"
    risk_class = "medium"

else:
    risk = "HIGH"
    risk_class = "high"

html = f"""
<!DOCTYPE html>
<html>
<head>
<title>Mini SOC Dashboard</title>

<style>

body {{
font-family: Arial;
background:#f4f4f4;
padding:20px;
}}

.card {{
background:white;
padding:20px;
margin:20px;
border-radius:10px;
box-shadow:0px 0px 10px gray;
}}

.high {{
color:red;
font-weight:bold;
}}

.medium {{
color:orange;
font-weight:bold;
}}

.low {{
color:green;
font-weight:bold;
}}

</style>
</head>

<body>

<h1>🛡 MINI SOC DASHBOARD</h1>

<div class="card">
<h2>Network Security Report</h2>

<p>Open Ports : {open_ports}</p>

<p>Services : {", ".join(services)}</p>

<p class="{risk_class}">
Risk Level : {risk}
</p>

</div>

</body>
</html>
"""

with open("../dashboard.html", "w", encoding="utf-8") as file:
    file.write(html)

print("Dynamic Dashboard Generated Successfully!")