from datetime import date
from django.db import models


class TransactionStatusModel(models.Model):
    status = models.CharField(max_length=40)

    class Meta:
        db_table = "transaction_statuses"

    def __str__(self):
        return self.status


class TransactionTypeModel(models.Model):
    type = models.CharField(max_length=40)

    class Meta:
        db_table = "transaction_types"

    def __str__(self):
        return self.type


class TransactionCategoriesModel(models.Model):
    type = models.ForeignKey(
        TransactionTypeModel,
        on_delete=models.CASCADE,
        related_name="categories"
    )
    category = models.CharField(max_length=40)

    class Meta:
        db_table = "transaction_categories"

    def __str__(self):
        return self.category


class TransactionSubCategoriesModel(models.Model):
    main_category = models.ForeignKey(
        TransactionCategoriesModel,
        on_delete=models.CASCADE,
        related_name="sub_categories"
    )
    sub_category = models.CharField(max_length=40)

    class Meta:
        db_table = "transaction_sub_categories"

    def __str__(self):
        return self.sub_category


class TransactionModel(models.Model):
    created_at = models.DateField(default=date.today)
    status = models.ForeignKey(
        TransactionStatusModel,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
    type = models.ForeignKey(
        TransactionTypeModel,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
    sub_category = models.ForeignKey(
        TransactionSubCategoriesModel,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    comment = models.TextField(blank=True, default="")

    class Meta:
        db_table = "transactions"