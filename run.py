from app import api

from geventwebsocket.handler import WebSocketHandler

from gevent import monkey, pywsgi  # import the monkey for some patching as well as the WSGI server
monkey.patch_all()  # make sure to do the monkey-patching before loading the falcon package!

port = 8080
server = pywsgi.WSGIServer(("", port), api,handler_class=WebSocketHandler)  # address and port to bind to ("" is localhost), and the Falcon handler API
server.serve_forever()  # once the server is created, let it serve forever