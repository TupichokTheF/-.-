from django.contrib import admin
from .models import TransactionStatus, TransactionType, TransactionCategories, TransactionSubCategories, Transaction

admin.site.register([
    TransactionStatus, TransactionType,
    TransactionCategories, TransactionSubCategories, Transaction,
])