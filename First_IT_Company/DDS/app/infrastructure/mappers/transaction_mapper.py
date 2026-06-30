from First_IT_Company.DDS.models import TransactionModel, TransactionSubCategoriesModel
from First_IT_Company.DDS.app.domains.transaction import (
    TransactionType,
    TransactionStatus,
    TransactionCategory,
    TransactionSubCategory,
    Transaction)

from decimal import Decimal

class TransactionMapper:

    @classmethod
    def to_entity(cls, transaction_: TransactionModel) -> Transaction:
        tr_type = TransactionType.create(transaction_.type.id, transaction_.type.type)
        tr_status = TransactionStatus.create(transaction_.status.id, transaction_.status.status)
        tr_category = TransactionCategory.create(transaction_.sub_category.main_category.id,
                                                 tr_type,
                                                 transaction_.sub_category.main_category.category)
        tr_sub_category = TransactionSubCategory.create(transaction_.sub_category.id, tr_category, transaction_.sub_category.sub_category)
        tr = Transaction.create(id_=transaction_.id,
                                amount_=Decimal(transaction_.amount),
                                comment_=transaction_.comment,
                                status_=tr_status,
                                type_=tr_type,
                                sub_category_=tr_sub_category)

        return tr

class TransactionSubCategoryMapper:

    @classmethod
    def to_entity(cls, transaction_sub_category_: TransactionSubCategoriesModel) -> TransactionSubCategory:
        tr_type = TransactionType.create(transaction_sub_category_.main_category.type.id,
                                         transaction_sub_category_.main_category.type.type)
        tr_category = TransactionCategory.create(transaction_sub_category_.main_category.id,
                                                 tr_type,
                                                 transaction_sub_category_.main_category.category)
        tr_sub_category = TransactionSubCategory.create(transaction_sub_category_.id,
                                                        tr_category,
                                                        transaction_sub_category_.sub_category)

        return tr_sub_category
