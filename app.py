#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options

from pymongo import MongoClient

from settings import settings
from urls import url_patterns

class Application(tornado.web.Application):
    def __init__(self):
        self.database = MongoClient(
            host=settings['database']['host'],
            port=settings['database']['port']
        ).get_database(name=settings['database']['name'])

        session_settings = dict(
            driver="redis",
            driver_settings=dict(
                host='localhost',
                port=6379,
                db=0,
                max_connections=1024,
            )
        )
        settings.update(session=session_settings)

        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
