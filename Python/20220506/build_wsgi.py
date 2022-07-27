# -*- coding: utf-8 -*-


from wsgiref.simple_server import make_server, WSGIServer
import wsgi_app_instance


from flask import Flask, request, make_response
from gevent.pywsgi import WSGIServer

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SECRET_KEY'] = '__dend__'
app.config['UPLOAD_FOLDER'] = 'static'

def main():
    host = '127.0.0.1'
    port = 8888

    app = wsgi_app_instance.AppDemo()

    # server = make_server(host, port, app)
    # msg = "Server Running on http://{host}:{port}/".format(host=host,
    #                                                        port=port)
    # print msg
    # server.serve_forever()


    msg = "Server Running on http://{host}:{port}/".format(host=host,
                                                           port=port)
    print msg
    WSGIServer((host, port), app).serve_forever()



if __name__ == '__main__':

    main()
