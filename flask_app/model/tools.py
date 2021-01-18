import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor, SGDClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, classification_report
from sklearn.datasets import make_classification, make_regression


def read_data_regression():
    # data_path = config.DATA_PATH
    # data = pd.read_csv(data_path)

    # X = data.drop("label", axis=1).values
    # y = data["label"].values
    X, y = make_regression(n_samples=100, n_features=7)

    return X, y


def read_data_classification():
    # data_path = config.DATA_PATH
    # data = pd.read_csv(data_path)

    # X = data.drop("label", axis=1).values
    # y = data["label"].values
    X, y = make_classification(n_samples=100, n_features=7)

    return X, y


def model_search_regression(X_train, y_train):
    scaler = StandardScaler()
    model = SGDRegressor()
    model_pipeline = Pipeline([("scaler", scaler), ("model", model)])

    search_space = [{"model": [SGDRegressor()],
                     },
                    {"model": [RandomForestRegressor()],
                     "model__n_estimators": [50, 100],
                     "model__min_samples_leaf":[1, 5]
                     },
                    # {"model": [GradientBoostingRegressor()],
                    #  "model__n_estimators": [50, 100],
                    #  "model__learning_rate": [.05, .1]
                    # }
                    ]
    
    grid_search = GridSearchCV(model_pipeline,
                               search_space,
                               scoring='neg_mean_squared_error',
                               cv=2, verbose=0)

    grid_search_results = grid_search.fit(X_train, y_train)

    best_model_pipeline = grid_search_results.best_estimator_
    
    return best_model_pipeline


def model_search_classification(X_train, y_train):
    scaler = StandardScaler()
    model = SGDClassifier()
    model_pipeline = Pipeline([("scaler", scaler), ("model", model)])

    search_space = [{"model": [SGDClassifier()],
                     },
                    {"model": [RandomForestClassifier()],
                     "model__n_estimators": [50, 100],
                     "model__min_samples_leaf":[1, 5]
                     },
                    {"model": [GradientBoostingClassifier()],
                     "model__n_estimators": [50, 100],
                     "model__learning_rate": [.05, .1]
                     }
                    ]

    grid_search = GridSearchCV(model_pipeline,
                               search_space,
                               scoring='accuracy',
                               cv=2, verbose=0)

    grid_search_results = grid_search.fit(X_train, y_train)

    best_model_pipeline = grid_search_results.best_estimator_

    return best_model_pipeline


def evaluate_model_regression(model_pipeline, X_train, X_test,
                              y_train, y_test):

    pred_train = model_pipeline.predict(X_train)
    pred_test = model_pipeline.predict(X_test)

    rmse_train = np.sqrt(mean_squared_error(y_train, pred_train))
    rmse_test = np.sqrt(mean_squared_error(y_test, pred_test))

    print("Train RMSE:", rmse_train)
    print("Test RMSE:", rmse_test)


def evaluate_model_classification(model_pipeline, X_train, X_test,
                                  y_train, y_test):

    y_pred_train = model_pipeline.predict(X_train)
    y_pred_test = model_pipeline.predict(X_test)

    print("Classification Report on Train Data:")
    print(classification_report(y_train, y_pred_train))

    print("Classification Report on Test Data:")
    print(classification_report(y_test, y_pred_test))

