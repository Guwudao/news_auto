from .web.sohu import Sohu


def initial_news_list_crawl():
    web_list = [Sohu()]
    for web in web_list:
        return web.run()
