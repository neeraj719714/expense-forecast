# Expense Forecast

A personal finance tracker that learns. Import bank transactions, tag and browse them,
see where your money goes, and let the app categorise new transactions, flag unusual
ones, and forecast next month's spend.

## Features (planned)

- Import transactions from CSV exports of multiple banks
- Tag transactions with categories, manually or by rules
- Monthly and per-category spending summaries from the CLI or the API
- Auto-categorisation of new transactions using a model trained on your own tags
- Anomaly detection for unusual transactions
- Next-month spend forecast
- REST API built with FastAPI, ready for a web frontend

## Tech stack

- Python 3.14, managed with [uv](https://docs.astral.sh/uv/)
- SQLite for storage
- FastAPI + pydantic for the API
- pandas, scikit-learn and PyTorch for analysis and models
- pytest and ruff for tests and linting

## Getting started

```bash
brew install uv            # or: curl -LsSf https://astral.sh/uv/install.sh | sh
git clone https://github.com/neeraj719714/expense-forecast.git
cd expense-forecast
uv sync
uv run pytest
```

Real bank exports live in `data/`, which is gitignored. A synthetic dataset can be
generated with `scripts/generate_sample.py` for demos and tests.

## Roadmap

Each phase ships a working increment. A phase is complete when its "Done when" line holds.

### Phase 0 — Project setup

Tooling in place: `uv`, `pytest`, `ruff`, `.gitignore`, repository on GitHub.

**Done when:** `uv run pytest` passes and the repo is on GitHub.

### Phase 1 — CSV summary

`expense-forecast summary transactions.csv` prints total spend, income, and spend per month.
`scripts/generate_sample.py` writes a fake twelve‑month CSV so the repo always has demo data.

**Done when:** the command runs on the sample CSV, with a test for month grouping.

### Phase 2 — Data model and persistence

A `Transaction` type, a `Category` enum, user-assigned categories, and SQLite storage.
Commands: `import`, `list`, `tag <id> <category>`, `summary --by category`.

**Done when:** data survives between runs, tagging works, tests cover import and tag.

### Phase 3 — Multi-bank import and rules

Pluggable importers for several bank CSV formats behind one interface, a config file,
logging, and rule-based auto-tagging (for example "contains STARBUCKS → Coffee").

**Done when:** `expense-forecast import --bank hdfc file.csv` and `--bank chase` both work, rules
auto-tag, and `ruff check` is clean.

### Phase 4 — Web API

FastAPI backend exposing transactions, tags and summaries.

**Done when:** `uv run uvicorn expense_forecast.api:app` serves `/transactions`, `/summary` and
`POST /transactions/{id}/tag`, with API tests.

### Phase 5 — Insights

pandas-powered analysis: monthly trends, category breakdowns, top merchants, rolling
averages. Exploratory work lives in `notebooks/`; results are served from `/insights`.

**Done when:** a notebook tells a clear story about a year of spending and `/insights`
returns the same numbers.

### Phase 6 — Auto-categorisation

A classifier trained on tagged transactions predicts categories for new ones. Served via
`POST /predict` and `expense-forecast import --auto-tag`, with the Phase 3 rule engine as fallback.

**Done when:** the model beats the rule engine on a held-out set and the accuracy figure
is recorded in this README.

### Phase 7 — Forecasting and anomalies

"You'll likely spend ₹X next month" and "this transaction looks unusual", using
regression for the forecast and `IsolationForest` for anomalies, each measured against a
naive baseline.

**Done when:** the forecast beats the "same as last month" baseline and anomaly flags
appear in the API.

### Phase 8 — Neural categoriser

The Phase 6 categoriser reimplemented as a small PyTorch network, then with pretrained
sentence embeddings, compared honestly against the scikit-learn version.

**Done when:** a comparison table (scikit-learn vs NN vs embeddings) is in this README.

### Phase 9 — Deployment

Dockerfile, GitHub Actions running `ruff` and `pytest` on every push, and the API
deployed to a free host.

**Done when:** a green CI badge and a public URL.

## Progress

- [ ] Phase 0 — Project setup
- [ ] Phase 1 — CSV summary
- [ ] Phase 2 — Data model and persistence
- [ ] Phase 3 — Multi-bank import and rules
- [ ] Phase 4 — Web API
- [ ] Phase 5 — Insights
- [ ] Phase 6 — Auto-categorisation
- [ ] Phase 7 — Forecasting and anomalies
- [ ] Phase 8 — Neural categoriser
- [ ] Phase 9 — Deployment
