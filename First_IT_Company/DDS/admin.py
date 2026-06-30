from django.contrib import admin
from .models import (
    TransactionStatusModel,
    TransactionTypeModel,
    TransactionCategoriesModel,
    TransactionSubCategoriesModel,
    TransactionModel)

admin.site.register([
    TransactionStatusModel, TransactionTypeModel,
    TransactionCategoriesModel, TransactionSubCategoriesModel, TransactionModel,
])