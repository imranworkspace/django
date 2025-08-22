from django.contrib import admin
from django.urls import path
from api.views import registrationForm,homepage,logout,login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',registrationForm,name='reg'),
    path('home/',homepage,name='home'),
    path('logout/',logout,name='logout'),
    path('login/',login,name='login')
]
