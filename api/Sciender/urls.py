from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),

    path(settings.API_ROOT, include("djoser.urls")),
    path(settings.API_ROOT, include("djoser.urls.authtoken")),
    
    path(settings.API_ROOT + "core/", include("CoreApp.urls")),
    path(settings.API_ROOT + "match/", include("MatchApp.urls")),
    path(settings.API_ROOT + "profile/", include("ProfileApp.urls")),
    path(settings.API_ROOT + "projects/", include("ProjectApp.urls")),
]
