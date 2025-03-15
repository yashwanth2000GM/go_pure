# from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from PIL import Image
# import io
# from .model_loader import predict

# # Create your views here.

# def plant_model(request):
#     return HttpResponse("Hello World")

# @csrf_exempt  # Disable CSRF for testing (use proper security in production)
# def predict_disease(request):
#     if request.method == 'POST' and 'image' in request.FILES:
#         image_file = request.FILES['image']
#         image = Image.open(io.BytesIO(image_file.read())).convert('RGB')

#         result = predict(image)
#         return JsonResponse({"prediction": result})

#     return JsonResponse({"error": "Invalid request"}, status=400)




# from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from PIL import Image
# import io
# import logging
# from .model_loader import predict  # Import the prediction function

# # Setup logging
# logger = logging.getLogger(__name__)

# def plant_model(request):
#     """Simple test view."""
#     return HttpResponse("🌱 Plant Disease Detection API is Running!")

# @csrf_exempt  # Disable CSRF for testing (use proper security in production)
# def predict_disease(request):
#     if request.method == 'GET':
#         return JsonResponse({"message": "Send a POST request with an image to get predictions."})

#     if request.method == 'POST' and 'image' in request.FILES:
#         try:
#             image_file = request.FILES['image']
#             image = Image.open(io.BytesIO(image_file.read())).convert('RGB')

#             # Call the model prediction function
#             result = predict(image)

#             return JsonResponse({"prediction": result})

#         except Exception as e:
#             logger.error(f"❌ Error in prediction: {e}")
#             # return JsonResponse({"error": "Internal Server Error "+e}, status=500)
#             return JsonResponse({"error": f"Internal Server Error: {str(e)}"}, status=500)


#     return JsonResponse({"error": "Invalid request. Please upload an image."}, status=400)


from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import io
import logging
from .model_loader import predict  # Import the prediction function

# Setup logging
logger = logging.getLogger(__name__)

def plant_model(request):
    """Simple test view."""
    return HttpResponse("🌱 Plant Disease Detection API is Running!")

@csrf_exempt  # Disable CSRF for testing (use proper security in production)
def predict_disease(request):
    if request.method == 'GET':
        return JsonResponse({"message": "Send a POST request with an image to get predictions."})

    if request.method == 'POST' and 'image' in request.FILES:
        try:
            image_file = request.FILES['image']
            image = Image.open(io.BytesIO(image_file.read())).convert('RGB')

            # Call the model prediction function
            result = predict(image)

            return JsonResponse({"prediction": result})

        except Exception as e:
            logger.error(f"❌ Error in prediction: {e}")
            return JsonResponse({"error": f"Internal Server Error: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request. Please upload an image."}, status=400)
