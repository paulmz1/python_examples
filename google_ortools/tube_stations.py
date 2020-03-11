# Uses Google's ortools lib to solve and plot the shortest path between London Underground train stations.
# https://developers.google.com/optimization/routing/tsp
# https://wiki.openstreetmap.org/wiki/List_of_London_Underground_stations
# Use Python 3.7.7 64bit if compatibility issues with ortools
import pandas as pd
import plotly.express as px
from geopy.distance import geodesic
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def get_route(manager, routing, solution):
    index = routing.Start(0)
    route = []
    while not routing.IsEnd(index):
        route.append(manager.IndexToNode(index))
        index = solution.Value(routing.NextVar(index))
    return route, solution.ObjectiveValue()


def main():

    stations = pd.read_csv("../data/tube_stations.csv")
    print(stations)

    manager = pywrapcp.RoutingIndexManager(len(stations), 1, 0)
    routing = pywrapcp.RoutingModel(manager)
    cache = {}

    def distance_callback(from_index, to_index):
        dist = cache.get((from_index, to_index), None)
        if dist:
            return dist
        frm = stations.iloc[manager.IndexToNode(from_index)]
        to = stations.iloc[manager.IndexToNode(to_index)]
        dist = geodesic((frm["Latitude"], frm["Longitude"]), (to["Latitude"], to["Longitude"])).meters
        cache[(from_index, to_index)] = dist
        return dist

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        route, distance = get_route(manager, routing, solution)
        print(f'Distance = {distance}')
        routed_stations = stations.iloc[route, :]
        print(routed_stations)
        fig = px.line_mapbox(routed_stations, lat="Latitude", lon="Longitude", text="Name", height=1000)
        fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=10, margin={"r": 0, "t": 0, "l": 0, "b": 0})
        fig.show()


if __name__ == '__main__':
    main()