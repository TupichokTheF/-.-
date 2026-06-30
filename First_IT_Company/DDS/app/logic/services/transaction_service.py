from First_IT_Company.DDS.app.domains.transaction import Transaction
from First_IT_Company.DDS.app.infrastructure.repositories import TransactionRepository, TransactionNotFound
from .exceptions import InvalidTransactionType, InvalidTransactionId

class TransactionService:

    def __init__(self, transaction_repo_: TransactionRepository):
        self._transaction_repo = transaction_repo_

    def get_transactions(self, filter_data) -> list[Transaction]:
        transactions = self._transaction_repo.get_all_transactions(filter_data)

        return transactions

    def create_transaction(self, transaction_data: dict) -> bool:
        transaction_sub_category = self._transaction_repo.get_transaction_sub_category_by_id(transaction_data['sub_category_id'])
        if transaction_sub_category.main_category.type.id != transaction_data['type_id']:
            raise InvalidTransactionType("Invalid transaction type for chosen category")

        self._transaction_repo.create_new_transaction(transaction_data)

        return True

    def delete_transaction(self, transaction_data: dict):
        try:
            self._transaction_repo.delete_transaction_by_id(transaction_data["id"])
        except TransactionNotFound as e:
            raise InvalidTransactionId(str(e))

        return True
