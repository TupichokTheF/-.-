from First_IT_Company.DDS.app.domains.transaction import Transaction

class TransactionService:

    def __init__(self, transaction_repo_):
        self._transaction_repo = transaction_repo_

    def get_transactions(self, filter_data) -> list[Transaction]:
        transactions = self._transaction_repo.get_all_transactions(filter_data)

        return transactions

    def create_transaction(self, transaction_data: dict) -> bool:
        self._transaction_repo.create_new_transaction(transaction_data)

        return True

    def delete_transaction(self, transaction_data: dict):
        self._transaction_repo.delete_transaction_by_id(transaction_data["id"])

        return True
