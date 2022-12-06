"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from links import views

urlpatterns = [
    path('admin/', admin.site.urls),   # http://127.0.0.1:8000/admin/
    path('links/', views.links_list, name="videos-list"),    # http://127.0.0.1:8000/links/
    path('links/<int:pk>/', views.links_detail, name="videos-detail"), # http://127.0.0.1:8000/links/
    path('links-delete/<int:pk>/', views.links_delete, name="videos-delete"), # http://127.0.0.1:8000/links/
    path('links-create/', views.links_create, name="videos-create"), # http://127.0.0.1:8000/links/
    # 1. http://127.0.0.1:8000/links/*/            (URL)
    # 2. http://127.0.0.1:8000/links/?links_id=4 (Get)
    # 3. key:value, key:value                     (POST)
]
