import xml.etree.ElementTree as ET


def read_file(file_name):
    """
    A function to read the XML dataset files.
    :param file_name: The name of the file to be read
    :return: root - The root node in the XML file
    """
    # Read file, store in tree, get root node
    tree = ET.parse('Datasets/' + file_name)
    root = tree.getroot()
    return root


def graph_size(graph):
    """
    A function to find the number of vertices (cities) in the graph.
    :param graph: The graph containing the vertices and edges of the TSP.
    :return: vert_size - The number of vertices in the graph
    """
    vert_size = 0
    for vertex in graph:
        vert_size += 1
    return vert_size


def convert_cost(cost):
    """
    A function to convert the cost attribute in the XML file to a float value.
    :param cost: The cost to be converted
    :return: dec - The converted cost value
    """
    result = float(cost)
    dec = float(format(result, 'f'))
    return dec


def build_graph(file_name):
    """
    A function to build the distance graph used in the problem.
    :param file_name: The name of the XML file to read from
    :return:
        dist_size - The number of cities
        dist - The distance graph containing the edge weights
    """
    root = read_file(file_name)
    # Get graph node from tree
    graph = root[5]
    dist_size = graph_size(graph)
    dist = [[0] * dist_size for i in range(dist_size)]
    vert_no = 0
    for vertex in graph:
        edge_no = 0
        for edge in vertex:
            if edge_no == vert_no:
                # Distance from current node is always 0
                dist[vert_no][edge_no] = 0
                edge_no += 1
            dist[vert_no][edge_no] = convert_cost(edge.attrib['cost'])
            edge_no += 1
        vert_no += 1
    return dist_size, dist
