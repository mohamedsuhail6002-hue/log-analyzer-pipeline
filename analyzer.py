log_file = "logs.txt"
report_file = "report.txt"

counts = {
    "INFO": 0,
    "ERROR": 0,
    "WARNING": 0
}

with open(log_file, "r") as file:
    for line in file:
        for key in counts:
            if line.startswith(key):
                counts[key] += 1

with open(report_file, "w") as report:
    report.write("Log Summary Report\n")
    report.write("-------------------\n")
    for key, value in counts.items():
        report.write(f"{key}: {value}\n")

print("Report generated successfully!")
