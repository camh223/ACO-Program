from random import random


def update_heuristic(H, ant_pos, d_size):
    """
    A function to update the heuristic matrix based on which nodes have been visited
    :param H: The heuristic matrix
    :param ant_pos: The current ant position
    :param d_size: The number of cites
    :return: H - the heuristic matrix
    """
    H = [[H[i][j] if i != j and j != ant_pos else 0 for j in range(d_size)] for i in range(d_size)]
    return H


def path_probability(H, phero_mat, d_size, alpha, beta, i):
    """
    A function to calculate the probability for each path from the current node.
    :param H: The heuristic matrix
    :param phero_mat: The pheromone matrix
    :param d_size: The number of cities
    :param alpha: A fixed parameter that determines the influence of the pheromone
    :param beta: A fixed parameter that determines the influence of the heuristic matrix
    :param i: The current position
    :return: P - The probability matrix
    """
    sum = 0
    result = [None] * d_size
    P = [None] * d_size
    for j in range(d_size):
        result[j] = phero_mat[i][j] ** alpha * H[i][j] ** beta
        sum += result[j]
    for j in range(d_size):
        P[j] = result[j]/sum
    return P


def choose_path(P, d_size):
    """
    A function to determine which path the ant will traverse.
    :param P: The probability matrix
    :param d_size: The number of cities
    :return: i - The new position of the ant
    """
    rand = random()
    cprob = 0
    for i in range(d_size):
        cprob += P[i]
        if cprob >= rand:
            break
    return i


def ant(H, phero_mat, d_size, alpha, beta):
    """
    A function to find the path of a singular ant in a run.
    :param H: The heuristic matrix
    :param phero_mat: The pheromone matrix
    :param d_size: The number of cities
    :param alpha: A fixed parameter that determines the influence of the pheromone
    :param beta: A fixed parameter that determines the influence of the heuristic matrix
    :return: path - The path that the ant takes
    """
    ant_pos = 0
    path = [0] * (d_size + 1)
    # Start and end point of the path will be the first node
    path[0] = ant_pos
    path[d_size] = ant_pos
    H = update_heuristic(H, ant_pos, d_size)
    for j in range(1, d_size):
        P = path_probability(H, phero_mat, d_size, alpha, beta, ant_pos)
        ant_pos = choose_path(P, d_size)
        H = update_heuristic(H, ant_pos, d_size)
        path[j] = ant_pos
    return path


def ant_movement(H, phero_mat, d_size, alpha, beta, num_ants):
    """
    A function to find the paths the ants take in a run.
    :param H: The heuristic matrix
    :param phero_mat: The pheromone matrix
    :param d_size: The number of cities
    :param alpha: A fixed parameter that determines the influence of the pheromone
    :param beta: A fixed parameter that determines the influence of the heuristic matrix
    :param num_ants: The number of ants in each run of the program
    :return: paths - The paths generated by each ant in a single run of the algorithm
    """
    paths = [ant(H, phero_mat, d_size, alpha, beta) for i in range(num_ants)]
    return paths
