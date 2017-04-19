import json


def get_config():
	filename = 'config.json'
	with open(filename,'r') as data_file:
		data_json = json.loads(data_file.read())
	return data_json

print get_config()