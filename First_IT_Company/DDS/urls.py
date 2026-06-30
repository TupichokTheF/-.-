from django.urls import path, include

urlpatterns = [
    path("dds/", include("First_IT_Company.DDS.app.presentation.urls"))
]