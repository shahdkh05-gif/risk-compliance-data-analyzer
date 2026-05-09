from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def create_visualizations(data: pd.DataFrame, output_dir: Path):
    output_dir.mkdir(exist_ok=True)

    create_risk_distribution_chart(data, output_dir)
    create_incident_trend_chart(data, output_dir)
    create_category_breakdown_chart(data, output_dir)


def create_risk_distribution_chart(data: pd.DataFrame, output_dir: Path):
    risk_counts = data["risk_level"].value_counts()

    plt.figure(figsize=(7, 7))
    plt.pie(risk_counts, labels=risk_counts.index, autopct="%1.1f%%", startangle=90)
    plt.title("Risk Distribution")
    plt.tight_layout()
    plt.savefig(output_dir / "risk_distribution_pie.png")
    plt.close()


def create_incident_trend_chart(data: pd.DataFrame, output_dir: Path):
    monthly_trends = data.groupby("month").size()

    plt.figure(figsize=(10, 5))
    monthly_trends.plot(kind="line", marker="o")
    plt.title("Incident Trends Over Time")
    plt.xlabel("Month")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_dir / "incident_trend_chart.png")
    plt.close()


def create_category_breakdown_chart(data: pd.DataFrame, output_dir: Path):
    category_counts = data["category"].value_counts()

    plt.figure(figsize=(10, 5))
    category_counts.plot(kind="bar")
    plt.title("Incident Category Breakdown")
    plt.xlabel("Category")
    plt.ylabel("Number of Incidents")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(output_dir / "category_breakdown_chart.png")
    plt.close()
