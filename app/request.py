import urllib.request,json
from .models import Source, Article
from datetime import datetime
import os

#getting the api key
api_key = None

#getting the news base url
base_url = None

#getting the articles url
articles_url = None

def configure_request(app):
	
	global api_key,base_url,articles_url
	api_key = app.config['NEWS_API_KEY'] 
	base_url = app.config['NEWS_API_SOURCE_URL']
	articles_url = app.config['ARTICLES_BASE_URL']

def get_sources(category):
	'''
	Function that gets the json response to the url request
	'''
	get_sources_url = base_url.format(api_key)

	with urllib.request.urlopen(get_sources_url) as url:
		get_sources_data = url.read()
		get_sources_response = json.loads(get_sources_data)
		print(get_sources_url)

		sources_results = None

		if get_sources_response['sources']:
			sources_results_list = get_sources_response['sources']
			sources_results = process_sources(sources_results_list)

	return sources_results 

def process_sources(sources_list):
	'''
	Function that processes the news sources results and turns them into a list of objects
	Args:
		sources_list: A list of dictionaries that contain sources details
	Returns:
		sources_results: A list of sources objects
	'''

	sources_results = []

	for source_item in sources_list:
		id = source_item['id'] 
		name = source_item['name']
		description = source_item['description']
		url = source_item['url']
		category = source_item['category']
		language = source_item['language']
		country = source_item['country']


		sources_object = Source(id,name,description,url,category,language,country)
		sources_results.append(sources_object)


	return sources_results

def get_articles(id):
	'''
	Function that processes the articles and returns a list of articles objects
	'''
	get_articles_url= 'https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey={}'.format(id,api_key)
		
	with urllib.request.urlopen(get_articles_url) as url:
		articles_details_data = url.read()
		articles_details_response= json.loads(articles_details_data)
		

		articles_results = None

		if articles_details_response:
			author = articles_details_response.get('author')
			description = articles_details_response('description')
			date = articles_details_response('publishedAt')
			url = articles_details_response('urlToImage')
			image = articles_details_response('url')
			title = articles_details_response('title')
			content = articles_details_response('content')
        	
			articles_results = Article(author,description,date,image,url,title,content)


	return articles_results		
		

def process_articles(articles_list):
    '''
    function that processes the json files of articles from the api key
    '''
    articles_results = []
    for article_item in articles_list:
        author = article_item.get('author')
        description = article_item.get('description')
        date = article_item.get('publishedAt')
        url = article_item.get('urlToImage')
        image = article_item.get('url')
        title = article_item.get ('title')
        content= article_item.get('content')
        if url:
            articles_object = Article(author,description,date,image,url,title,content)
            articles_results.append(articles_object)

    return articles_results




        