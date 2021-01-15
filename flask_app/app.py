from flask import Flask, request, jsonify, abort
import sys
import pickle
import numpy as np
import json
import time

server = Flask(__name__)

MODEL_NAME = "model.pkl"

with open("model/"+MODEL_NAME, "rb") as f:
    model = pickle.load(f)

@server.route("/", methods=["post", "get"])
def home():
    if request.method == "POST":
        return {"model": f"{MODEL_NAME}"}
    else:
        return f"<h1><center> model name: {MODEL_NAME} </center> </h1>"

@server.route("/predict", methods=["post"])
def predict():
    start_time = time.time()

    if not request.json or "data" not in request.json:
        abort(400) 

    data_req = request.get_json(force=True)
    data = np.array(data_req["data"])

    preditions = model.predict(data)

    print(preditions)

    # for i in pred:
    # 		result.append(dict(zip(le.classes_, i/sum(i))))
    
    response = {
        "input": data.tolist(),
        "predictions": preditions.tolist(), 
        "time": round(time.time() - start_time, 6)
        }

    return jsonify(response), 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000, debug=True)