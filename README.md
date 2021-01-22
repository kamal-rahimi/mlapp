# MLAPP
## A template repository to train a Machine Learning model and deploy it as Docker Microservices using Flask, Unicorn and Nginx.

## Train Model

To train the model, run:
```
python3 -m pip install model_app/requirements.txt

python model_app/train_model.py
```

## Deploy Model
To deploy the model as Microservice using Flask, Unicorn and Nginx run:

```
sudo sh deploy_model.sh
```

## Use the Model for Predictions
To check wheather the model deployed succesfully, go to "0.0.0.0" address in a browser.

To use model for prediction, send HTTP POST requests to '0.0.0.0/predict' address.
e.g.,
```
curl --header "Content-Type: application/json" \
 --request POST --data '{"data":[[0,0,0,0,0,0,0]]}' \
 http://localhost:80/predict
```
You can also use the following helpper scripts to send prediction request to the model:
```
sh scripts/curl_get_request.sh
sh scripts/curl_post_request.sh
python3 scripts/send_request.py
```

## Remove the Deployment
To remove the deployed model, run:
```
sudo sh destroy_deployment.sh
```

