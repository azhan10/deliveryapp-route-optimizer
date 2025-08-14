# Calculate Distances: Use the Haversine formula to calculate the distance between two geographic points (latitude and longitude). This will help in finding the nearest stop for each leg of the route.

# Estimate Travel Time: Calculate travel time dynamically based on distance, using a lower speed for short distances and a higher speed for longer distances. This ensures more accurate travel time estimates.

# Generate Google Maps Links: Create a Google Maps link that plots the optimized route on a map. Ensure that each stop in the route is unique to avoid duplicate waypoints.

# Optimize Route: Implement a point-to-point optimization by choosing the nearest unvisited location at each step. Organize pickups and drop-offs so that each route segment has a maximum number of stops, making the routes efficient and manageable.

# Load and Process Data: Load the data from a CSV file, preprocess it by setting default values where necessary, and convert it into a format suitable for optimization.

# Save and Export Results: Export each optimized route segment to a CSV file, including total distance, total duration, and a link to the Google Maps route. Return all Google Maps links for easy access.

# Run the Program: Execute the main function to load data, optimize the routes, and generate CSV files and map links for each route.


from math import radians, cos, sin, asin, sqrt
import pandas as pd
import numpy as np
import os, json



"""

Calculates the distance

"""

def haversine(lon1, lat1, lon2, lat2):
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

	# haversine formula 
	dlon = lon2 - lon1 
	dlat = lat2 - lat1 
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a)) 
	r = 6371 
	return c * r




"""

Finds the nearest route

Using the Greedy Nearest neighbour

"""

def optimize_routes(locations, max_stops=5):
    if not locations:
        return []

    unvisited = locations[1:]  # first one is start
    current = locations[0]
    route = [current]
    batches = []
    
    # Find nearest unvisited
    while unvisited:
        nearest = min(unvisited, key=lambda loc: haversine(current["pickup_lat"], current["pickup_lng"], loc["dropoff_lat"], loc["dropoff_lng"]))
        route.append(nearest)
        unvisited.remove(nearest)
        current = nearest

        if len(route) == max_stops or not unvisited:
            batches.append(route)
            if unvisited:
                current = unvisited[0]
                route = [current]
                unvisited.remove(current)

    return batches




"""

Travel time estimation in miles

The speed logic is slower for short hops

The hyperparameters allows users to decide the limits

"""

def estimate_travel_time_miles(distance_miles, short_distance_limit=2, medium_distance_limit=6, short_speed=12, medium_speed=25, long_speed=37):
    if distance_miles < short_distance_limit:  
        speed_mph = short_speed  
    elif distance_miles < medium_distance_limit:
        speed_mph = medium_speed
    else:
        speed_mph = long_speed

    return (distance_miles / speed_mph) * 60  # minutes


"""

Google Maps Link Generator

Accepts a list of pickup/dropoff pairs and returns a Google Maps directions URL.

"""
def generate_maps_link(pairs):
    
    waypoints = []
    for row in pairs:
        pickup = f"{row['pickup_lat']},{row['pickup_lng']}"
        dropoff = f"{row['dropoff_lat']},{row['dropoff_lng']}"
        waypoints.append(pickup)
        waypoints.append(dropoff)
    
    # Remove duplicates while preserving order
    seen = set()
    unique_waypoints = []
    for wp in waypoints:
        if wp not in seen:
            unique_waypoints.append(wp)
            seen.add(wp)

    base_url = "https://www.google.com/maps/dir/"
    return base_url + "/".join(unique_waypoints)



"""

Save Route to CSV

"""
def save_to_csv(batch, batch_num, folder="output"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    total_dist, total_time = 0, 0

    for i in range(len(batch) - 1):
        dist = haversine(batch[i]["pickup_lat"], batch[i]["pickup_lng"], batch[i+1]["dropoff_lat"], batch[i+1]["dropoff_lng"])
        total_dist += dist
        total_time += estimate_travel_time_miles(dist)


    return {
        "batch": batch_num,
        "total_distance_km": round(total_dist, 2),
        "total_duration_min": round(total_time, 2),
        "map_link": generate_maps_link(batch)
    }



"""

Runs the process

"""
def main(file_path, max_stops=5):

	location_df = pd.read_csv(file_path)

	nearest_batch = optimize_routes(json.loads(location_df.to_json(orient='records')), max_stops=max_stops)

	links = []
	for i, batch in enumerate(nearest_batch, 1):
	    result = save_to_csv(batch, i)
	    links.append(result)

	links_df = pd.DataFrame(links)
	links_df.to_csv(os.path.join('output', 'batch-results.csv'), index=False)

	return links
