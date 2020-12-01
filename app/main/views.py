from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles
from ..models import Source

#views
@main.route('/')
def index():
	'''
	view root page function that returns index page and its data
	'''

	entertainment_sources = get_sources('entertainment')
	health_sources = get_sources('health')
	general_sources = get_sources('general')
	science_sources = get_sources('science')
	sports_sources = get_sources('sports')
	technology_sources = get_sources('technology')
	business_sources = get_sources('business')
	title = "News"
	 

	return render_template('index.html', entertainment=entertainment_sources, health=health_sources, general=general_sources, science=science_sources, sports=sports_sources, technology=technology_sources, business=business_sources)

@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('articles.html',title=title, articles=articles) 