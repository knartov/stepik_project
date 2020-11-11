from flask import Flask, render_template
import data

title = data.title
subtitle = data.subtitle
description = data.description
departures = data.departures
tours = data.tours

app = Flask(__name__)

@app.route('/')  
def main():
    return render_template('index.html', title = title, subtitle=subtitle, tours = tours)

@app.route('/departures/<departure>')  
def departures(departure):
	return render_template('departure.html', departure = f'{departure}')

@app.route('/tours/<id>/')
def tours(id):
    return render_template('tour.html', tour = f'{id}', tours = tours)

@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!", 404

@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим!", 500

app.run()