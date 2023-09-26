import joblib
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def train_model():
    # تعریف مدل و کامپایل آن
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', input_shape=[64, 64, 3]),
        tf.keras.layers.MaxPool2D(pool_size=2, strides=2),
        tf.keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu'),
        tf.keras.layers.MaxPool2D(pool_size=2, strides=2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(units=128, activation='relu'),
        tf.keras.layers.Dense(units=5, activation='softmax')
    ])
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

    # آموزش مدل با استفاده از دادگان آموزش و آزمون
    train_datagen = ImageDataGenerator(rescale=1./255)
    training_set = train_datagen.flow_from_directory(
        'Image_Processing/data_set/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical'
    )
    test_datagen = ImageDataGenerator(rescale=1./255)
    test_set = test_datagen.flow_from_directory(
        'Image_Processing/data_set/test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical'
    )
    model.fit(
        training_set,
        validation_data=test_set,
        epochs=30
    )

    # ذخیره مدل در فایل pickle
    joblib.dump(model, 'Image_Processing/utils/flower_model.pkl')

# train_model()