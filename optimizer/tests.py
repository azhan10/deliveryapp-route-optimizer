from django.test import TestCase
import optimizer.optimize_routes as optimize_routes

class UtilsTestCase(TestCase):

	# """
	
	# Testing the haversine miles between Manchester Arndale to Manchester Science Park

	# Should be ~1.66 miles by road, ~1.55 miles straight-line

	# """
	# def test_haversine_miles(self):
	# 	arndale_lat, arndale_lon = 53.4848, -2.2399
	# 	msp_lat, msp_lon = 53.4608, -2.2400

	# 	distance = optimize_routes.haversine_miles(arndale_lat, arndale_lon, msp_lat, msp_lon)

	# 	self.assertAlmostEqual(distance, 1.55, delta=0.1)

	# """
		
	# Testing time travel in miles short miles
	
	# """
	# def test_estimate_travel_time_miles_short(self):
	# 	time = optimize_routes.estimate_travel_time_miles(1)
	# 	expected = (1 / 12.5) * 60
	# 	self.assertAlmostEqual(time, expected, places=2)


	"""
		
	Testing time travel in miles medium miles

	pass
	
	"""
	def test_estimate_travel_time_miles_medium(self):
		time = optimize_routes.estimate_travel_time_miles(5)
		expected = (5 / 25) * 60
		self.assertAlmostEqual(time, expected, places=2)

	# """
		
	# Testing time travel in miles long miles
	
	# """
	# def test_estimate_travel_time_miles_long(self):
	# 	time = optimize_routes.estimate_travel_time_miles(20)
	# 	expected = (20 / 37.5) * 60
	# 	self.assertAlmostEqual(time, expected, places=2)

	# """
		
	# Testing the optimised solutions here
	
	# """
	# def test_optimize_route(self):
	# 	locations = [
	# 		{"id": "1", "address": "A", "lat": 0.0, "lon": 0.0},
	# 		{"id": "2", "address": "B", "lat": 0.0, "lon": 1.0},
	# 		{"id": "3", "address": "C", "lat": 1.0, "lon": 1.0},
	# 		{"id": "4", "address": "D", "lat": 1.0, "lon": 0.0}
	# 	]
	# 	result = optimize_routes.optimize_routes(locations, max_stops=5)
	# 	route_ids = [loc["id"] for batch in result for loc in batch]
	# 	expected_ids = ['1', '2', '3', '4']
	# 	self.assertEqual(route_ids, expected_ids)
