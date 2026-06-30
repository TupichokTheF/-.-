from First_IT_Company.DDS.models import TransactionModel
from First_IT_Company.DDS.app.domains.transaction import Transaction
from First_IT_Company.DDS.app.infrastructure.mappers.transaction_mapper import TransactionMapper

class TransactionRepository:

    def get_all_transactions(self, filter_data) -> list[Transaction]:
        res = TransactionModel.objects.select_related(
            "status", "type", "sub_category__main_category__type"
        )

        if 'date_to' in filter_data:
            res.filter(created_at__lte=filter_data['date_to'])
        if 'date_from' in filter_data:
            res.filter(created_at__gte=filter_data['date_from'])
        if 'status_id' in filter_data:
            res.filter(status_id=filter_data['status_id'])
        if 'type_id' in filter_data:
            res.filter(status_id=filter_data['type_id'])
        if 'category_id' in filter_data:
            res.filter(sub_category__main_category_id=filter_data['category_id'])
        if 'sub_category_id' in filter_data:
            res.filter(sub_category_id=filter_data['sub_category_id'])

        return [TransactionMapper.to_entity(tr) for tr in res]

    def create_new_transaction(self, data_: dict) -> bool:
        tr = TransactionModel.objects.create(**data_)

        return True

    def delete_transaction_by_id(self, transaction_id: int):
        tr = TransactionModel.objects.get(id=transaction_id)
        tr.delete()

        return True
