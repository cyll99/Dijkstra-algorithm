import Utilities
from graph import Graph

vertices, init_graph = Utilities.create_graph()

for node in vertices:
    init_graph[node] = {}

init_graph = Utilities.add_edges_to_graph(init_graph)
graph = Graph(vertices, init_graph)

start_node = '9'
target_node = '29'

previous_nodes, shortest_path = Utilities.dijkstra_algorithm(graph=graph, start_node=start_node)
Utilities.shortes_path_from_a_node_to_another(previous_nodes, start_node=start_node, target_node=target_node)
print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
print(f"The minimum cost from {start_node} to each vertex:")
id_label, label_id = Utilities.dictionnary_label_id()

for vertex, weight in shortest_path.items():
    print(f"{start_node} -> {id_label[vertex]}  : {weight}")