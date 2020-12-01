from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles
from ..models import Source

# Views
@main.route('/')
def index():
	'''
	view root page function that returns the index page and its data
	'''
    entertainment_sources = get_sources('entertainment')
    busness_sources = get_sources('business')
    technology_sources = get_sources('technology')
    health_sources = get_sources('health')
	science_sources = get_sources('science')
	general_sources = get_sources('general')
	sports_sources = get_sources('sports')
	title = "News"

	return render_template('index.html',title = title, entertainment = entertainment_sources, business = business_sources, technology =technology_sources, health = health_sources, science = science_sources, general = general_sources, sports = sports_sources)

@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'{id}'

	return render_template('articles.html',title= title,articles = articles)  