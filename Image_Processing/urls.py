from django.urls import path
from .import views

app_name = "Image_Processing"

urlpatterns = [
    path('', views.process, name="pocess" )
]
