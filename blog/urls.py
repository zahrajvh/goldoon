from .import views
from django.urls import path

app_name = "blog"

urlpatterns = [
    path("", views.blog_list, name = "blog"),
    path("blog/<int:id>", views.blog_det, name = "blog_detail")
]


