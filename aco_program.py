import dist_graph, pheromone

if __name__ == '__main__':
    num_ants = 5
    d_size, d = dist_graph.build_graph('burma14.xml')
    phero_map = pheromone.phero_init(d_size)
    print(phero_map)