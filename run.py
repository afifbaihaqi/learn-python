import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kompas')
def kompas_tren():
    data_1 = requests.get('https://www.kompas.com/tren')
    tren = BeautifulSoup(data_1.text, 'html.parser')
    tren_area = tren.find(attrs={'class': 'col-bs10-7'})

    titles = tren_area.findAll(attrs={'class': 'trenLatest__title'})
    images = tren_area.findAll(attrs={'class': 'trenLatest__img'})

    return render_template('index.html', images=images)
if __name__ == '__main__':
    app.run(debug=True)
