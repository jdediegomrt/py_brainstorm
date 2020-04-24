from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('trivia/', include('trivia.urls')),
    path('admin/', admin.site.urls),
]
