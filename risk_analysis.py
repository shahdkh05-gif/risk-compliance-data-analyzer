from pathlib import Path

import numpy as np
import pandas as pd


def generate_sample_dataset(file_path: Path):
    np.random.seed(7)

    departments = ["IT", "Finance", "HR", "Operations", "Security", "Legal"]
    categories = [
        "Phishing",
        "Malware",
        "Policy Violation",
        "Unauthorized Access",
        "System Outage",
        "Data Handling Issue",
    ]
    statuses = ["Open", "Investigating", "Resolved", "Closed"]

    records = []
    start_date = pd.Timestamp("2025-01-01")

    for incident_id in range(1, 121):
        severity = np.random.randint(1, 11)
        days_after_start = np.random.randint(0, 365)

        records.append(
            {
                "incident_id": incident_id,
                "date_reported": start_date + pd.Timedelta(days=int(days_after_start)),
                "department": np.random.choice(departments),
                "category": np.random.choice(categories),
                "severity_score": severity,
                "status": np.random.choice(statuses),
                "estimated_cost": np.random.randint(500, 25000),
            }
        )

    data = pd.DataFrame(records)

    # Add a few messy values so the cleaning step has real work to do.
    data.loc[5, "department"] = np.nan
    data.loc[18, "status"] = np.nan
    data.loc[34, "severity_score"] = np.nan
    data.loc[49, "date_reported"] = "03/15/2025"
    data.loc[72, "category"] = " malware "

    data.to_csv(file_path, index=False)


def classify_risk(severity_score):
    if severity_score <= 3:
        return "Low Risk"
    if severity_score <= 6:
        return "Medium Risk"
    if severity_score <= 8:
        return "High Risk"
    return "Critical Risk"


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    cleaned = data.copy()

    cleaned["date_reported"] = pd.to_datetime(cleaned["date_reported"], errors="coerce")
    cleaned["date_reported"] = cleaned["date_reported"].fillna(cleaned["date_reported"].median())

    cleaned["department"] = cleaned["department"].fillna("Unknown")
    cleaned["category"] = cleaned["category"].fillna("Uncategorized")
    cleaned["status"] = cleaned["status"].fillna("Unknown")

    cleaned["department"] = cleaned["department"].str.strip().str.title()
    cleaned["category"] = cleaned["category"].str.strip().str.title()
    cleaned["status"] = cleaned["status"].str.strip().str.title()

    cleaned["severity_score"] = pd.to_numeric(cleaned["severity_score"], errors="coerce")
    cleaned["severity_score"] = cleaned["severity_score"].fillna(cleaned["severity_score"].median())
    cleaned["severity_score"] = cleaned["severity_score"].clip(1, 10).astype(int)

    cleaned["estimated_cost"] = pd.to_numeric(cleaned["estimated_cost"], errors="coerce")
    cleaned["estimated_cost"] = cleaned["estimated_cost"].fillna(0).round(2)

    cleaned["risk_level"] = cleaned["severity_score"].apply(classify_risk)
    cleaned["month"] = cleaned["date_reported"].dt.to_period("M").astype(str)

    return cleaned


def analyze_data(data: pd.DataFrame) -> dict:
    risk_order = ["Low Risk", "Medium Risk", "High Risk", "Critical Risk"]

    risk_counts = data["risk_level"].value_counts().reindex(risk_order, fill_value=0)
    category_counts = data["category"].value_counts()
    department_counts = data["department"].value_counts()
    monthly_trends = data.groupby("month").size()

    return {
        "risk_counts": risk_counts,
        "category_counts": category_counts,
        "department_counts": department_counts,
        "monthly_trends": monthly_trends,
    }
