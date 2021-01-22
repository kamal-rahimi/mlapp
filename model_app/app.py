from flask import Flask, request, jsonify, abort
import sys
import pickle
import numpy as np
import json
import time
import os
import logging
from model.train import train_model

FLASK_APP_PORT = 5000

MODEL_PATH = './model/model.pkl'

if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    
    logging.info("Model is loaded.")
else:
    logging.info(f"No trained model is found at '{MODEL_PATH}' path")

server = Flask(__name__)

@server.route("/", methods=["post", "get"])
def home():
    if model:
        response = f"<h1><center> Model is deployed! </center> </h1>"
    else:
        response = f"<h1><center> Model is not trained yet! </center> </h1>"
    return response

@server.route("/predict", methods=["post"])
def predict():
    start_time = time.time()

    if not request.json or "data" not in request.json:
        abort(400)

    data_req = request.get_json(force=True)
    data = np.array(data_req["data"])

    response = {}
    response["input_data"] = data.tolist()
    try:
        preditions = model.predict(data)
        # for i in pred:
        # result.append(dict(zip(le.classes_, i/sum(i))))
        response["result"] = "OK"
        response["predictions"] = preditions.tolist()
    except Exception as e:
        response["result"] = "FAILED"
        logging.error(e)

    response["time"] = round(time.time() - start_time, 4)

    logging.info(json.dumps(response))

    return response, 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=FLASK_APP_PORT, debug=True)
