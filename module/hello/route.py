from app import api
from .quote import *

api.add_route('/falcon', QuoteResource())
api.add_route('/falcon2', QuoteResource2())

print "a"