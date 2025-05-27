# Module to generate a detailed report of actions performed.
import pandas as pd

def generate_report(logs, output_file="report.csv"):
    """Generates a CSV report from the logs."""
    try:
        df = pd.DataFrame(logs, columns=["Title", "Status", "Message"])
        df.to_csv(output_file, index=False)
        print(f"Report generated successfully: {output_file}")
    except Exception as e:
        print(f"Error generating report: {e}")