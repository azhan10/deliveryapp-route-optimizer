from django.test import TestCase
import optimizer.optimize_routes as optimize_routes

class OptimizeRoutesTestCase(TestCase):

	# Testing the haversine km between Manchester Arndale to Manchester Science Park
	# Should be ~2.67
	def test_haversine(self):
		arndale_lat, arndale_lon = 53.4848, -2.2399
		msp_lat, msp_lon = 53.4608, -2.2400

		distance = optimize_routes.haversine_distance(arndale_lat, arndale_lon, msp_lat, msp_lon)

		self.assertAlmostEqual(distance, 2.6686864462949633, delta=0.1)

	# Testing time travel in short km
	def test_estimate_travel_time_short(self):
		time = optimize_routes.estimate_travel_time(1, 20)
		expected = (1 / 20) * 60
		self.assertAlmostEqual(time, expected, places=2)

	# Testing time travel in long km
	def test_estimate_travel_time_long(self):
		time = optimize_routes.estimate_travel_time(20, 60)
		expected = (20 / 60) * 60
		self.assertAlmostEqual(time, expected, places=2)


	# Testing time travel in medium km
	def test_estimate_travel_time_medium(self):
		time = optimize_routes.estimate_travel_time(5, 40)
		expected = (5 / 40) * 60
		self.assertAlmostEqual(time, expected, places=2)


	# Testing the optimised solutions here
	def test_optimize_route(self):
		locations = [
	        {
	        	"id":"1",
	            "pickup_lat": 53.4848,
	            "pickup_lng": -2.2399,     # Manchester Arndale
	            "dropoff_lat": 53.4608,
	            "dropoff_lng": -2.2400     # Manchester Science Park
	        },
	        {
	        	"id":"2",
	            "pickup_lat": 53.4725,
	            "pickup_lng": -2.2935,     # Old Trafford
	            "dropoff_lat": 53.4794,
	            "dropoff_lng": -2.2453     # Manchester Central Library
	        },
	        {
	        	"id":"3",
	            "pickup_lat": 53.4608,
	            "pickup_lng": -2.2400,     # Manchester Science Park
	            "dropoff_lat": 53.4848,
	            "dropoff_lng": -2.2399,     # Manchester Arndale
	        }
	    ]
		result = optimize_routes.n_nearest_routes(locations, max_stops=5)
		route_ids = [loc["id"] for batch in result for loc in batch]
		expected_ids = ['1', '3', '2']
		self.assertEqual(route_ids, expected_ids)
