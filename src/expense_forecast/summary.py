import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Summary:
    total_spend: float
    total_income: float
    monthly_spent: dict[str, float]


SALARY_KEY = "SALARY"


def summary(path: Path | str) -> Summary:
    income = 0
    total_spend = 0
    per_month_spends = {}
    csv_path = Path(path)
    with csv_path.open(mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            date_str = row["date"]
            merchant = row["merchant"]
            amount = float(row["amount"])
            if merchant == SALARY_KEY:
                income += amount
            else:
                total_spend += amount
                year_month = "-".join(date_str.split("-")[:2])
                per_month_spends[year_month] = (
                    per_month_spends.get(year_month, 0.0) + amount
                )
    return Summary(
        total_income=income,
        total_spend=total_spend,
        monthly_spent=dict(per_month_spends),
    )
