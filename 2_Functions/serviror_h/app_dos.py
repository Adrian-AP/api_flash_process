import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    
    return "Welcome to DL prediction"

@app.route('/pagina_')
def pagina():
    
    template_path = os.path.join('api_flash_process', '2_Functions', 'serviror_h', 'templates', 'frontend.html')
    return render_template('frontend.html')

@app.route('/x')
def hellox():
    
    return "Welcome to DL predictionx"


if __name__ == "__main__":
    
    app.run(port=5070)
    
    # # print(os.listdir('./api_flash_process/2_Functions/serviror_h/templates'))
    
    # template_path = os.path.join('Desktop', 'GIT_Parent','api_flash_process', '2_Functions', 'serviror_h', 'templates', 'index.html')
    # print(template_path)
