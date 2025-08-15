from django.http import JsonResponse
from django.shortcuts import render

import pandas as pd
import numpy as np

import json, os

import optimizer.optimize_routes as optimize_routes


# Make the filename universal
def get_filename():
	return "customer-trial-1"



# optimize_route_view:

# Loads a specific CSV file containing route data.
# Calls the optimize_routes function to generate optimized Google Maps links for each route.
# Returns these map links as a JSON response, allowing you to see all routes in Google Maps format via an API endpoint.

# Hyperparamters:
# 	- speed kmh - speed number in kilometres
# 	- max_stops - the number of max stops

def optimize_route_view(request):

	file_path = os.path.join('data', (get_filename() + '.csv'))

	try:
		speed_kmh = int(request.GET['speed_kmh'])
	except:
		speed_kmh = 30

	try:
		max_stops = int(request.GET['max_stops'])
	except:
		max_stops = 5

	routes = optimize_routes.optimize_routes(file_path, speed_kmh=speed_kmh, max_stops=max_stops)

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

	error = False
	message = "Here is all the data"

	if os.path.isfile(file_path) == False:
		message = "The file is missing"
		error = True

	try:
		file_path_df = pd.read_csv(file_path)
		file_path_json = json.loads(file_path_df.to_json(orient='records'))
	except:
		message = "There was an error with the data."
		error = True
		file_path_json = []

	context = {
		"data": file_path_json,
		"message": message,
		"error":error
	}
	
	return render(request, 'optimizer/data_source.html', context)

	