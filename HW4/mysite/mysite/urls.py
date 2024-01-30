from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

urlpatterns = [
    #path("", ""),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
