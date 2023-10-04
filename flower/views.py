from django.shortcuts import render
from .models import flower
from blog.models import blog


# Create your views here.
def flower_list(request):
    flower_list = flower.objects.all()[:6]
    context = {
        "flowers" : flower_list
    }
    return render (request, "flower/HomePage.html" , context)

def all_flowers(request):
    all_flowers = flower.objects.all()
    context = {
        "flowers" : all_flowers
    }
    return render (request, "flower/FlowersPage.html" , context)

def flower_des(request , id):
    flower_detail = flower.objects.get(id = id)
    context = {
        "flower" : flower_detail
    }
    return render(request, "flower/flowerdetail.html", context)

def search(request):
    if request.method == "GET":
        q =request.GET.get("search")
    flower_list = flower.objects.filter(name__icontains=q)
    return render(request, "flower/searchresult.html" , {"flower_list": flower_list})



def decoration(request):
    model1_objects = flower.objects.all()
    model2_objects = blog.objects.all()
    return render(request, 'all.html', {'model1_objects': model1_objects, 'model2_objects': model2_objects})
