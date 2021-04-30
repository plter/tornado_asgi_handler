async def app(scope, receive, send):
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/html'],
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': b"Hello World",
    })
