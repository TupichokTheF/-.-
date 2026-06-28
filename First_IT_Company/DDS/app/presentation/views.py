from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import

from First_IT_Company.DDS.models import Transaction
from First_IT_Company.DDS.app.logic.services import TransactionService
from First_IT_Company.DDS.app.infrastructure.repositories import TransactionRepository


class TransactionView(APIView):

    def get(self, request):
        transaction_service = TransactionService(TransactionRepository())
        transactions = transaction_service.get_all_transactions()

        return Response(transactions)

    def post(self, request):
        res = Transaction.objects.create()

        return Response({"status": True})