def app(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']

    if method == 'POST' and path == '/login':
        try:
            size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            size = 0
        body = environ['wsgi.input'].read(size).decode()
        params = dict(p.split('=') for p in body.split('&'))

        username = params.get('username', '')
        password = params.get('password', '')

        if username == 'admin' and password == 'admin123':
            response = f"Welcome, {username}!"
        else:
            response = "Invalid credentials"

        start_response('200 OK', [('Content-Type', 'text/plain')])
        return [response.encode()]

    # fallback
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello from WSGI app!']
