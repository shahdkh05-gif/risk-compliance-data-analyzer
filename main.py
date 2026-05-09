from pathlib import Path

import pandas as pd

from database import save_to_database
from risk_analysis import analyze_data, clean_data, generate_sample_dataset
from visualization import create_visualizations


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
DB_PATH = BASE_DIR / "risk_compliance.db"


def main():
    DATA_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)

    input_file = DATA_DIR / "sample_incidents.csv"
    report_file = OUTPUT_DIR / "final_risk_report.csv"

    if not input_file.exists():
        generate_sample_dataset(input_file)
        print(f"Sample dataset created: {input_file}")

    print("Loading dataset...")
    raw_data = pd.read_csv(input_file)

    print("Cleaning data and classifying risk...")
    cleaned_data = clean_data(raw_data)

    print("Running analysis...")
    summary = analyze_data(cleaned_data)

    print("Saving processed data to SQLite...")
    save_to_database(cleaned_data, DB_PATH)

    print("Creating charts...")
    create_visualizations(cleaned_data, OUTPUT_DIR)

    cleaned_data.to_csv(report_file, index=False)

    print("\nRisk & Compliance Data Analyzer")
    print("--------------------------------")
    print(f"Total records analyzed: {len(cleaned_data)}")
    print("\nIncidents by risk level:")
    print(summary["risk_counts"].to_string())
    print("\nIncidents by category:")
    print(summary["category_counts"].to_string())
    print("\nOutput files created in the outputs folder.")
    print(f"Final CSV report: {report_file}")
    print(f"SQLite database: {DB_PATH}")


if __name__ == "__main__":
    main()
