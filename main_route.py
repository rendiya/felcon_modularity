
'''for all route in module import here
'''

from module.hello import route
from app import api
from abort import *

api.add_sink(handle_404, '')