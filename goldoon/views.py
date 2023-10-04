from django.shortcuts import render
from flower.models import flower
from blog.models import blog

def all_models(request):
    model1_objects = flower.objects.all()
    model2_objects = blog.objects.all()
    return render(request, 'main/all.html', {'model1_objects': model1_objects, 'model2_objects': model2_objects})
