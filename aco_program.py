import dist_graph, pheromone, ant_movement


def init_heuristic(d_size, d):
    """
    A function to initialise the heuristic matrix based on 1/d[i][j]
    :param d_size: The number of cities
    :param d: The distance matrix containing the weight for each edge
    :return: H - The heuristic matrix
    """
    # Initialise heuristic matrix with zeroes.
    H = [[0 for i in range(d_size)] for j in range(d_size)]
    for i in range(d_size):
        for j in range(d_size):
            # Probability of travelling to current node is always 0
            if i != j:
                H[i][j] = 1/d[i][j]
    return H


def run_aco(num_ants, alpha, beta, e, Q, max_runs, file_name):
    """
    A function to start running the ant colony optimisation functionality.
    :param num_ants: The number of ants in each run of the program
    :param alpha: A fixed parameter that determines the influence of the pheromone
    :param beta: A fixed parameter that determines the influence of the heuristic matrix
    :param e: The rate of evaporation
    :param Q: A fixed parameter that determines the influence of fitness on the pheromone
    :param max_runs: The number of times the algorithm will run
    :param file_name: The name of the file containing the dataset to perform ACO on
    :return: best_fit - the most optimal solution cost
    """
    runs = 0
    best_fit = -1
    d_size, d = dist_graph.build_graph(file_name)
    phero_mat = pheromone.phero_init(d_size)
    H = init_heuristic(d_size, d)
    while runs < max_runs:
        paths = ant_movement.ant_movement(H, phero_mat, d_size, alpha, beta, num_ants)
        phero_mat, best_fit = pheromone.phero_update(d, d_size, paths, phero_mat, num_ants, Q, best_fit)
        phero_mat = pheromone.phero_evaporation(e, d_size, phero_mat)
        # num_ants fitness evaluations occur per run
        runs += num_ants
    return best_fit


if __name__ == '__main__':
    num_ants = 5
    alpha = 1
    beta = 2
    e = 0.5
    Q = 1
    max_runs = 10000
    # Change with 'brazil58.xml' for brazil dataset
    file_name = 'burma14.xml'
    best_fit = run_aco(num_ants, alpha, beta, e, Q, max_runs, file_name)
    print(best_fit)
