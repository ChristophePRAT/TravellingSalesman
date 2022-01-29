import math
import random
from itertools import permutations
from tqdm import tqdm

class Traveller:
    def __init__(self, start_point, points):
        self.path = []
        self.start_point = start_point
        self.current_point = start_point
        self.all_points = points.copy()
        self.remaining_points = points
        self.cumulative_distance = 0

    def travel_to(self, point):
        # Calculate distance between current point and next point
        self.cumulative_distance += point.distance_to(self.current_point)
        # Update path

        self.path.append(point)
        # Update current point
        self.current_point = point
        # Remove point from remaining points
        self.remaining_points.remove(point)

    def add_path(self, path):
        self.path = list(path)
        for point in path:
            self.travel_to(point)

    def reset(self):
        self.remaining_points = self.all_points.copy()

        self.path = []
        self.current_point = self.start_point
        self.cumulative_distance = 0

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, point):
        return math.sqrt((self.x-point.x)**2 + (self.y-point.y)**2)

def generate_data(num_points):
    for i in range(num_points):
        yield Point(random.randint(0, 100), random.randint(0, 100))
origin = Point(50, 50)

def distance_to_origin(point):
    return point.distance_to(origin)
# get closest point
def closest_point(points):
    min_distance = None
    closest_point = None
    for point in points:
        distance = distance_to_origin(point)
        if min_distance is None or distance < min_distance:
            min_distance = distance
            closest_point = point
    return closest_point
def furthest_point(points):
    max_distance = None
    furthest_point = None
    for point in points:
        distance = distance_to_origin(point)
        if max_distance is None or distance > max_distance:
            max_distance = distance
            furthest_point = point
    return furthest_point

number_of_cities = int(input("How many cities do you want to visit? "))
traveller = Traveller(origin, list(generate_data(number_of_cities)))

def brute_force():
    min_distance = None
    way = None
    cities = traveller.remaining_points
    with tqdm(total=math.factorial(number_of_cities)) as pbar:
        for path in permutations(cities):
            traveller.add_path(path)
            distance = traveller.cumulative_distance
            traveller.reset()

            # print(distance)
            if min_distance is None or distance < min_distance:
                min_distance = distance
                way = path
            pbar.update(1)
    print("Minimum distance: ", min_distance)
brute_force()
