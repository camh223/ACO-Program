from random import random


def phero_init(d_size):
    phero_mat = [[0] * d_size for i in range(d_size)]
    for i in range(d_size):
        for j in range(i+1, d_size):
            phero = random()
            phero_mat[i][j] = phero
            phero_mat[j][i] = phero
    return phero_mat


def phero_evaporation(e, d_size, phero_mat):
    for i in range(d_size):
        for j in range(d_size):
            phero_mat[i][j] *= (1-e)
    return phero_mat


def phero_update(d, d_size, paths, phero_mat, num_ants, Q, best_fit):
    for i in range(num_ants):
        cost = 0
        for j in range(d_size):
            cost += d[paths[i][j]][paths[i][j+1]]
        if best_fit == -1 or cost < best_fit:
            best_fit = cost
        for j in range(d_size):
            phero_mat[paths[i][j]][paths[i][j+1]] += Q/cost
            phero_mat[paths[i][j+1]][paths[i][j]] += Q/cost
    return phero_mat, best_fit
