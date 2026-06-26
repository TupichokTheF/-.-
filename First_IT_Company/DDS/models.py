from datetime import date
from django.db import models


class TransactionStatus(models.Model):
    status = models.CharField(max_length=40)

    def __str__(self):
        return self.status


class TransactionType(models.Model):
    type = models.CharField(max_length=40)

    def __str__(self):
        return self.type


class TransactionCategories(models.Model):
    type = models.ForeignKey(
        TransactionType,
        on_delete=models.CASCADE,
        related_name="categories"
    )
    category = models.CharField(max_length=40)

    def __str__(self):
        return self.category


class TransactionSubCategories(models.Model):
    main_category = models.ForeignKey(
        TransactionCategories,
        on_delete=models.CASCADE,
        related_name="sub_categories"
    )
    sub_category = models.CharField(max_length=40)

    def __str__(self):
        return self.sub_category


class Transaction(models.Model):
    created_at = models.DateField(default=date.today)
    status = models.ForeignKey(
        TransactionStatus,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
    type = models.ForeignKey(
        TransactionType,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
    sub_category = models.ForeignKey(
        TransactionSubCategories,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    comment = models.TextField(blank=True, default="")