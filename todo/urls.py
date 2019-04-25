"""seraph URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from todoapp import views


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^todos/list/", views.get_todos, name="get_todos"),
    url(r"^todos/create/", views.create_todo, name="create_todo"),
    url(r"^todos/(?P<id>[0-9]+)/", views.get_todo, name="get_todo"),
    url(r"^todos/edit/(?P<id>[0-9]+)/", views.edit_todo, name="edit_todo"),
    url(r"^todos/delete/(?P<id>[0-9]+)/", views.delete_todo, name="delete_todo"),
    # APIS
    url(r"api/list/", views.get_api_todos, name="get_api_todos"),
    url(r"api/(?P<id>[0-9]+)/", views.get_api_todo, name="get_api_todo"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
