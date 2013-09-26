from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.web import StaticFileHandler

from handlers.index import IndexHandler
from handlers.blog import BlogHandler
from handlers.login import LoginHandler
from handlers.logoff import LogoffHandler
from handlers.article import ArticleHandler
from handlers.category import CategoryHandler
from handlers.edit import EditHandler
from handlers.register import RegisterHandler

from handlers.ajax.getarticle import AjaxGetArticleHandler
from handlers.ajax.addarticle import AjaxAddArticleHandler
from handlers.ajax.updatearticle import AjaxUpdateArticleHandler

import os, pymongo

settings = {
    'static_path': os.path.join(os.path.dirname(__file__), "static"),
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    'login_url': '/login',
    'database': pymongo.MongoClient('mongodb://localhost:27017').ytblog,
    'cookie_secret': '81c970b4e3ec500e0807073db064f15a45d3c3c4',
}


if __name__ == "__main__":
    application = Application([
            (r"/", IndexHandler),
            (r"/blog", BlogHandler),
            (r"/blog/article/(?P<article_id>.*)", ArticleHandler),
            (r"/blog/edit/?(?P<article_id>.*)", EditHandler),
            (r"/blog/category/(?P<tag_id>.*)", CategoryHandler),
            (r"/user/login", LoginHandler),
            (r"/user/logoff", LogoffHandler),
            (r"/user/register", RegisterHandler),
            (r"/media/(.*)", StaticFileHandler, {"path": "media"}),

            ## AJAX
            (r"/blog/ajax/article/add", AjaxAddArticleHandler),
            (r"/blog/ajax/article/get/(?P<article_id>.*)", AjaxGetArticleHandler),
            (r"/blog/ajax/article/update/(?P<article_id>.*)", AjaxUpdateArticleHandler),
            
        ], **settings)
    application.listen(9030)

    IOLoop.instance().start()
