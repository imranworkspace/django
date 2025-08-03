
from django.contrib import admin
from django.urls import path
from myapp.views import studentView
# swagger implementation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# for docker
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
    openapi.Info(
        title="Student API",# custom project name 
        default_version='v1',
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myform/', studentView,name='myform'),
    # swagger 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) ## for docker
