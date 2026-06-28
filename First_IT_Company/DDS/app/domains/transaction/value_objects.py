from dataclasses import dataclass


@dataclass(frozen=True)
class TransactionStatus:
    value: str

@dataclass(frozen=True)
class TransactionType:
    value: str