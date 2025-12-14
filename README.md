## AI Finance KPI Analysis

**Purpose:**  
Demonstrates a finance-focused KPI analysis workflow suitable for executive decision support, dashboards, and AI-powered analytics.

**Status:**  
Prototype / demonstration (not production-hardened).

**Tools:**  
Python, pandas, matplotlib, LLM-assisted development (Cursor).

**Use cases:**  
- Executive KPI reviews  
- Finance and FP&A scenario analysis  
- AI feature engineering for forecasting and risk models  

This project demonstrates how I approach **data-driven financial analysis for enterprise clients** as an AI business consultant. Using simplified income statement and balance sheet data for Comcast, I calculate a suite of **profitability, liquidity, leverage, and efficiency KPIs** and make the results easily reusable for further analytics, dashboards, or machine learning models.

The repo is intentionally lightweight and self-contained so it can serve as a clear example of my **analytic thinking, data hygiene practices, and business-focused metric design**.

---

## Project Overview

The analysis focuses on turning raw financial statements into **actionable performance metrics** that an executive team or investment stakeholder would care about. From the input CSVs, the pipeline:

- **Ingests** cleaned income statement and balance sheet data from the `data/` folder.
- **Merges** them into a unified dataset keyed on `Year`.
- **Derives KPIs** that quantify:
  - **Profitability** (Operating Margin, Net Margin, ROA, ROE)
  - **Liquidity** (Current Ratio, Quick Ratio)
  - **Leverage & risk** (Debt-to-Equity, Interest Coverage)
  - **Operational efficiency** (Asset Turnover, Receivables Turnover)
- **Exports** a consolidated KPI table to `output/kpi_table.csv` for downstream use (BI tools, Python notebooks, or AI models).

This mirrors how I would structure a **first-phase financial analytics engagement**: start with robust KPIs, then layer on more advanced modeling where appropriate.

---

## Who This Project Is For

- **Business and finance leaders** who want a concrete example of how financial data can be transformed into KPIs that support decision-making.  
- **Analytics and AI consulting clients** who want to see how I structure small, targeted analysis projects.  
- **Learners and collaborators** (including my daughter and future mentees) who want a simple but realistic template for corporate KPI analysis they can extend in their own portfolios.

---

## Data Description & Limitations

- **Source format**: The input CSVs in `data/sample/` are **simplified, cleaned representations** of Comcast’s income statement and balance sheet by year.  
- **Purpose**: They are designed for **educational and portfolio demonstration purposes**, not for official reporting or investment decisions.  
- **Scope**: Only a subset of line items is included—enough to compute the KPIs listed below, but not a full set of financial disclosures.  
- **Assumptions**: Column naming and structure are intentionally stable and simple so the scripts remain easy to read and modify.

When adapting this project for another company, you would typically replace these CSVs with that company’s data in the same general format.

---

## Repository Structure

- `src/`  
  - `calculate_kpis.py` – Core script that loads the financial statement data, harmonizes column names, computes KPIs, and writes the results to `output/kpi_table.csv`.  
  - `visualize_trends.py` – Companion script that builds or loads the KPI table and generates trend charts saved to `output/`.

- `data/`  
  - `sample/`  
    - `comcast_income_statement.csv` – Simplified income statement by year (e.g., Revenue, OperatingIncome, NetIncome, InterestExpense).  
    - `comcast_balance_sheet.csv` – Simplified balance sheet by year (e.g., TotalAssets, TotalLiabilities, TotalEquity, CurrentAssets, CurrentLiabilities, Inventory, AccountsReceivable).

- `output/`  
  - `kpi_table.csv` – Generated KPI table combining both statements and all calculated metrics.

---

## Key Business KPIs Calculated

The pipeline computes the following metrics for each year:

- **Operating Margin** = OperatingIncome / Revenue  
  How efficiently the core operations generate profit from sales.

- **Net Margin** = NetIncome / Revenue  
  Profitability after all expenses, taxes, and interest.

- **Return on Assets (ROA)** = NetIncome / TotalAssets  
  Measures how effectively the company uses its asset base to generate earnings.

- **Return on Equity (ROE)** = NetIncome / TotalEquity  
  Gauges returns delivered to shareholders.

- **Current Ratio** = CurrentAssets / CurrentLiabilities  
  A basic view of short-term liquidity.

- **Quick Ratio** = (CurrentAssets − Inventory) / CurrentLiabilities  
  A more conservative liquidity measure that excludes inventory.

- **Debt-to-Equity** = TotalLiabilities / TotalEquity  
  Indicates leverage and balance-sheet risk.

- **Interest Coverage** = OperatingIncome / InterestExpense  
  Shows how comfortably the company can service its debt.

