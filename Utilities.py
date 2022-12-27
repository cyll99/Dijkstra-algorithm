import sys
import xml.etree.ElementTree as ET
tree = ET.parse('graph.xml')
root = tree.getroot()

"""
This function returns two dictionaries with the labels and ids of each vertex
"""
def dictionnary_label_id():
    id_label = {}   # dictionnary that associates an id to a label
    label_id = {}    # dictionnary that associates a label to an id
    for vertex in root.iter('Vertex'):
        node = vertex.attrib
        id_label[node['vertexId']] = node['label']
        label_id[node['label']] = node['vertexId']
    return id_label, label_id



"""
This function returns the list of all vertices and a dictionary with each vertex as key
"""
def create_graph():
    vertices = [] #list of vertices
    init_graph = {} #initial graph
    for vertex in root.iter('Vertex'):
        node = vertex.attrib
        id = node['vertexId']
        vertices.append(id)
        init_graph[id] = {}

    return vertices, init_graph

"""
This fucntion takes the graph of the previous function as parameter and add all the edges to it
"""
def add_edges_to_graph(init_graph):
    tree = ET.parse('graph.xml')
    root = tree.getroot()
    for vertex in root.iter('Edge'):
        node = vertex.attrib
        head = node['head']
        tail = node['tail']
        weight = node['weight']

        init_graph[head][tail] = float(weight)
    return init_graph


def dijkstra_algorithm(graph, start_node):
    id_label, label_id = dictionnary_label_id()
    start_node = label_id[start_node]
    unvisited_nodes = list(graph.get_nodes())

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
    shortest_path = {}

    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}

    # We'll use max_value to initialize the "infinity" value of the unvisited nodes
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0
    shortest_path[start_node] = 0

    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path

# print the path
def shortes_path_from_a_node_to_another(previous_nodes, start_node, target_node):
    id_label, label_id = dictionnary_label_id()
    id_start_node = label_id[start_node]
    path = []
    node = label_id[target_node]

    while node != id_start_node:
        path.append(id_label[node])
        node = previous_nodes[node]

    # Add the start node manually
    path.append(start_node)

    print(f"The best path from node {start_node} to {target_node} is: .")
    print(" -> ".join(reversed(path)))
