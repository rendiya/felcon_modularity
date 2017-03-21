from app import api
from module.quote import QuoteResource

api.add_route('/quote', QuoteResource())