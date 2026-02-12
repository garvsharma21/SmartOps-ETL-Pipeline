import logging
import pandas as pd
from pathlib import Path

logger = logging.getLogger(__name__)

def transform(input_path: str, output_dir: str):

    df = pd.read_csv(input_path)

    required_cols = ["Date", "Customer Name", "Revenue", "Expense"]

    # Validate template
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Convert date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Ensure numeric values
    df["Revenue"] = pd.to_numeric(df["Revenue"], errors="coerce").fillna(0)
    df["Expense"] = pd.to_numeric(df["Expense"], errors="coerce").fillna(0)

    # Create Month column
    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    # ✅ REPORT 1 — Monthly Profit
    monthly = (
        df.groupby("Month")
        .agg(
            Revenue=("Revenue", "sum"),
            Expenses=("Expense", "sum")
        )
        .reset_index()
    )

    monthly["Profit"] = monthly["Revenue"] - monthly["Expenses"]

    # ✅ REPORT 2 — Top Customers
    customers = (
        df.groupby("Customer Name")
        .agg(Total_Revenue=("Revenue", "sum"))
        .sort_values(by="Total_Revenue", ascending=False)
        .reset_index()
    )

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    monthly_path = output_dir / "monthly_profit.csv"
    customer_path = output_dir / "top_customers.csv"

    monthly.to_csv(monthly_path, index=False)
    customers.to_csv(customer_path, index=False)

    logger.info("Reports generated successfully")

    return str(monthly_path), str(customer_path)
