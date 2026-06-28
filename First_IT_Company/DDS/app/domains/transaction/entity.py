from dataclasses import dataclass, field
from decimal import Decimal
from datetime import datetime

from .value_objects import TransactionType, TransactionStatus

@dataclass(kw_only=True, eq=False)
class TransactionCategory:
    id: int
    type: TransactionType
    name: str

@dataclass(kw_only=True, eq=False)
class TransactionSubCategory:
    id: int
    main_category: TransactionCategory
    name: str

@dataclass(kw_only=True, eq=False)
class Transaction:
    id: int
    amount: Decimal
    comment: str
    created_at: datetime = field(default=datetime.now())
    status: TransactionStatus
    type: TransactionType
    sub_category: TransactionSubCategory