- **Asset Turnover** = Revenue / TotalAssets  
  Reflects how efficiently assets are used to generate revenue.

- **Receivables Turnover** = Revenue / AccountsReceivable  
  Indicates how quickly the company collects from customers.

These are exactly the types of metrics I use when **connecting quantitative performance to strategic recommendations** for business and finance leaders.

---

## How to Run the Project

### 1. Prerequisites

- **Python**: 3.9+ recommended  
- **Install dependencies** (from the project root):

```bash
pip install -r requirements.txt
```

### 2. Run the KPI Pipeline

From the project root (e.g., `ai-finance-kpi-analysis`), run:

```bash
python src/calculate_kpis.py
```

This will:

- Read the input CSVs from `data/sample/`
- Compute all KPIs described above
- Save the combined result to `output/kpi_table.csv`
- Print a subset of core profitability metrics (`Year`, `OperatingMargin`, `NetMargin`, `ROA`, `ROE`) to the console

If you prefer using `visualize_trends.py` from a notebook or IDE, you can import it or run it directly in a similar way (ensuring your working directory is set appropriately):

```bash
python src/visualize_trends.py
```

---

## Example Use Cases

This project is a minimal but realistic starting point for:

- **Executive KPI dashboards** – Feed `output/kpi_table.csv` into tools like Power BI, Tableau, or Looker to track multi-year performance.
- **Valuation & scenario analysis** – Use ROE, leverage, and margin trends to inform DCF assumptions or capital structure decisions.
- **AI / ML modeling** – Treat KPIs as engineered features for forecasting revenue, default risk, or churn at a portfolio or business-unit level.
- **Benchmarking** – Compare Comcast’s metrics with peer companies to highlight competitive strengths and gaps.

---

## Sample Outputs

After running the scripts, you should see:

- **Tabular output**: `output/kpi_table.csv` containing one row per year with all KPIs (e.g., `Year`, `Revenue`, `OperatingMargin`, `NetMargin`, `ROA`, `ROE`, `DebtToEquity`, etc.).  
- **Trend charts** (from `visualize_trends.py`) saved to `output/`, including:
  - `operating_margin_trend.png`
  - `net_margin_trend.png`
  - `roe_trend.png`
  - `debt_to_equity_trend.png`

These files provide both a **numerical** and **visual** view of performance that can be dropped into presentations, dashboards, or further analysis.

---

## Adapting This Template for Other Companies

To reuse this project for another company or dataset:

- **Prepare new CSVs** that match the general structure of `comcast_income_statement.csv` and `comcast_balance_sheet.csv` (one row per year, similar column names).  
- **Drop them into `data/sample/`**, either overwriting the existing files or adding new ones and updating the script paths if needed.  
- **Update labels and copy** in `README.md` (e.g., company name, context) to reflect the new analysis.  
- **Rerun the scripts**:
  ```bash
  python calculate_kpis.py
  python visualize_trends.py
  ```

This mirrors how I would build a **reusable analysis template** for multiple business units or portfolio companies.

---

## How This Reflects My Consulting Approach

As an **AI business consultant**, I focus on:

- **Translating raw data into business language**: KPIs that a CFO, COO, or CEO can immediately understand and act on.  
- **Building extensible data assets**: The KPI table is structured to plug into more advanced analytics without rework.  
- **Keeping the pipeline simple and maintainable**: Clear, readable Python and CSV-based data make it easy for non-technical stakeholders to follow the logic.

If you’re interested in how this style of analysis could be extended for your organization—e.g., automated forecasting, anomaly detection, or KPI-based alerting—this project is a good representation of my starting point for such engagements.

---

## Authors & Learning Context

This repository is part of a **shared learning and portfolio-building effort** between myself and my daughter, focused on:

- Developing **business analytics and AI consulting skills** through realistic but approachable financial datasets.  
- Practicing **clean, well-documented analysis pipelines** that can be understood by both technical and non-technical stakeholders.  
- Creating a **reusable template** that can seed future projects in our respective portfolios.

The code and documentation are intentionally kept clear and compact so they can be used as a reference or starting point in future client or educational work.

---

## Next Possible Extensions

Some natural follow-ons that I would typically propose in a client context:

- Add **visualizations** of KPI trends (e.g., margin, ROE, leverage) over time.
- Incorporate **peer benchmarks** or industry averages.
- Layer in **forecasting models** (time series or causal models) using these KPIs as key drivers.
- Deploy the metrics and insights into a **lightweight dashboard** or **executive scorecard**.

These are intentionally left as next steps to keep this repository focused, clear, and easy to review in a portfolio setting.


