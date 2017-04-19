import json
import falcon
from abort import *

class QuoteResource:
	def on_get(self, request, response):
		"""Handles GET requests"""
		quote = {
            'quote': 'I\'ve always been more interested in the future than in the past.',
            'author': 'Grace Hopper'
            }

		resp.body = json.dumps(quote)
		return resp

class QuoteResource2:
	def on_get(self, request, response):
		"""Handles GET requests"""
		handle_401(request=request,response=response)
		