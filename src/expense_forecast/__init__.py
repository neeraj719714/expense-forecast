import argparse

from .summary import summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Expense forecast CLI")
    command_parser = parser.add_subparsers(dest="command", required=True)
    summary_parser = command_parser.add_parser(
        "summary", help="Summarise transactions from a CSV"
    )
    summary_parser.add_argument("path", help="Path to the CSV file")
    args = parser.parse_args()

    if args.command == "summary":
        result = summary(args.path)
        print(
            f"Summarised expenses:\nTotal spent: ₹{result.total_spend}\nTotal Income:{result.total_income}"
        )
        for month, amount in sorted(result.monthly_spent.items()):
            print(f"Monthly spent for {month} is {result.monthly_spent[month]}")
