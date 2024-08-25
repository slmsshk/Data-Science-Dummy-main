from flask import Flask, request, jsonify
import numpy as np
from classifiers import *
from pipeline import *
from tensorflow.keras.preprocessing.image import ImageDataGenerator

app = Flask(__name__)

# Load the model and its pretrained weights
classifier = Meso4()
classifier.load('weights/Meso4_DF.h5')

# Minimal image generator
dataGenerator = ImageDataGenerator(rescale=1./255)
generator = dataGenerator.flow_from_directory(
    'test_images',
    target_size=(256, 256),
    batch_size=1,
    class_mode='binary',
    subset='training'
)

@app.route('/predict', methods=['POST'])
def predict():
    # send image data through the request
    X, y = generator.next()
    prediction = classifier.predict(X)
    response = {
        'Predicted': str(prediction),
        'Real class': str(y)
    }
    return jsonify(response)

@app.route('/predict_video', methods=['POST'])
def predict_video():
    # Load the second set of weights
    classifier.load('weights/Meso4_F2F.h5')

    # Compute predictions for video dataset
    predictions = compute_accuracy(classifier, 'test_videos')
    response = {video_name: str(predictions[video_name][0]) for video_name in predictions}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
