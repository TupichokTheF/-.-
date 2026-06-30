from django.urls import path, include

urlpatterns = [
    path("dds/", include("First_IT_Company.DDS.app.presentation.urls.trans_urls")),
    path("dds/references/", include("First_IT_Company.DDS.app.presentation.urls.ref_urls")),
]