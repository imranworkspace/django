from django.contrib import admin
from django.urls import path
from studentapp.views import demo_form,success_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myform/', demo_form,name='myform'),
    path('success/', success_form,name='success'),
]
