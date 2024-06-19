"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

admin.site.index_title = "Админ панел"

schema_view = get_schema_view(
    openapi.Info(
        title="Giotto Urgench API",
        default_version="v1",
        description="Giotto Urgench backend",
        contact=openapi.Contact(
            email="chogirmali.yigit@gmail.com", url="https://t.me/chogirmali_yigit"
        ),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)


def admin_panel(request):
    return redirect("admin:index")


urlpatterns = [
    path("", admin_panel, name="admin-panel"),
    path("admin/", admin.site.urls),
    path(
        "api/",
        include(
            [
                path(
                    "v1/",
                    include(
                        [
                            path("shop/", include("shop.urls")),
                        ]
                    ),
                ),
            ]
        ),
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
