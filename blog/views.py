from django.shortcuts import render
from .models import blog, category

# Create your views here.
def blog_list(request):
    blog_list = blog.objects.all()
    category_list = category.objects.all()
    context = {
        "blogs" : blog_list,
        "categories" : category_list
    }
    return render (request, "blog/blogpage.html" , context)

def blog_det(request , id):
    blog_detail = blog.objects.get(id = id)
    Recents = blog.objects.all().order_by("-created_at")[:10]
    context = {
        "blog" : blog_detail,
        "recents" : Recents,
         
    }
    return render(request, "blog/blog_detail.html", context)