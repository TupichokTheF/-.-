from rest_framework import serializers


class TransactionOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    created_at = serializers.DateField()
    amount = serializers.DecimalField(max_digits=14, decimal_places=2)
    comment = serializers.CharField()
    status = serializers.CharField(source="status.status")
    type = serializers.CharField(source="type.type")
    category = serializers.CharField(source="sub_category.main_category.name")
    sub_category = serializers.CharField(source="sub_category.name")

class TransactionCreateInputSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=14, decimal_places=2)
    comment = serializers.CharField()
    status_id = serializers.IntegerField()
    type_id = serializers.IntegerField()
    sub_category_id = serializers.IntegerField()

class TransactionDeleteInputSerializer(serializers.Serializer):
    id = serializers.IntegerField()

class TransactionFilterInputSerializer(serializers.Serializer):
    date_from = serializers.DateField(required=False)
    date_to = serializers.DateField(required=False)
    status_id = serializers.IntegerField(required=False)
    type_id = serializers.IntegerField(required=False)
    category_id = serializers.IntegerField(required=False)
    sub_category_id = serializers.IntegerField(required=False)