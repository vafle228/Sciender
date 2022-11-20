from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("sciender-api/v1", admin.site.urls)
]
