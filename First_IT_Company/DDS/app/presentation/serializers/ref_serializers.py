from rest_framework import serializers
from First_IT_Company.DDS.models import (
    TransactionStatusModel,
    TransactionTypeModel,
    TransactionCategoriesModel,
    TransactionSubCategoriesModel,
)


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionStatusModel
        fields = ["id", "status"]


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionTypeModel
        fields = ["id", "type"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionCategoriesModel
        fields = ["id", "category", "type"]


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionSubCategoriesModel
        fields = ["id", "sub_category", "main_category"]