from First_IT_Company.DDS.models import TransactionModel, TransactionSubCategoriesModel
from First_IT_Company.DDS.app.domains.transaction import Transaction
from First_IT_Company.DDS.app.infrastructure.mappers.transaction_mapper import TransactionMapper, TransactionSubCategoryMapper
from .exceptions import TransactionNotFound, SubCategoryNotFound

class TransactionRepository:

    def get_transaction_sub_category_by_id(self, sub_category_id: int):
        res = TransactionSubCategoriesModel.objects.select_related(
            "main_category__type"
        ).filter(id=sub_category_id).first()
        if not res:
            raise SubCategoryNotFound(f"Sub category with id={sub_category_id} was not found")

        return TransactionSubCategoryMapper.to_entity(res)


    def get_all_transactions(self, filter_data: dict) -> list[Transaction]:
        res = TransactionModel.objects.select_related(
            "status", "type", "sub_category__main_category__type"
        )

        if 'date_to' in filter_data:
            res = res.filter(created_at__lte=filter_data['date_to'])
        if 'date_from' in filter_data:
            res = res.filter(created_at__gte=filter_data['date_from'])
        if 'status_id' in filter_data:
            res = res.filter(status_id=filter_data['status_id'])
        if 'type_id' in filter_data:
            res = res.filter(type_id=filter_data['type_id'])
        if 'category_id' in filter_data:
            res = res.filter(sub_category__main_category_id=filter_data['category_id'])
        if 'sub_category_id' in filter_data:
            res = res.filter(sub_category_id=filter_data['sub_category_id'])

        return [TransactionMapper.to_entity(tr) for tr in res]

    def create_new_transaction(self, data_: dict) -> Transaction:
        tr = TransactionModel.objects.create(**data_)

        return TransactionMapper.to_entity(tr)

    def delete_transaction_by_id(self, transaction_id: int):
        tr = TransactionModel.objects.filter(id=transaction_id).first()
        if tr is None:
            raise TransactionNotFound(f"Transaction with id={transaction_id} was not found")
        tr.delete()

        return True
