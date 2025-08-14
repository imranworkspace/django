
from django.contrib import admin
from django.urls import path
from studentapp.views import set_session_view,get_session_view,flush_session_view,view_methods
urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/', set_session_view),
    path('get/', get_session_view),
    path('flush/', flush_session_view),
    path('views/', view_methods),
]
