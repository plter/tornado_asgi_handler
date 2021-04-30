import tornado.ioloop
import tornado.web
import tornado_asgi_handler
import my_asgi


application = tornado.web.Application([
    (r".*", tornado_asgi_handler.AsgiHandler, dict(asgi_app=my_asgi.app))
])
application.listen(8000)

try:
    tornado.ioloop.IOLoop.current().start()
except KeyboardInterrupt as err:
    print("Server stopped")
