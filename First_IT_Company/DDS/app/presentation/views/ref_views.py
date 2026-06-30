from rest_framework import generics
from First_IT_Company.DDS.models import (
    TransactionStatusModel,
    TransactionTypeModel,
    TransactionCategoriesModel,
    TransactionSubCategoriesModel,
)
from ..serializers.ref_serializers import (
    StatusSerializer,
    TypeSerializer,
    CategorySerializer,
    SubCategorySerializer,
)


class StatusListCreateView(generics.ListCreateAPIView):
    queryset = TransactionStatusModel.objects.all()
    serializer_class = StatusSerializer

class StatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransactionStatusModel.objects.all()
    serializer_class = StatusSerializer


class TypeListCreateView(generics.ListCreateAPIView):
    queryset = TransactionTypeModel.objects.all()
    serializer_class = TypeSerializer

class TypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransactionTypeModel.objects.all()
    serializer_class = TypeSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = TransactionCategoriesModel.objects.select_related("type").all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransactionCategoriesModel.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = TransactionSubCategoriesModel.objects.select_related("main_category").all()
    serializer_class = SubCategorySerializer

class SubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransactionSubCategoriesModel.objects.all()
    serializer_class = SubCategorySerializer