# tornado_asgi_handler
A request handler runs in tornado to support asgi


# Example hello_world

```python
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
```

**Run hello_world example**   
```shell
PYTHONPATH=. python examples/hello_world
```

# Checkout all exmaples here 
[examples](examples)

