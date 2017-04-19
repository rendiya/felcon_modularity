import falcon
import json

api = falcon.API()

import main_route


'''
struktur folder
-app
-run (run app with uwsgi and gevent)
-db
-main_route (for union alls route)
-config (.json and .py)
-module:
  --name_module
  --model module
  --route module
'''