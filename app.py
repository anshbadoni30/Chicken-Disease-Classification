from flask import Flask, request, jsonify, render_template
import os

import base64
from flask_cors import CORS, cross_origin
from src.cnnClassifier.utils.common import decodeImage
from src.cnnClassifier.pipeline.predict import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"




@cross_origin()
@app.route('/predict', methods=['POST'])
def predictRoute():
    # Step 1: Get the base64 string
    image_base64 = request.json['image']

    # Step 2: Decode it to bytes
    image_data = base64.b64decode(image_base64)

    # Step 3: Save the decoded bytes to file
    with open(clApp.filename, 'wb') as f:
        f.write(image_data)

    # Step 4: Predict
    result = clApp.classifier.predict()
    print(result)

    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    # app.run(host='0.0.0.0', port=8080) #local host
    # app.run(host='0.0.0.0', port=8080) #for AWS
    app.run(host='0.0.0.0', port=80, debug=True) #for AZURE http://127.0.0.1/