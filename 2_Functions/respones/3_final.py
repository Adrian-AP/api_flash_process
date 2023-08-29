import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    
    return "Welcome to testing model"

@app.route('/img')
def pagina():
    
    return render_template('frontend.html')


@app.route('/ax')
def pagino():
    
    return render_template('frontendj.html')


@app.route('/ab')
def paginox():
    
    return render_template('test.html')

@app.route('/testing')
def paginoxb():
    
    return render_template('test_dos.html')


if __name__ == "__main__":
    
    app.run(port=8053)