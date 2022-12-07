#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from flask import Flask, request, make_response
from gevent.pywsgi import WSGIServer

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SECRET_KEY'] = '__dend__'
app.config['UPLOAD_FOLDER'] = 'static'


def response(result):
    resp = json.dumps(result, sort_keys=True, indent=2)
    resp = make_response(resp)
    resp.headers['Content-Type'] = 'application/json'
    return resp


@app.route('/')
def index():
    return 'ok'


@app.route('/service/', methods=["GET"])
def service_get():
    params = request.args
    res = dict(aa=params.get("aa"), bb=params.get("bb"))
    return response(res)


@app.route('/service/', methods=["POST"])
def service_post():
    params = dict()
    if request.form:
        params = request.form
        print "form", params
    if request.json:
        params = request.json
        print "json", params

    res = dict(aa=params.get("aa"), bb=params.get("bb"))
    return response(res)


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
