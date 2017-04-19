import json
import falcon


class QuoteResource:
	def on_get(self, req, resp):
		"""Handles GET requests"""
		quote = {
            'quote': 'I\'ve always been more interested in the future than in the past.',
            'author': 'Grace Hopper'
            }

		resp.body = json.dumps(quote)
		return resp

class QuoteResource2:
	def on_get(self, req, resp):
		"""Handles GET requests"""
		quote = {
            'quote': 'lalala',
            'author': 'Grace Hopper'
            }

		resp.body = json.dumps(quote)
		return resp
		