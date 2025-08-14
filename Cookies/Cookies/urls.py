
from django.contrib import admin
from django.urls import path
from cookieapp.views import set_cookieview,get_cookieview,del_cookieview,set_signed_cookie_view,get_signed_cookie_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/',set_cookieview,name='set'),
    path('get/',get_cookieview,name='get'),
    path('del/',del_cookieview,name='del'),
    path('set_signed/',set_signed_cookie_view,name='set_signed'),
    path('get_signed/',get_signed_cookie_view,name='get_signed')
]
