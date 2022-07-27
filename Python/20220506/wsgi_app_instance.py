# -*- coding: utf-8 -*-


class AppDemo(object):

    def __init__(self):
        pass

    def wsgi_app(self, environ, start_response):
        status = "200 OK"
        response_headers = [('Content-Type', 'text/html')]
        start_response(status, response_headers)
        path = environ['PATH_INFO'][1:] or 'hello'
        return [b'<h1> %s </h1>' % path.encode()]

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


if __name__ == '__main__':
    app = AppDemo()