from expense_forecast import summary


def test_expense_summary(tmp_path):
    test_csv = tmp_path / "transactions.csv"
    test_csv.write_text(
        "date,merchant,amount\n"
        "2026-07-10,STARBUCKS,500\n"
        "2026-07-09,UBER,150\n"
        "2026-08-08,SALARY,5000\n"
        "2026-08-08,SALARY,1500\n"
        "2026-08-08,SWIGGY,100\n"
    )

    summarised = summary(test_csv)
    assert summarised.total_income == 6500
    assert summarised.total_spend == 750
    assert summarised.monthly_spent["2026-07"] == 650
    assert summarised.monthly_spent["2026-08"] == 100
