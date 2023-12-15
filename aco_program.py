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
    max_runs = 10000
    runs = 0
    best_fit = -1
    d_size, d = dist_graph.build_graph('burma14.xml')
    phero_mat = pheromone.phero_init(d_size)
    H = init_heuristic(d_size, d)
    while runs < max_runs:
        paths = ant_movement.ant_movement(H, phero_mat, d_size, alpha, beta, num_ants)
        phero_mat, best_fit = pheromone.phero_update(d, d_size, paths, phero_mat, num_ants, Q, best_fit)
        phero_mat = pheromone.phero_evaporation(e, d_size, phero_mat)
        # num_ants fitness evaluations occur per run
        runs += num_ants
    print(best_fit)
