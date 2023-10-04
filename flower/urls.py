from .import views
from django.urls import path

app_name = "flower"

urlpatterns = [
    path("", views.flower_list, name = "flower_list"),
    path("flowers/", views.all_flowers, name = "all_flowers"),
    path("<int:id>", views.flower_des, name = "detail"),
    path("search/", views.search, name = "search"),
    path('all/', views.decoration, name='all_models')
]
    