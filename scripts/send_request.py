import requests
import json
import numpy as np

IP_ADDRESS = 'localhost'

data = np.random.randn(3, 7)

resp = requests.post(f"http://{IP_ADDRESS}:80/predict",
                     json={"data": data.tolist()})

print(resp.json())