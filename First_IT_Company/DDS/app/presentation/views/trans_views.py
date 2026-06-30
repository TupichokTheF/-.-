from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from First_IT_Company.DDS.app.logic.services import TransactionService
from First_IT_Company.DDS.app.infrastructure.repositories import TransactionRepository
from First_IT_Company.DDS.app.presentation.serializers.trans_serializers import (TransactionOutputSerializer,
                                                                               TransactionCreateInputSerializer,
                                                                               TransactionDeleteInputSerializer,
                                                                               TransactionFilterInputSerializer)


class TransactionView(APIView):

    def get(self, request):
        filter_serializer = TransactionFilterInputSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        transaction_service = TransactionService(TransactionRepository())
        transactions = transaction_service.get_transactions(filter_serializer.validated_data)

        serializer = TransactionOutputSerializer(transactions, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        transaction_service = TransactionService(TransactionRepository())
        try:
            transaction_service.create_transaction(serializer.validated_data)
        except Exception as e:
            raise ValidationError(str(e))

        return Response({"status": True})

    def delete(self, request):
        serializer = TransactionDeleteInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        transaction_service = TransactionService(TransactionRepository())
        transaction_service.delete_transaction(serializer.validated_data)

        return Response({"status": True})
