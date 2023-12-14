import dist_graph, pheromone


def gen_heuristic(d_size, d):
    # Initialise heuristic matrix with zeroes.
    H = [[0 for i in range(d_size)] for j in range(d_size)]
    for i in range(d_size):
        for j in range(d_size):
            if i != j:
                H[i][j] = 1/d[i][j]
    return H


if __name__ == '__main__':
    d_size, d = dist_graph.build_graph('burma14.xml')
    phero_map = pheromone.phero_init(d_size)
    H = gen_heuristic(d_size, d)
    print(H)
