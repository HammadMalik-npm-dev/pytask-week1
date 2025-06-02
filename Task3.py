import csv
from datetime import datetime

def analyze_csv(input_file, report_file):
    with open(input_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("CSV file is empty")
        return

    # Find rows with missing values
    missing_rows = [i+2 for i, row in enumerate(rows)  # +2 for header + 1-based indexing
                    if any(value == '' or value is None for value in row.values())]

    # Count unique entries per column
    unique_counts = {}
    for column in reader.fieldnames:
        col_values = [row[column] for row in rows if row[column] != '' and row[column] is not None]
        unique_counts[column] = len(set(col_values))

    # Write report
    with open(report_file, 'w', encoding='utf-8') as rep:
        rep.write(f"CSV Analysis Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        rep.write(f"Total rows (excluding header): {len(rows)}\n")
        rep.write(f"Rows with missing values: {len(missing_rows)}\n")
        if missing_rows:
            rep.write(f"Row numbers with missing values: {missing_rows}\n")
        rep.write("\nUnique entries per column:\n")
        for col, count in unique_counts.items():
            rep.write(f"  {col}: {count}\n")

    print(f"Report written to {report_file}")


if __name__ == "__main__":
    analyze_csv('input.csv', 'report.txt')
