# learn-python → machine learning, by building one real app

A learning roadmap. Every phase adds real features to one app and teaches the Python
you need for that feature. The ML phases at the end use the data the app has been
collecting all along, so the ML is never abstract.

**Starting point:** experienced frontend developer, new to Python. We skip "what is a
variable" and go straight to Python's own idioms, tooling and standard library.

## The app: **Ledger** — a personal finance tracker that learns

You import bank transactions, browse and tag them, see where money goes, and
eventually the app categorises transactions for you, flags unusual ones, and forecasts
next month's spend.

Why this app:
- Starts as a 50-line script, grows into a package, an API, then a data + ML project.
- Its data (dated, labelled text with amounts) is the perfect first ML dataset:
  text classification, regression, time series, anomaly detection all fit naturally.
- You can use your own bank exports (kept out of git) or a synthetic dataset.

## How we work

1. Each phase has **Build**, **Python you learn**, and **Done when**.
2. You write the code. Ask Claude to explain a concept, review a commit, or hand you a
   small exercise before a feature. Don't ask it to write the feature for you.
3. Commit at the end of every "Done when" line. Small, frequent commits.
4. Real bank data never goes into git. `data/` is gitignored from day one.

---

## Phase 0 — Setup (1 evening)

**Build:** empty project that runs, tests, lints and is on GitHub.

- Install `uv` (`curl -LsSf https://astral.sh/uv.sh | sh`) — package + venv manager.
- `uv init`, `uv add --dev pytest ruff`, `pyproject.toml` committed.
- `.gitignore` (Python template + `data/`), `git init`, push to GitHub.
- VS Code: Python + Ruff extensions, select the `.venv` interpreter.

**Python you learn:** virtual envs, `pyproject.toml`, running scripts with `uv run`,
the REPL (`python -i`), `ruff` as formatter + linter.

**Done when:** `uv run pytest` passes a trivial test and the repo is on GitHub.

## Phase 1 — Transactions from a CSV (week 1)

**Build:** `ledger summary transactions.csv` prints total spend, income, and spend
per month. Include a `scripts/generate_sample.py` that writes a fake 12‑month CSV so the
repo has demo data.

**Python you learn:** syntax, `str`/`int`/`float`/`Decimal`, `list`/`dict`/`tuple`/`set`,
functions and keyword args, f-strings, `for`/`while`, truthiness, `open()` and the `csv`
module, `datetime`, `argparse`, `if __name__ == "__main__"`, `random` for the generator.

**Done when:** command runs on the sample CSV, and there's a test for the month
grouping logic.

## Phase 2 — Model the data properly (week 2)

**Build:** a `Transaction` type, a `Category` enum, user-assigned categories, and
persistence in SQLite. Commands: `import`, `list`, `tag <id> <category>`, `summary
--by category`.

**Python you learn:** `@dataclass`, `Enum`, type hints (`list[Transaction]`, `| None`),
`Optional`, exceptions and custom errors, `sqlite3`, `pathlib`, sorting with `key=`,
`pytest` fixtures and `tmp_path`.

**Done when:** data survives between runs, tagging works, tests cover import + tag.

## Phase 3 — Make it a real package (week 3)

**Build:** support two or three bank CSV formats via pluggable importers, a config
file, logging, and rule-based auto-tagging ("contains STARBUCKS → Coffee").

**Python you learn:** packages and `__init__.py`, absolute vs relative imports,
comprehensions, generators and `yield`, `*args/**kwargs`, decorators, context managers
(`with`, `contextlib`), `Protocol`/ABCs for the importer interface, `logging`, `re`,
`functools`, `itertools`, `collections.Counter/defaultdict`, `typer` or `click` for a
nicer CLI.

**Done when:** `ledger import --bank hdfc file.csv` and `--bank chase` both work through
the same interface, rules auto-tag, and `ruff check` is clean.

## Phase 4 — Web API (week 4)

