from django.urls import path
from ..views.ref_views import (
    StatusListCreateView, StatusDetailView,
    TypeListCreateView, TypeDetailView,
    CategoryListCreateView, CategoryDetailView,
    SubCategoryListCreateView, SubCategoryDetailView,
)

urlpatterns = [
    path("statuses/", StatusListCreateView.as_view()),
    path("statuses/<int:pk>/", StatusDetailView.as_view()),

    path("types/", TypeListCreateView.as_view()),
    path("types/<int:pk>/", TypeDetailView.as_view()),

    path("categories/", CategoryListCreateView.as_view()),
    path("categories/<int:pk>/", CategoryDetailView.as_view()),

    path("sub-categories/", SubCategoryListCreateView.as_view()),
    path("sub-categories/<int:pk>/", SubCategoryDetailView.as_view()),
]