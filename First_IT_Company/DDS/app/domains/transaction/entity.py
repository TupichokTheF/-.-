from dataclasses import dataclass, field
from decimal import Decimal
from datetime import date

@dataclass(kw_only=True, eq=False)
class TransactionStatus:
    id: int
    status: str

    @classmethod
    def create(cls, id_: int, status_: str):
        return cls(id=id_, status=status_)

@dataclass(kw_only=True, eq=False)
class TransactionType:
    id: int
    type: str

    @classmethod
    def create(cls, id_: int, type_: str):
        return cls(id=id_, type=type_)

@dataclass(kw_only=True, eq=False)
class TransactionCategory:
    id: int
    type: TransactionType
    name: str

    @classmethod
    def create(cls, id_: int, type_: TransactionType, name_: str):
        return cls(id=id_, type=type_, name=name_)

@dataclass(kw_only=True, eq=False)
class TransactionSubCategory:
    id: int
    main_category: TransactionCategory
    name: str

    @classmethod
    def create(cls, id_: int, main_category_: TransactionCategory, name_: str):
        return cls(id=id_, main_category=main_category_, name=name_)

@dataclass(kw_only=True, eq=False)
class Transaction:
    id: int
    amount: Decimal
    comment: str
    created_at: date = field(default_factory=date.today)
    status: TransactionStatus
    type: TransactionType
    sub_category: TransactionSubCategory

    @classmethod
    def create(cls, id_: int,
               amount_: Decimal,
               comment_: str,
               status_: TransactionStatus,
               type_: TransactionType,
               sub_category_: TransactionSubCategory):
        return cls(id=id_, amount=amount_, comment=comment_, status=status_, type=type_, sub_category=sub_category_)