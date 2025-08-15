from django.http import JsonResponse
from django.shortcuts import render

import pandas as pd

import json, os

import optimizer.optimize_routes as optimize_routes


# Make the filename universal
def get_filename():
	return "customer-trial-1"



# optimize_route_view:

# Loads a specific CSV file containing route data.
# Calls the optimize_routes function to generate optimized Google Maps links for each route.
# Returns these map links as a JSON response, allowing you to see all routes in Google Maps format via an API endpoint.

# Hyperparamters (GET request):
# 	- speed kmh - speed number in kilometres
# 	- max_stops - the number of max stops

def optimize_route_view(request):

	file_path = os.path.join('data', (get_filename() + '.csv'))

	if os.path.isfile(file_path) == False:
		return JsonResponse({
	        'status_code': 404,
	        'error': 'The file was not found'
	    })

	preprocessing = optimize_routes.preprocessing(file_path)

	if preprocessing['error'] == True:
		return JsonResponse({
	        'status_code': 400,
	        'error': preprocessing['message']
	    })

	try:
		speed_kmh = int(request.GET['speed_kmh'])
	except:
		speed_kmh = 30

	try:
		max_stops = int(request.GET['max_stops'])
	except:
		max_stops = 5

	routes = optimize_routes.optimize_routes(file_path, speed_kmh=speed_kmh, max_stops=max_stops)
	map_links = []

	if len(routes) > 0:
		map_links = [x['map_link'] for x in routes]

	return JsonResponse({
		"map_links": map_links
	})



# data_source_table_view:

# Loads the same CSV file to display the raw data in a web template.
# If the file is missing, it shows an error message in the template.
# Passes the data to a template as a table, enabling you to view and verify the dataset used for route optimization.

def data_source_table_view(request):

	file_path = os.path.join('data', (get_filename() + '.csv'))

	preprocessing = optimize_routes.preprocessing(file_path)

	error = False
	message = "Here is the data"
	file_path_json = []

	if os.path.isfile(file_path) == False:
		message = "The file was not found"
		error = True
	
	elif preprocessing['error'] == True:
		message = preprocessing['message']
		error = True

	else:
		file_path_df = pd.read_csv(file_path)
		file_path_json = json.loads(file_path_df.to_json(orient='records'))

	context = {
		"data": file_path_json,
		"message": message,
		"error":error
	}
	
	return render(request, 'optimizer/data_source.html', context)

	