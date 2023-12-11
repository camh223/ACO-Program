import xml.etree.ElementTree as ET


def read_file(file_name):
    # Read file, store in tree, get root node
    tree = ET.parse('Datasets/'+file_name)
    root = tree.getroot()
    print(root[0].text)
    return root

def build_graph(file_name):
    root = read_file(file_name)
    # Get graph node
    graph = root[5]
    # Prepare distance array
    dist = []
    # Initialise vertex number
    vert_no = 0
    for vertex in graph:
        # Initialise edge number
        edge_no = 0
        for edge in vertex:
            if edge_no == vert_no:
                dist[vert_no][edge_no] = 0
            else:
                dist[vert_no][edge_no] =





