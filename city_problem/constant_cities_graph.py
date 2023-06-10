import math
import random


def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


GRAPH = {}
random.seed(96)

cities = [
    ("New York City", 0, 0),
    ("Los Angeles", 3000, 0),
    ("Chicago", 800, 700),
    ("Houston", 1400, -300),
    ("Phoenix", 3200, -200),
    ("Philadelphia", 100, 200),
    ("San Antonio", 1300, -400),
    ("San Diego", 2900, 200),
    ("Dallas", 1200, -100),
    ("San Jose", 3200, 400),
    ("Austin", 1200, -300),
    ("Jacksonville", 200, -500),
    ("Fort Worth", 1300, -100),
    ("Columbus", 300, 800),
    ("San Francisco", 3000, 400),
    ("Indianapolis", 500, 600),
    ("Charlotte", 400, -600),
    ("Seattle", 4000, 800),
    ("Denver", 1800, 500),
    ("Washington, D.C.", 200, 400),
    ("Boston", 100, 800),
    ("El Paso", 2400, -500),
    ("Nashville", 800, 400),
    ("Detroit", 300, 700),
    ("Oklahoma City", 1000, -300),
    ("Portland", 4000, 1000),
    ("Las Vegas", 3100, -100),
    ("Memphis", 800, 200),
    ("Louisville", 600, 500),
    ("Baltimore", 200, 300)
]

# Create GRAPH edges with costs greater than Euclidean distance
for i in range(len(cities)):
    current_city = cities[i]
    current_name, current_x, current_y = current_city
    GRAPH[current_city] = []

    for j in range(len(cities)):
        if i != j:
            neighbor_city = cities[j]
            neighbor_name, neighbor_x, neighbor_y = neighbor_city

            distance = euclidean_distance(current_x, current_y, neighbor_x, neighbor_y)
            # Add rand num in [1,10000] to make the cost greater than the distance
            cost = distance + random.randint(1, 10000)

            GRAPH[current_city].append((neighbor_city, cost))


def print_graph(graph):
    for city, neighbors in graph.items():
        city_name, city_x, city_y = city
        print(f"{city_name} ({city_x}, {city_y}):")
        for neighbor, cost in neighbors:
            neighbor_name, neighbor_x, neighbor_y = neighbor
            print(f"  -> {neighbor_name} ({neighbor_x}, {neighbor_y}) (Cost: {cost})")
        print()
