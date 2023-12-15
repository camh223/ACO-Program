from random import random


def phero_init(d_size):
    """
    Initialises the pheromone matrix with random values.
    :param d_size: The number of cities
    :return: phero_mat - the pheromone matrix
    """
    phero_mat = [[0] * d_size for i in range(d_size)]
    for i in range(d_size):
        for j in range(i+1, d_size):
            phero = random()
            # Edge[i][j] = Edge[j][i] so they must have the same pheromone value.
            phero_mat[i][j] = phero
            phero_mat[j][i] = phero
    return phero_mat


def phero_evaporation(e, d_size, phero_mat):
    """
    A function to evaporate the pheromone according to the evaporation rate.
    :param e: The evaporation rate
    :param d_size: The number of cities
    :param phero_mat: The pheromone matrix
    :return: phero_mat - The updated pheromone matrix
    """
    for i in range(d_size):
        for j in range(d_size):
            phero_mat[i][j] *= (1-e)
    return phero_mat


def phero_update(d, d_size, paths, phero_mat, num_ants, Q, best_fit):
    """
    A function to update the pheromone matrix based on fitness.
    :param d: The distance matrix containing the weight for each edge
    :param d_size: The number of cities
    :param paths: The paths generated by each ant in a single run of the algorithm
    :param phero_mat: The pheromone matrix
    :param num_ants: The number of ants in each run of the algorithm
    :param Q: A fixed parameter that determines the influence of fitness on the pheromone
    :param best_fit: The most optimal solution found so far
    :return:
        phero_mat - The updated pheromone matrix
        best_fit - The updated most optimal solution found so far
    """
    for i in range(num_ants):
        cost = 0
        for j in range(d_size):
            cost += d[paths[i][j]][paths[i][j+1]]
            # Check if most optimal solution has been set. If not, set to cost value.
        if best_fit == -1 or cost < best_fit:
            best_fit = cost
        for j in range(d_size):
            # Edge[i][j] = Edge[j][i] so they must have the same pheromone value.
            phero_mat[paths[i][j]][paths[i][j+1]] += Q/cost
            phero_mat[paths[i][j+1]][paths[i][j]] += Q/cost
    return phero_mat, best_fit
