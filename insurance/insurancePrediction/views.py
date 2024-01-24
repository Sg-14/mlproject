from django.shortcuts import render

# Create your views here.

def predictView(request):
    context = {}
    return render(request, "views/predict.html", context)