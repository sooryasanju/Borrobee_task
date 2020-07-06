from django.urls import path
from . import views
urlpatterns=[
    path("list", views.get_list, name="list"),
    path("home", views.get_home, name="home"),
    path("add", views.add_reminder, name="add"),
    path("view/<int:pk>",views.get_view,name="get_view"),
    path("edit/<int:pk>",views.get_edit,name="update"),


]