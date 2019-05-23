from django.urls import include, path
from . import views

urlpatterns = [
    path('page_info/', views.page_info, name="page_info"),
]
