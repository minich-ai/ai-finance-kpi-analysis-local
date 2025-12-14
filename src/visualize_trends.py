"""
Trend visualization script for Comcast financial KPIs.

This script is designed to complement `calculate_kpis.py`:
- It uses the same directory structure and data sources.
- It either reads the pre-computed `kpi_table.csv` from the `output/` folder
  or, if it does not exist, computes the KPIs in the same way as `calculate_kpis.py`.
- It then creates simple trend charts for selected KPIs and saves them to `output/`.

These plots are useful for quickly assessing how profitability, leverage, and
returns have evolved over time.
"""

import os
from typing import List

import pandas as pd
import matplotlib.pyplot as plt


# Base project paths (aligned with `calculate_kpis.py`)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data", "sample")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

# Ensure an output directory exists at the project root for saving results
os.makedirs(OUTPUT_DIR, exist_ok=True)


def build_kpi_table() -> pd.DataFrame:
    """
    Build the KPI table from raw income statement and balance sheet CSV files.

    This mirrors the logic used in `calculate_kpis.py` so that both scripts
    produce a consistent KPI dataset.
    """
    income_path = os.path.join(DATA_DIR, "comcast_income_statement.csv")
    balance_path = os.path.join(DATA_DIR, "comcast_balance_sheet.csv")

    income = pd.read_csv(income_path)
    balance = pd.read_csv(balance_path)

    # Normalize balance sheet column names so KPI calculations match
    balance.rename(
        columns={
            "TotalCurrentAssets": "CurrentAssets",
            "TotalCurrentLiabilities": "CurrentLiabilities",
        },
        inplace=True,
    )

    # Merge the income statement and balance sheet data on Year
    df = income.merge(balance, on="Year")

    # Profitability
    df["OperatingMargin"] = df["OperatingIncome"] / df["Revenue"]
    df["NetMargin"] = df["NetIncome"] / df["Revenue"]
    df["ROA"] = df["NetIncome"] / df["TotalAssets"]
    df["ROE"] = df["NetIncome"] / df["TotalEquity"]

    # Liquidity
    df["CurrentRatio"] = df["CurrentAssets"] / df["CurrentLiabilities"]
    df["QuickRatio"] = (df["CurrentAssets"] - df["Inventory"]) / df["CurrentLiabilities"]

    # Leverage and coverage
    df["DebtToEquity"] = df["TotalLiabilities"] / df["TotalEquity"]
    df["InterestCoverage"] = df["OperatingIncome"] / df["InterestExpense"]

    # Efficiency
    df["AssetTurnover"] = df["Revenue"] / df["TotalAssets"]
    df["ReceivablesTurnover"] = df["Revenue"] / df["AccountsReceivable"]

    kpi_path = os.path.join(OUTPUT_DIR, "kpi_table.csv")
    df.to_csv(kpi_path, index=False)

    return df


def load_or_build_kpi_table() -> pd.DataFrame:
    """
    Load the KPI table from `output/kpi_table.csv` if it exists,
    otherwise compute it from the source CSVs.
    """
    kpi_path = os.path.join(OUTPUT_DIR, "kpi_table.csv")

    if os.path.exists(kpi_path):
        return pd.read_csv(kpi_path)

    return build_kpi_table()


def plot_trend(
    df: pd.DataFrame,
    kpi_column: str,
    ylabel: str,
    output_filename: str,
) -> None:
    """
    Create a simple line chart of a KPI over time and save it as a PNG.
    """
    if "Year" not in df.columns:
        raise ValueError("Expected a 'Year' column in the KPI table.")

    if kpi_column not in df.columns:
        raise ValueError(f"Expected '{kpi_column}' column in the KPI table.")

    plt.figure(figsize=(8, 4))
    plt.plot(df["Year"], df[kpi_column], marker="o")
    plt.title(f"{kpi_column} Trend Over Time")
    plt.xlabel("Year")
    plt.ylabel(ylabel)
    plt.grid(True, linestyle="--", alpha=0.5)

    output_path = os.path.join(OUTPUT_DIR, output_filename)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def generate_trend_charts(df: pd.DataFrame) -> None:
    """
    Generate a small set of core trend visualizations for executive review.
    """
    charts: List[dict] = [
        {
            "column": "OperatingMargin",
            "ylabel": "Operating Margin",
            "filename": "operating_margin_trend.png",
        },
        {
            "column": "NetMargin",
            "ylabel": "Net Margin",
            "filename": "net_margin_trend.png",
        },
        {
            "column": "ROE",
            "ylabel": "Return on Equity",
            "filename": "roe_trend.png",
        },
        {
            "column": "DebtToEquity",
            "ylabel": "Debt-to-Equity",
            "filename": "debt_to_equity_trend.png",
        },
    ]

    for chart in charts:
        plot_trend(
            df=df,
            kpi_column=chart["column"],
            ylabel=chart["ylabel"],
            output_filename=chart["filename"],
        )


if __name__ == "__main__":
    kpi_df = load_or_build_kpi_table()

    # Generate core KPI trend charts for quick profitability and leverage review
    generate_trend_charts(kpi_df)

    # Also print a compact view of key KPIs to the console
    print(
        kpi_df[
            [
                "Year",
                "OperatingMargin",
                "NetMargin",
                "ROA",
                "ROE",
                "DebtToEquity",
            ]
        ]
    )
