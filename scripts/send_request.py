import requests
import json
import numpy as np

data = np.random.randn(3, 7)

resp = requests.post("http://0.0.0.0:80/predict",
                     json={"data": data.tolist()})

print(resp.json())