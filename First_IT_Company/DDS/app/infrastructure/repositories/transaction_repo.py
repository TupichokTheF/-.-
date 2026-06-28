from First_IT_Company.DDS.models import Transaction

class TransactionRepository:

    def get_all_transactions(self) -> list[Transaction]:
        res = Transaction.objects.all()

        return list(res.all())
