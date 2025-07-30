
from django.contrib import admin
from django.urls import path
from studentapp.views import demo_form,success
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myform/',demo_form,name='myform'),
    path('success/',success,name='success'),
]
