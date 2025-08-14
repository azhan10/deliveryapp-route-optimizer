from django.http import JsonResponse
from django.shortcuts import render

import pandas as pd
import numpy as np

import json, os

import optimizer.optimize_routes as optimize_routes

# optimize_route_view:

# Loads a specific CSV file containing route data.
# Calls the optimize_routes function to generate optimized Google Maps links for each route.
# Returns these map links as a JSON response, allowing you to see all routes in Google Maps format via an API endpoint.


# data_source_table_view:

# Loads the same CSV file to display the raw data in a web template.
# If the file is missing, it shows an error message in the template.
# Passes the data to a template as a table, enabling you to view and verify the dataset used for route optimization.

def optimize_route_view(request):

	file_path = os.path.join('data', 'customer-requests-testingLondon36.csv')

	routes = optimize_routes.main(file_path)

	map_links = [x['map_link'] for x in routes]

	return JsonResponse({
		"map_links": map_links
	})


def data_source_table_view(request):

	error = False
	message = "Here is all the data"
	file_path = os.path.join('data', 'customer-requests-testingLondon36.csv')

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

	