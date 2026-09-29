from dataclasses import dataclass
from enum import StrEnum


class Category(StrEnum):
    SALARY = "salary"
    FOOD = "food"
    SHOPPING = "shopping"
    TRAVEL = "travel"
    DAILY = "daily"
    OTHER = "other"


@dataclass
class Transaction:
    date: str
    merchant: str
    amount: float
    category: Category | None = Category.OTHER
    id: int | None = None
