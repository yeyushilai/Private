#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SECRET_KEY'] = '__dend__'
app.config['UPLOAD_FOLDER'] = 'static'


@app.route('/')
def index():
    return 'ok'


def main():
    host = '127.0.0.1'
    port = 8888
    addr = (host, port)

    msg = "Server Running on http://{host}:{port}/".format(host=host,
                                                           port=port)
    print msg
    WSGIServer(addr, app).serve_forever()


if __name__ == '__main__':
    main()
