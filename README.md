# Python Examples 
## Traveling Salesman Problems

### ORTools
google_ortools/tube_stations.py - Uses Google's [ortools lib](https://developers.google.com/optimization/routing/tsp) to solve the shortest path between
 London Underground train stations from [Openstreetmap](https://wiki.openstreetmap.org/wiki/List_of_London_Underground_stations).
 The results are plotted onto a map of London using [Plotly](https://plot.ly/python/lines-on-mapbox/#lines-on-mapbox-maps-using-plotly-express).

![Tube Stations](https://github.com/paulmz1/python_examples/blob/master/images/tube_stations.png)

### Dash 
dash/traveling_salesman.py - Using [Dash](https://dash.plot.ly/) for the realtime visualisation of the Traveling Salesman Problem being solved using brute force.

![Dash](https://github.com/paulmz1/python_examples/blob/master/images/dash.png)

### NetworkX Held Karp
tsp/traveling_salesman.py - Visualisation using [Networkx](https://networkx.github.io/) of an asymmetric Traveling Salesman Problem
 solved using the [Held–Karp](https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm) algorithm. See tsp/solvers/tsp_held_karp.py
 
![NetworkX Held Karp](https://github.com/paulmz1/python_examples/blob/master/images/held_karp_networkx.png)


 
Requirements.txt generated with> pipreqs --force


