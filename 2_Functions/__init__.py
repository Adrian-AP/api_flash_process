from flask import Flask
import pickle
from tensorflow.keras.models import load_model


# Initialize App
app = Flask(__name__)

# Load models
with open("model/model.pkl", "rb") as file:
    # carga los datos del archivo pickle
    model = pickle.load(file)
