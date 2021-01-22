import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score

from .tools import (read_data_classification,
                    read_data_regression,
                    model_search_classification,
                    model_search_regression,
                    evaluate_model_classification,
                    evaluate_model_regression
                   )


def train_model():
    """Train a model

    Returns:
        model_pipeline: Model pipeline
    """

    X, y = read_data_classification()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

    model_pipeline = model_search_classification(X_train, y_train)
    print("Best Model Piepline:", model_pipeline)

    model_pipeline.fit(X_train, y_train)

    evaluate_model_classification(model_pipeline, X_train, X_test,
                                  y_train, y_test)

    return model_pipeline

