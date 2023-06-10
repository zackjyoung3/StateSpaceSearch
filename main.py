from city_problem.constant_cities_graph import GRAPH
from city_problem.city_graph import CityGraph
from state_space_base.search import UCS, GBFS, AStar

city_graph = CityGraph(GRAPH, 'Las Vegas', 'New York City')
ucs = UCS(city_graph)
gbfs = GBFS(city_graph)
a_star = AStar(city_graph)
ucs_soln = ucs.search()
print(ucs_soln)
gbfs_soln = gbfs.search(city_graph)
print(gbfs_soln)
a_star_soln = a_star.search()
print(a_star_soln)
