import csv
import random
from datetime import UTC, datetime, timedelta
from pathlib import Path

MERCHANTS = [
    "SALARY",
    "AMAZON",
    "STARBUCKS",
    "UBER",
    "PETROL",
    "SWIGGY",
    "BLINKIT",
    "ZEPTO",
]

Row = tuple[str, str, float]


def generate(n: int, seed: int | None = 3333) -> list[Row]:
    rand = random.Random(seed)
    rows = []
    for _ in range(n):
        random_date = datetime.now(tz=UTC).date() - timedelta(days=rand.randint(0, 365))
        random_date_string = random_date.isoformat()
        random_merchant = rand.choice(MERCHANTS)
        random_amount = rand.randint(10, 10000)
        row = [random_date_string, random_merchant, random_amount]
        rows.append(row)
    return rows


def write(rows: list[Row], path: Path | str) -> None:
    path_local = Path(path)
    with path_local.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "merchant", "amount"])
        writer.writerows(rows)


if __name__ == "__main__":
    n = 300
    rows = generate(n)
    write(rows, "samples/generated/expense_sample.csv")
