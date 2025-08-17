from django.contrib import admin
from django.urls import path
from api.views import postView
# swagger implementation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# for static files , ui
from django.conf import settings
from django.conf.urls.static import static
# api login/logout  session framework
from django.contrib.auth import views as auth_views
from django.urls import path, include



schema_view = get_schema_view(
    openapi.Info(
        title="Student API",# custom project name 
        default_version='v1',
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',postView,name='api'),
    path('api/<int:pk>/',postView,name='api'),
    # for login/logout
    path('auth/', include('rest_framework.urls')),  # adds /login/ and /logout/ session framework

    # swagger 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
     # ✅ Add this line:
    path('accounts/', include('django.contrib.auth.urls')),  # Adds /accounts/login/
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
