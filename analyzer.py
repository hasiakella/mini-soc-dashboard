from collections import Counter

failed_users = []

with open("../logs/auth.log", "r") as file:
    for line in file:
        if "Failed Login" in line:
            user = line.split()[-1]
            failed_users.append(user)

count = Counter(failed_users)

report = "===== MINI SOC THREAT REPORT =====\n\n"

for user, attempts in count.items():

    report += f"User: {user}\n"
    report += f"Failed Attempts: {attempts}\n"

    if attempts >= 3:
        report += "Severity: HIGH\n"
        report += "Alert: Possible Brute Force Attack\n"

    elif attempts == 2:
        report += "Severity: MEDIUM\n"
        report += "Alert: Suspicious Activity\n"

    else:
        report += "Severity: LOW\n"
        report += "Alert: Monitor User\n"

    report += "-" * 30 + "\n"

print(report)

with open("../reports/report.txt", "w") as file:
    file.write(report)

print("Report generated successfully!")