
from django.contrib import admin
from django.urls import path
from studentapp.views import profileall

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all/',profileall),
]
