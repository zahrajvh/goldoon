import numpy as np
import tensorflow as tf
import joblib
import tempfile
import os
from PIL import Image, UnidentifiedImageError


def classify_flower(image):
    # بارگیری مدل از فایل pickle
    model = joblib.load('Image_Processing/utils/flower_model.pkl')

    # Save the uploaded image to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_image:
        temp_image.write(image.read())
        temp_image_path = temp_image.name

    # بررسی قابل شناسایی بودن تصویر
    try:
        Image.open(temp_image_path)
    except (IOError, UnidentifiedImageError):
        # حذف فایل موقت
        os.remove(temp_image_path)
        return 'تصویر نامعتبر است'

    # ارزیابی تصویر
    test_image = tf.keras.preprocessing.image.load_img(temp_image_path , target_size=(64, 64))
    test_image = tf.keras.preprocessing.image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    result = model.predict(test_image)
    if np.argmax(result) == 0:
        return('Daisy')
    elif np.argmax(result) == 1:
        return('Dandelion')
    elif np.argmax(result) == 2:
        return('Rose')
    elif np.argmax(result) == 3:
        return('Sunflower')
    elif np.argmax(result) == 4:
        return('Tulip')