# Risk & Compliance Data Analyzer

This is a simple Python project that analyzes incident and compliance-style data. It loads a CSV file, cleans up messy values, classifies each record into a risk level, saves the processed data to SQLite, creates charts, and exports a final CSV report.

I made it as a student portfolio project, so the code is kept straightforward and easy to follow from the terminal.

## Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- Matplotlib

## What It Does

- Loads incident data from a CSV file
- Creates a sample cybersecurity incident dataset if no dataset exists yet
- Cleans missing values and fixes inconsistent formatting
- Classifies incidents as Low Risk, Medium Risk, High Risk, or Critical Risk
- Counts incidents by risk level, category, department, and month
- Stores the cleaned data in a SQLite database
- Creates charts for the analysis
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

When the project runs, it also creates:

```text
data/sample_incidents.csv
outputs/final_risk_report.csv
outputs/risk_distribution_pie.png
outputs/incident_trend_chart.png
outputs/category_breakdown_chart.png
risk_compliance.db
```

## How To Run It

1. Open the project folder in your terminal.

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the project:

```bash
python main.py
```

The first time you run it, the project creates a sample dataset automatically inside the `data` folder.

## Outputs

The terminal shows a short summary, including the total number of records and the number of incidents in each risk level.

The `outputs` folder contains the final CSV report and three chart images:

- `risk_distribution_pie.png` shows how incidents are split across risk levels
- `incident_trend_chart.png` shows how incidents change month by month
- `category_breakdown_chart.png` shows which incident categories appear the most

The SQLite database file is called `risk_compliance.db`. It stores the cleaned data in a table named `processed_incidents`.

## Notes

This project uses generated sample data, but the same code can be adjusted to work with a real incident or compliance CSV file later.
