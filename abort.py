import falcon
import json

def handle_400(request, response):
	error = {'meta':{ 'error_message' : 'Bad Request','code':400 }}
	response.status = falcon.HTTP_400
	response.body = json.dumps(error)

def handle_401(request,response):
	error = {'meta':{ 'error_message' : 'User Unauthorized','code':401 }}
	request.status = falcon.HTTP_401
	response.body = json.dumps(error)

def handle_403(request,response):
	error = {'meta':{ 'error_message' : 'Forbidden Access','code':403 }}
	request.status = falcon.HTTP_403
	response.body = json.dumps(error)

def handle_404(request,response):
	error = {'meta':{ 'error_message' : 'Page Not Found','code':404 }}
	request.status = falcon.HTTP_404
	response.body = json.dumps(error)

def handle_405(request,response):
	error = {'meta':{ 'error_message' : 'Methods Not Allowed','code':405 }}
	request.status = falcon.HTTP_405
	response.body = json.dumps(error)

def handle_500(request,response):
	error = {'meta':{ 'error_message' : 'Bad Request','code':500 }}
	request.status = falcon.HTTP_500
	response.body = json.dumps(error)
