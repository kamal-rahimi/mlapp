import pickle
import numpy as np
import pandas as pd
import sklearn as sk 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import config

def train_model():
    data_path = config.DATA_PATH
    data = pd.read_csv(data_path)

    X = data.drop("label", axis=1).values
    y = data["label"].values

    model = LinearRegression()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

    model.fit(X_train, y_train)
    pred_train = model.predict(X_train)
    pred_test = model.predict(X_test)

    rmse_train = np.sqrt(mean_squared_error(y_train, pred_train))
    rmse_test = np.sqrt(mean_squared_error(y_test, pred_test))

    print("Train RMSE:", rmse_train)
    print("Test RMSE:", rmse_test)
    print("Model intercept:", model.intercept_)
    print("Model Coefficients", model.coef_)

    return model


if __name__ == '__main__':

    model = train_model()

    model_path = config.MODEL_PATH
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

