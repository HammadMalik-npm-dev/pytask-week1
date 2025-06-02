import os
from datetime import datetime

def find_log_files(directory):
    return [file for file in os.listdir(directory) if file.endswith('.log') or file.endswith('.txt')]

def summarize_errors(file_path):
    errors = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if any(keyword in line.upper() for keyword in ['ERROR', 'FAIL', 'EXCEPTION', 'CRITICAL']):
                errors.append(line.strip())
    return errors

def write_report(report_path, summary):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(report_path, 'w', encoding='utf-8') as report:
        report.write(f"Error Summary Report - {timestamp}\n\n")
        for filename, errors in summary.items():
            report.write(f"File: {filename}\n")
            if errors:
                for error in errors:
                    report.write(f"  - {error}\n")
            else:
                report.write("  No errors found.\n")
            report.write("\n")

def main():
    directory = 'logs' 
    report_path = 'weekly_log_report.txt'

    log_files = find_log_files(directory)
    summary = {}

    for file in log_files:
        path = os.path.join(directory, file)
        summary[file] = summarize_errors(path)

    write_report(report_path, summary)
    print(f"Report written to: {report_path}")

