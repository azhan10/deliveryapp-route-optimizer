from django.test import TestCase
import optimizer.optimize_routes as optimize_routes

class OptimizeRoutesTestCase(TestCase):

	# Testing the time summation of a batch of routes
	def test_time_route_sum(self):

		routes = [
			{
				'pickup_company_name': 'Hilfiger Stores Ltd',
				'pickup_address_line_1': '100 Liverpool St',
				'pickup_city': 'London',
				'pickup_postcode': 'EC2M 2AU',
				'pickup_email': 'billy@deliveryapp.com',
				'pickup_lat': 51.5181999, 
				'pickup_lng': -0.083709061, 
				'pickup_time_from': '08:30:00',
				'pickup_time_to': '11:00:00',
				'dropoff_company_name': 'Fast Couriers',
				'dropoff_address_line_1': 'gate 4 - MOL',
				'dropoff_city': 'London',
				'dropoff_postcode': 'EC1A2FD',
				'dropoff_email': 'billy@deliveryapp.com',
				'dropoff_lat': 51.5171675, 
				'dropoff_lng': -0.1043089, 
				'dropoff_time_from': '12:30:00',
				'dropoff_time_to': '20:30:00'
			},
			{
				'pickup_company_name': 'Hilfiger Stores Ltd',
				'pickup_address_line_1': '111 Liverpool St',
				'pickup_city': 'London',
				'pickup_postcode': 'EC2M 2AU',
				'pickup_email': 'billy@deliveryapp.com',
				'pickup_lat': 51.5181999, 
				'pickup_lng': -0.083709061, 
				'pickup_time_from': '08:30:00',
				'pickup_time_to': '11:00:00',
				'dropoff_company_name': 'Fast Couriers',
				'dropoff_address_line_1': '20 ROPE MAKER - LINKLATERS',
				'dropoff_city': 'London',
				'dropoff_postcode': 'EC2Y9LY',
				'dropoff_email': 'billy@deliveryapp.com',
				'dropoff_lat': 51.5199204, 
				'dropoff_lng': -0.0889247, 
				'dropoff_time_from': '10:00:00',
				'dropoff_time_to': '20:30:00'
			},
			{
				'pickup_company_name': 'Hilfiger Stores Ltd',
				'pickup_address_line_1': '108 Liverpool St',
				'pickup_city': 'London',
				'pickup_postcode': 'EC2M 2AU',
				'pickup_email': 'billy@deliveryapp.com',
				'pickup_lat': 51.5181999, 
				'pickup_lng': -0.083709061, 
				'pickup_time_from': '08:30:00',
				'pickup_time_to': '11:00:00',
				'dropoff_company_name': 'Fast Couriers',
				'dropoff_address_line_1': 'DACC Europe/StructureTone',
				'dropoff_city': 'London',
				'dropoff_postcode': 'EC24UJ',
				'dropoff_email': 'billy@deliveryapp.com',
				'dropoff_lat': 51.5161213, 
				'dropoff_lng': -0.0787609, 
				'dropoff_time_from': '12:30:00',
				'dropoff_time_to': '20:30:00'
			},
			{
				'pickup_company_name': 'Hilfiger Stores Ltd',
				'pickup_address_line_1': '113 Liverpool St',
				'pickup_city': 'London',
				'pickup_postcode': 'EC2M 2AU',
				'pickup_email': 'billy@deliveryapp.com',
				'pickup_lat': 51.5181999, 
				'pickup_lng': -0.083709061, 
				'pickup_time_from': '08:30:00',
				'pickup_time_to': '11:00:00',
				'dropoff_company_name': 'Fast Couriers',
				'dropoff_address_line_1': '6 BEVIS MARKS',
				'dropoff_city': 'London',
				'dropoff_postcode': 'EC3A7BA',
				'dropoff_email': 'billy@deliveryapp.com',
				'dropoff_lat': 51.5151206, 
				'dropoff_lng': -0.0795008, 
				'dropoff_time_from': '10:00:00',
				'dropoff_time_to': '20:30:00'
			},
			{
				'pickup_company_name': 'Hilfiger Stores Ltd',
				'pickup_address_line_1': '109 Liverpool St',
				'pickup_city': 'London',
				'pickup_postcode': 'EC2M 2AU',
				'pickup_email': 'billy@deliveryapp.com',
				'pickup_lat': 51.5181999, 'pickup_lng': -0.083709061, 'pickup_time_from': '08:30:00',
				'pickup_time_to': '11:00:00','dropoff_company_name': 'Fast Couriers',
				'dropoff_address_line_1': 'RaporMarketing',
				'dropoff_city': 'London',
				'dropoff_postcode': 'EC2A4HJ',
				'dropoff_email': 'billy@deliveryapp.com',
				'dropoff_lat': 51.523712, 'dropoff_lng': -0.0835602, 'dropoff_time_from': '12:30:00',
				'dropoff_time_to': '20:30:00'
			}
		]

		total_time = 0
		speed_kmh = 30

		for i in range(len(routes)):
			dist = optimize_routes.haversine_distance(routes[i]["pickup_lat"], routes[i]["pickup_lng"], routes[i]["dropoff_lat"], routes[i]["dropoff_lng"])
			total_time += optimize_routes.estimate_travel_time(dist, speed_kmh=speed_kmh)

		total_time = round(total_time, 2)
		expected_time = 6.63
		self.assertEqual(total_time, expected_time)


	# Testing the distance summation of a batch of routes
	def test_distance_route_sum(self):

		routes = [
			{
				'pickup_company_name': 'Hilfiger Stores Ltd',
				'pickup_address_line_1': '100 Liverpool St',
				'pickup_city': 'London',
				'pickup_postcode': 'EC2M 2AU',
				'pickup_email': 'billy@deliveryapp.com',
				'pickup_lat': 51.5181999, 
				'pickup_lng': -0.083709061, 
				'pickup_time_from': '08:30:00',
				'pickup_time_to': '11:00:00',
				'dropoff_company_name': 'Fast Couriers',
				'dropoff_address_line_1': 'gate 4 - MOL',
				'dropoff_city': 'London',
				'dropoff_postcode': 'EC1A2FD',
				'dropoff_email': 'billy@deliveryapp.com',
				'dropoff_lat': 51.5171675, 
				'dropoff_lng': -0.1043089, 
				'dropoff_time_from': '12:30:00',
				'dropoff_time_to': '20:30:00'
			},
			{
				'pickup_company_name': 'Hilfiger Stores Ltd',
				'pickup_address_line_1': '111 Liverpool St',
				'pickup_city': 'London',
				'pickup_postcode': 'EC2M 2AU',
				'pickup_email': 'billy@deliveryapp.com',
				'pickup_lat': 51.5181999, 
				'pickup_lng': -0.083709061, 
				'pickup_time_from': '08:30:00',
				'pickup_time_to': '11:00:00',
				'dropoff_company_name': 'Fast Couriers',
				'dropoff_address_line_1': '20 ROPE MAKER - LINKLATERS',
				'dropoff_city': 'London',
				'dropoff_postcode': 'EC2Y9LY',
				'dropoff_email': 'billy@deliveryapp.com',
				'dropoff_lat': 51.5199204, 
				'dropoff_lng': -0.0889247, 
				'dropoff_time_from': '10:00:00',
				'dropoff_time_to': '20:30:00'
			},
			{
				'pickup_company_name': 'Hilfiger Stores Ltd',
				'pickup_address_line_1': '108 Liverpool St',
				'pickup_city': 'London',
				'pickup_postcode': 'EC2M 2AU',
				'pickup_email': 'billy@deliveryapp.com',
				'pickup_lat': 51.5181999, 
				'pickup_lng': -0.083709061, 
				'pickup_time_from': '08:30:00',
				'pickup_time_to': '11:00:00',
				'dropoff_company_name': 'Fast Couriers',
				'dropoff_address_line_1': 'DACC Europe/StructureTone',
				'dropoff_city': 'London',
				'dropoff_postcode': 'EC24UJ',
				'dropoff_email': 'billy@deliveryapp.com',
				'dropoff_lat': 51.5161213, 
				'dropoff_lng': -0.0787609, 
				'dropoff_time_from': '12:30:00',
				'dropoff_time_to': '20:30:00'
			},
			{
				'pickup_company_name': 'Hilfiger Stores Ltd',
				'pickup_address_line_1': '113 Liverpool St',
				'pickup_city': 'London',
				'pickup_postcode': 'EC2M 2AU',
				'pickup_email': 'billy@deliveryapp.com',
				'pickup_lat': 51.5181999, 
				'pickup_lng': -0.083709061, 
				'pickup_time_from': '08:30:00',
				'pickup_time_to': '11:00:00',
				'dropoff_company_name': 'Fast Couriers',
				'dropoff_address_line_1': '6 BEVIS MARKS',
				'dropoff_city': 'London',
				'dropoff_postcode': 'EC3A7BA',
				'dropoff_email': 'billy@deliveryapp.com',
				'dropoff_lat': 51.5151206, 
				'dropoff_lng': -0.0795008, 
				'dropoff_time_from': '10:00:00',
				'dropoff_time_to': '20:30:00'
			},
			{
				'pickup_company_name': 'Hilfiger Stores Ltd',
				'pickup_address_line_1': '109 Liverpool St',
				'pickup_city': 'London',
				'pickup_postcode': 'EC2M 2AU',
				'pickup_email': 'billy@deliveryapp.com',
				'pickup_lat': 51.5181999, 'pickup_lng': -0.083709061, 'pickup_time_from': '08:30:00',
				'pickup_time_to': '11:00:00','dropoff_company_name': 'Fast Couriers',
				'dropoff_address_line_1': 'RaporMarketing',
				'dropoff_city': 'London',
				'dropoff_postcode': 'EC2A4HJ',
				'dropoff_email': 'billy@deliveryapp.com',
				'dropoff_lat': 51.523712, 'dropoff_lng': -0.0835602, 'dropoff_time_from': '12:30:00',
				'dropoff_time_to': '20:30:00'
			}
		]

		total_dist = 0

		for i in range(len(routes)):
			dist = optimize_routes.haversine_distance(routes[i]["pickup_lat"], routes[i]["pickup_lng"], routes[i]["dropoff_lat"], routes[i]["dropoff_lng"])
			total_dist += dist

		total_dist = round(total_dist, 2)
		expected_distance = 3.31
		self.assertEqual(total_dist, expected_distance)


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
