class Source:
    '''
    Source class to define source objects
    '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class Article:
    '''
    Class that instantiates objects of the news article objects of the news sources
    '''
    def __init__(self,author,title, description,url,time,image):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.time = time
        self.image = image

