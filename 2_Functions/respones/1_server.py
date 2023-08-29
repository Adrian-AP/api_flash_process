
## Libraries ##

import pandas as pd
from plotnine import *
from io import BytesIO
from flask import *
import os


import warnings
warnings.filterwarnings("ignore")




## Read data ## --> It comes directly from github

url = "https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
gapminder_df = pd.read_csv(url)

gapminder_df = gapminder_df[['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap']]


## Server ## --> Instance of apiflash class

app = Flask(__name__)

## Functions ## -->  Associated to instanced model

# First function --> It returns a json where is included all inromation related to a country

@app.route('/continent_pop', methods=['POST'])
def continent_pop():
    # Consigo los datos de la petición
    data = request.get_json(force=True)

    continent = data['continent']
   
    year = data['year']
    
    result = gapminder_df.loc[(gapminder_df['continent']==continent) & 
                       
                       (gapminder_df['year']== year)]

    # La predicción la convierto a un JSON
    return jsonify(result.to_json(orient='records'))


## Landingpage ## --> first local page

@app.route('/')
def hello():

    return "Welcome to countries prediction"


## Country graphic

@app.route('/pais_life')
def pais_life():
    # Consigo los datos de la petición
    data = request.get_json(force=True)

    pais = data['country']
    title = data['title']
    
    result = gapminder_df.loc[(gapminder_df['country']==pais)]
    
    chart = (ggplot(result)
             + aes(x='year', y='lifeExp')
             + geom_line()
             + labs( title =  title, x = "Year", y = "Life exp")
             + theme_bw()
            )
    
    # renderiza el gráfico como una imagen PNG
    img = BytesIO()
    chart.save(img, format="png")
    
    # Regresa el archivo PNG al cliente
    img.seek(0)

    
    return send_file(img, mimetype="image/png")
    

if __name__ == "__main__":
    
    print("Hello ongoing")
    
    app.run(port=8052)