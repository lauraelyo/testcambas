from django.urls import include, path
from . import views

urlpatterns = [
    path('view_profile/edit_profile/', views.edit_profile, name="edit_profile"),
]
