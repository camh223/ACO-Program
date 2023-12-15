import dist_graph, pheromone, ant_movement


def init_heuristic(d_size, d):
    # Initialise heuristic matrix with zeroes.
    H = [[0 for i in range(d_size)] for j in range(d_size)]
    for i in range(d_size):
        for j in range(d_size):
            if i != j:
                H[i][j] = 1/d[i][j]
    return H


if __name__ == '__main__':
    num_ants = 5
    alpha = 1
    beta = 2
    e = 0.5
    Q = 1
    d_size, d = dist_graph.build_graph('burma14.xml')
    phero_mat = pheromone.phero_init(d_size)
    print(phero_mat)
    H = init_heuristic(d_size, d)
    paths = ant_movement.ant_movement(H, phero_mat, d_size, alpha, beta, num_ants)
    phero_mat = pheromone.phero_update(d, d_size, paths, phero_mat, num_ants, Q)
    print(phero_mat)
    phero_mat = pheromone.phero_evaporation(e, d_size, phero_mat)
    print(phero_mat)
