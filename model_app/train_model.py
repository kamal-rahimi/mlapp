from model.train import train_model
import os
import pickle

MODEL_PATH = 'model_app/model/model.pkl'

if __name__ == '__main__':

    model_pipeline = train_model()

    if hasattr(model_pipeline, "predict"):

        with open(MODEL_PATH, "wb+") as f:
            pickle.dump(model_pipeline, f)

        print(f"Model is trained and saved in: {MODEL_PATH}")
    else:
        print("The trained model does not have 'predict' attribute!")