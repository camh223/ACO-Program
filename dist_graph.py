import xml.etree.ElementTree as ET


def read_file(file_name):
    # Read file, store in tree, get root node
    tree = ET.parse('Datasets/' + file_name)
    root = tree.getroot()
    return root


def graph_size(graph):
    vert_size = 0
    for vertex in graph:
        vert_size += 1
    return vert_size


def convert_cost(cost):
    result = float(cost)
    dec = float(format(result, 'f'))
    return dec


def build_graph(file_name):
    root = read_file(file_name)
    # Get graph node
    graph = root[5]
    dist_size = graph_size(graph)
    # Prepare distance array
    dist = [[0] * dist_size for i in range(dist_size)]
    # Initialise vertex number
    vert_no = 0
    for vertex in graph:
        # Initialise edge number
        edge_no = 0
        for edge in vertex:
            if edge_no == vert_no:
                dist[vert_no][edge_no] = 0
                edge_no += 1
            dist[vert_no][edge_no] = convert_cost(edge.attrib['cost'])
            edge_no += 1
        vert_no += 1
    return dist
