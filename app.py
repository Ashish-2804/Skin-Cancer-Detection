from flask import Flask, request, render_template,url_for
import cv2
import numpy as np
import os
import tensorflow
import keras
import joblib
from keras.models import load_model

app = Flask(__name__)
pred_id=joblib.load('pred_id.joblib')
data=joblib.load('data.joblib')
model = load_model('Skin_Cancer_FT.hdf5')
unique_labels = joblib.load('unique_labels.joblib')
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def get_pred_label(prediction_probabilities):
    return unique_labels[np.argmax(prediction_probabilities)]
@app.route("/", methods=["GET", "POST"])
def index():
    pred_label = ''
    image_url = None
    pred=''
    if request.method == "POST":
        if "file" in request.files:
            image_file = request.files["file"]
            if image_file.filename != '':

                image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
                image_file.save(image_path)
                image = cv2.imread(image_path)
                new_shape = (224, 224)
                resized_img = cv2.resize(image, new_shape)
                input_data = np.expand_dims(resized_img, axis=0)
                pred_prob, image = model.predict(input_data), image
                pred_label = get_pred_label(pred_prob)
                print(pred_label)
                image_url = url_for('static', filename=image_file.filename)
                pred=pred_id[pred_label]
    return render_template("index.html", prediction=pred_label, image_url=image_url, prediction_id=pred)
@app.route("/details/<prediction_id>")
def details(prediction_id):
    print("Prediction ID:", prediction_id)
    details = data[unique_labels[int(prediction_id)]]
    return render_template("details.html", details=details)
if __name__ == "__main__":
    app.run(debug=True)