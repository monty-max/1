from django.conf import urls
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from djangoProject2.views import Test

#список твоих ссылок = админ дефолтная, пусть она всегда будет, там админка приложения, покажу позже
urlpatterns = [
    path('admin/', admin.site.urls)
]

router = DefaultRouter()

router.register('test', Test, basename='Test')

#тут мы объявили сваггер - то что ты видишь по ссылку /api/v1/swagger
schema_view_v1 = get_schema_view(
    openapi.Info(
        title="TEST, API",
        default_version='v1',
        description="",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="test@test.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
#а тут в нашим урлам добавиои этот сваггер += - значит что к сущ массиво добавилось то что после =
urlpatterns += [
    url(rf'^api/v1/swagger/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
urlpatterns += router.urls