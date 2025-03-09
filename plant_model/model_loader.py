import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing import image
from PIL import Image

MODEL_PATH = r"E:\\yashwanth_cnn_ model\\deploy\\go_pure\\plant_model\\model\\yashwanth3(200e)_plantmodel.keras"

try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")

# Class labels (ensure they match your model's output classes)
CLASS_NAMES = [
    'Corn_commonrust', 'Corn_grayleafspot', 'Cotton_Aphids',
    "Cotton_Armyworm", "Tomato___Bacterial_spot", "Tomato___Early_blight"
]

def predict(img):
    """
    Predicts the disease class of the input image.

    Args:
        img (PIL.Image.Image): The image to classify.

    Returns:
        dict: The predicted class and confidence score.
    """
    if model is None:
        return {"error": "Model not loaded. Check the path and model file."}

    try:
        # Resize and normalize image
        img = img.resize((128, 128))  
        img_array = image.img_to_array(img) / 255.0  
        img_array = np.expand_dims(img_array, axis=0)  

        # Get predictions
        prediction = model.predict(img_array)
        predicted_class = CLASS_NAMES[np.argmax(prediction)]
        confidence = np.max(prediction)

        return {"class": predicted_class, "confidence": float(confidence)}

    except Exception as e:
        return {"error": f"Prediction failed: {e}"}
