

class TransactionService:

    def __init__(self, transaction_repo_):
        self._transaction_repo = transaction_repo_

    def get_all_transactions(self):
        transactions = self._transaction_repo.get_all_transactions()

        return transactions