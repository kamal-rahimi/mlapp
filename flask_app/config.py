
import os

dir_abs_path = os.path.abspath(os.path.dirname(__file__))
DATA_PATH = dir_abs_path + "/data/data.csv"
MODEL_PATH = dir_abs_path + "/model/model.pkl"

FLASK_APP_PORT = 5000
WSGI_APP_PORT = 8000