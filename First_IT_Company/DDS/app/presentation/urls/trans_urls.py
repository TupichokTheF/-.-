from django.urls import path

from First_IT_Company.DDS.app.presentation.views.trans_views import TransactionView

urlpatterns = [
    path('transactions/', TransactionView.as_view())
]