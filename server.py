import tornado.ioloop
import tornado.web

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": "static", "default_filename": "index.html"})
    ])
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()

