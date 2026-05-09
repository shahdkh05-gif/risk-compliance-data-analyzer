# Risk & Compliance Data Analyzer

This is a simple Python project that analyzes incident and compliance data. It cleans the data, groups incidents by risk level, stores the processed records in SQLite, and creates a few charts and reports.

I built this project as part of my portfolio because I am interested in data analysis, data governance, and GRC work.

## Problem Statement

Organizations usually have many incident or compliance records, but the raw data can be messy or hard to understand quickly. This project shows how basic data analysis can help organize those records and highlight which incidents may need more attention.

## Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- Matplotlib

## Features

- Loads incident data from a CSV file
- Creates sample incident data if no CSV file exists
- Cleans missing values and fixes formatting issues
- Classifies incidents into four risk levels:
  - Low Risk
  - Medium Risk
  - High Risk
  - Critical Risk
- Counts incidents by risk level, category, department, and month
- Saves the cleaned data into a SQLite database
- Creates charts for the main analysis
- Exports a final CSV report

## Project Structure

```text
main.py
risk_analysis.py
database.py
visualization.py
requirements.txt
README.md
```

## How To Run The Project

1. Open the project folder in your terminal.

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the project:

```bash
python main.py
```

The project will create a sample dataset automatically the first time it runs.

## Outputs

After running the project, these files are created:

- `data/sample_incidents.csv` - sample incident dataset
- `outputs/final_risk_report.csv` - cleaned data with risk levels added
- `risk_compliance.db` - SQLite database with the processed records
- `outputs/risk_distribution_pie.png` - chart showing risk level distribution
- `outputs/incident_trend_chart.png` - chart showing incidents over time
- `outputs/category_breakdown_chart.png` - chart showing incident categories

The terminal also prints a short summary of the results.

## Notes

This project uses sample data, so it is mainly for practice and portfolio purposes. The same structure can be used with a real incident, compliance, or risk dataset if the CSV columns are adjusted.
