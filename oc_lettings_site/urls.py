from django.contrib import admin
from django.urls import path, include

from . import views


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include("letting.urls", namespace="letting")),
    path('profiles/', include("profile.urls", namespace="profile")),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
