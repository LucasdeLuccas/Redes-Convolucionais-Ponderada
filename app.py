from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import io

app = Flask(__name__)
model = load_model('pesos.h5')

def prepare_image(image):
    image = image.resize((28, 28)).convert('L')
    image = np.array(image).reshape(1, 28, 28, 1).astype('float32') / 255
    return image

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    image = Image.open(io.BytesIO(file.read()))
    image = prepare_image(image)
    prediction = model.predict(image)
    digit = np.argmax(prediction)
    return render_template('predict.html', digit=digit)


if __name__ == "__main__":
    app.run(debug=True)
