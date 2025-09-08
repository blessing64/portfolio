from django.urls import path
from . import views
urlpatterns = [
    path("", views.projects, name="projects"),
    path("add/", views.add_project, name="add_project"),
    path("<int:pk>/", views.detail_project, name="detail_project"),
    path("delete/<int:pk>/", views.delete_project, name="delete_project"),
]