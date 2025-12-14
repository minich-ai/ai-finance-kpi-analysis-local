import os
import pandas as pd

# Resolve paths relative to the project root (one level above `src/`)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data", "sample")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")

# Ensure an output directory exists at the project root for saving KPI results
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load the cleaned income statement and balance sheet data from the sample data folder
income = pd.read_csv(os.path.join(DATA_DIR, "comcast_income_statement.csv"))
balance = pd.read_csv(os.path.join(DATA_DIR, "comcast_balance_sheet.csv"))

# Normalize balance sheet column names so KPI calculations match
balance.rename(
    columns={
        "TotalCurrentAssets": "CurrentAssets",
        "TotalCurrentLiabilities": "CurrentLiabilities",
    },
    inplace=True,
)

# creating a new dataframe by merging the income and balance sheets on the Year column
df = income.merge(balance, on="Year")

df["OperatingMargin"] = df["OperatingIncome"] / df["Revenue"]
df["NetMargin"] = df["NetIncome"] / df["Revenue"]
df["ROA"] = df["NetIncome"] / df["TotalAssets"]
df["ROE"] = df["NetIncome"] / df["TotalEquity"]

df["CurrentRatio"] = df["CurrentAssets"] / df["CurrentLiabilities"]
df["QuickRatio"] = (df["CurrentAssets"] - df["Inventory"]) / df["CurrentLiabilities"]

df["DebtToEquity"] = df["TotalLiabilities"] / df["TotalEquity"]
df["InterestCoverage"] = df["OperatingIncome"] / df["InterestExpense"]

df["AssetTurnover"] = df["Revenue"] / df["TotalAssets"]
df["ReceivablesTurnover"] = df["Revenue"] / df["AccountsReceivable"]

df.to_csv(os.path.join(OUTPUT_DIR, "kpi_table.csv"), index=False)
# df.to_csv("../output/kpi_table.csv", index=False)

# print the first 5 rows of the dataframe
print(df[["Year", "OperatingMargin", "NetMargin", "ROA", "ROE"]])