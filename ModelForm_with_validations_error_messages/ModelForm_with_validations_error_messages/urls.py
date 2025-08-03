from django.contrib import admin
from django.urls import path
from studentapi.views import demo_reg,success_form
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myform/', demo_reg,name='myform'),
    path('success/',success_form,name='success'),
]
