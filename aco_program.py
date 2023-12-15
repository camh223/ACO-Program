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
    d_size, d = dist_graph.build_graph('burma14.xml')
    phero_mat = pheromone.phero_init(d_size)
    H = init_heuristic(d_size, d)
    ant_movement.ant_movement(H, phero_mat, d_size, alpha, beta, num_ants)

