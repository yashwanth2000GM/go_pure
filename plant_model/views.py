from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import io
from .model_loader import predict

# Create your views here.

def plant_model(request):
    return HttpResponse("Hello World")

@csrf_exempt  # Disable CSRF for testing (use proper security in production)
def predict_disease(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image_file = request.FILES['image']
        image = Image.open(io.BytesIO(image_file.read())).convert('RGB')

        result = predict(image)
        return JsonResponse({"prediction": result})

    return JsonResponse({"error": "Invalid request"}, status=400)
