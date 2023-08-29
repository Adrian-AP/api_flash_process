from flask import Flask, render_template
import os

app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "¡Hola!!, mundo!"


@app.route('/')
def pagina():
    return render_template('./templates/index.html')

if __name__ == '__main__':
    
    app.run(port=5070)

