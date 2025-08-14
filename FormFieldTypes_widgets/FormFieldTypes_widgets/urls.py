from django.contrib import admin
from django.urls import path
from studentapp.views import demo_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myform/', demo_form,name='myform'),
]
