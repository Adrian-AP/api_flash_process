# Local imports
import datetime

# Third part imports
from flask import request
import pandas as pd

from ms import app
from ms.functions import get_model_response

from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


model_file = 'model.pkl'
version = "v1.0.0"


app = Flask(__name__)

# Variable global para almacenar los datos de la foto
datos_de_la_foto = 'datos/datos_de_la_foto'

@app.route('/subir_foto', methods=['POST'])
def subir_foto():
    global datos_de_la_foto
    imagen = request.files['foto']

    # Procesar la imagen y almacenar los datos
    foto = Image.open(imagen)
    foto = foto.resize((224, 224))  # Ajustar al tamaño requerido
    foto_array = np.array(foto) / 255.0  # Convertir a arreglo numpy y normalizar
    foto_array = np.expand_dims(foto_array, axis=0)  # Agregar dimensión de lote
    datos_de_la_foto = foto_array

    return "Foto recibida y datos almacenados."

@app.route('/predict', methods=['POST'])
def predict():
    global datos_de_la_foto

    if datos_de_la_foto is None:
        return "Primero debes subir una foto."

    nombres_clases = ['Bacterial_spot', 'Early_blight', 'Late_blight', 'Leaf_Mold', 'Septoria_leaf_spot',
                      'Target_Spot', 'Tomato_Yellow_Leaf_Curl_Virus', 'Tomato_mosaic_virus',
                      'Two-spotted_spider_mite', 'healthy']
    
    # Cargar y usar el modelo para la predicción
    # Supongamos que "model" es un modelo previamente cargado
    predicciones = model.predict(datos_de_la_foto)
    indice_prediccion = np.argmax(predicciones)
    nombre_clase_predicha = nombres_clases[indice_prediccion]

    return jsonify({"clase_predicha": nombre_clase_predicha})

@app.route('/')
def index():
    return render_template('body/index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
