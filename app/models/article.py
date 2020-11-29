class Article:
    '''
    Class that instantiates objects of the news article objects 
    '''
    def __init__(self,author,title, description,url,time,image):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.time = time
        self.image = image
        