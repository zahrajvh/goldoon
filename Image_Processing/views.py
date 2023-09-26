from django.shortcuts import render
from .forms import Processing_form
from flower.models import flower
from .utils.image_processor import classify_flower

    
# Create your views here.
def process(request):
    processing = Processing_form()
    if request.method == "POST":
        processing = Processing_form(request.POST, request.FILES)
        image = request.FILES.get('photo')
        result = classify_flower(image)

        Flower_detected = flower.objects.get(name=result)
        context = {
            'flower': Flower_detected
        }
        return render(request, 'flower/flowerdetail.html', context)
        return render(request, 'Image_Processing/result.html', {'result': result, 'flower': flower})
        # return render(request, 'Image_Processing/result.html', {'result': result})  # نمایش صفحه نتیجه به کاربر

    else:
        print(processing.errors)
        processing = Processing_form()
    
    context = {
        "form" : processing
    }

    return render(request, "Image_Processing/processingPage.html", context)
