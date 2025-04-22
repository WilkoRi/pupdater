from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("dashboard/", include("dashboard.urls")),
    path("admin/", admin.site.urls),
    path("pupdater/", include("pupdater.urls")),  # ✅ dit is cruciaal
]
