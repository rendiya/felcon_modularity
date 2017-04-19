import falcon
import json

api = falcon.API()

import main_route


'''
struktur folder
-app
-run (run app with uwsgi and gevent)
-db
-abort
-main_route (for union alls route)
-config (.json and .py)
-module:
  --name_module
  --model module
  --route module

joss semua tinggal panggil bero
jangan taruh apa pun di route atau apalah....
modular falconery
'''