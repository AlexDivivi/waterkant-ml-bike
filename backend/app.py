import logging
from flask_cors import CORS
import connexion

def get_weather(dtime):
    weather = None # TODO: implement here weather API calls for given dtime
    return weather

def get_prediction(dtime):
    weather = get_weather(dtime)
    # TODO: build an feature array, one-hot-encode the categorical features and use model.predict
    return # prediction

logging.basicConfig(level=logging.INFO)

app = connexion.App(__name__, specification_dir='swagger/')
app.add_api('api.yaml')

# add CORS support
CORS(app.app)

# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

if __name__ == '__main__':
    # run our standalone server
    app.run(port=8080)
    # TODO: load here machine learning model