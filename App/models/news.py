class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,name, description, url, category, language, country):
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class Articles:
    '''
    Articles class to define Articles Objects
    '''

    def __init__(self,author, title, description, url, urlToManage, publishedAt, content):

        self.author = author
        self.title = title
        self.descriptionAt = publishedAt
        self.c0ontent = content