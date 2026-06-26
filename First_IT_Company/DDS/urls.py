from django.urls import path, include

urlpatterns = [
    path("/dds", include("DDS.presentation.urls"))
]