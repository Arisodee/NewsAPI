from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_articles
from ..models import Source

#views
@main.route('/')
def index():
	'''
	Root function that returns index page and its data
	'''
	general_sources = get_sources('general')
	title = "News"

	return render_template('index.html', title=title, general=general_sources)
		

@main.route('/articles/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'{id}'

	return render_template('articles.html',title=title, articles=articles) 