from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework import permissions
from users.views import UserMixinViews
from todo_app.views import ProjectModelViewSet, TodoModelViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView

schema_view = get_schema_view(
    openapi.Info(
        title="api_service",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('users', UserMixinViews)
router.register('projects', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