**Build:** FastAPI backend exposing transactions, tags and summaries. Optional: a tiny
frontend (you're a frontend dev; a small React or plain HTML page against the API is a
good weekend job, but it isn't the point).

**Python you learn:** FastAPI, `pydantic` models and validation, `async/await` basics,
dependency injection, `httpx` for testing the API, environment variables, project layout
for an app vs a library.

**Done when:** `uv run uvicorn ledger.api:app` serves `/transactions`, `/summary`, and
`POST /transactions/{id}/tag`, with API tests.

## Phase 5 — Data analysis: the bridge to ML (weeks 5–6)

**Build:** a `notebooks/` folder. Load transactions into pandas, produce monthly trend
charts, category breakdowns, top merchants, rolling averages. Add an `/insights` API
endpoint backed by pandas.

**Python you learn:** Jupyter, `numpy` arrays and vectorisation, `pandas` DataFrames
(`groupby`, `resample`, `pivot_table`, `merge`, missing data), `matplotlib`/`seaborn`.

**Done when:** a notebook tells a clear story about a year of spending, and `/insights`
returns the same numbers.

## Phase 6 — First ML model: auto-categorisation (weeks 7–8)

**Build:** train a classifier on your tagged transactions that predicts the category of
new ones. Serve it: `POST /predict` and `ledger import --auto-tag`. Rule-based tagging
from Phase 3 becomes the fallback.

**ML you learn:** the supervised learning loop, train/validation/test split, features vs
labels, text → numbers (`TfidfVectorizer`), `LogisticRegression` vs `RandomForest`,
accuracy / precision / recall / confusion matrix, cross-validation, overfitting,
`Pipeline`, saving models with `joblib`, retraining when new tags come in.

**Done when:** model beats the rule engine on a held-out set, and the accuracy number is
in the README.

## Phase 7 — Forecasting and anomalies (weeks 9–10)

**Build:** "You'll likely spend ₹X next month" and "this transaction looks unusual".

**ML you learn:** regression (`LinearRegression`, gradient boosting), feature engineering
on dates, time-series basics (lag features, seasonality, walk-forward validation), MAE/RMSE,
unsupervised learning with `IsolationForest`, why baselines matter (naive "same as last
month" first).

**Done when:** forecast beats the naive baseline; anomaly flags appear in the API.

## Phase 8 — Deep learning intro (weeks 11–12)

**Build:** the same categoriser as a small neural network in PyTorch, then with
pretrained sentence embeddings. Compare against Phase 6 honestly.

**ML you learn:** tensors, autograd, `nn.Module`, loss functions, optimisers, training
loops, batching, embeddings, when deep learning is and isn't worth it.

**Done when:** a comparison table (sklearn vs NN vs embeddings) is in the README.

## Phase 9 — Ship it (week 13)

**Build:** Dockerfile, GitHub Actions running `ruff` + `pytest` on every push, deploy the
API somewhere free (Fly.io / Render), a proper README with screenshots.

**Done when:** a green CI badge and a public URL.

---

## After this

You'll have covered core Python, packaging, testing, a web framework, pandas, scikit-learn
and PyTorch. Natural next steps: Kaggle competitions, *Hands-On Machine Learning*
(Géron), fast.ai course, or deepening into one area (NLP, time series, MLOps).

## Reference material (use alongside, not instead of, building)

- Official tutorial: https://docs.python.org/3/tutorial/ (Phases 1–3)
- *Fluent Python* (Ramalho) for the "why" behind idioms (Phase 3+)
- *Python for Data Analysis* (McKinney, free online) (Phase 5)
- scikit-learn user guide (Phases 6–7)
- PyTorch official tutorials (Phase 8)

## Progress

- [ ] Phase 0 — Setup
- [ ] Phase 1 — CSV summary
- [ ] Phase 2 — Data model + SQLite
- [ ] Phase 3 — Package, importers, rules
- [ ] Phase 4 — FastAPI
- [ ] Phase 5 — pandas + notebooks
- [ ] Phase 6 — Categoriser
- [ ] Phase 7 — Forecast + anomalies
- [ ] Phase 8 — PyTorch
- [ ] Phase 9 — Ship
