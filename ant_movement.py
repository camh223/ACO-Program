from random import random


def update_heuristic(H, ant_pos, d_size):
    H = [[H[i][j] if i != j and j != ant_pos else 0 for j in range(d_size)] for i in range(d_size)]
    return H


def path_probability(H, phero_mat, d_size, alpha, beta, i):
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
    rand = random()
    cprob = 0
    for i in range(d_size):
        cprob += P[i]
        if cprob >= rand:
            break
    return i


def ant(H, phero_mat, d_size, alpha, beta):
    ant_pos = 0
    H = update_heuristic(H, ant_pos, d_size)
    for j in range(d_size - 1):
        P = path_probability(H, phero_mat, d_size, alpha, beta, ant_pos)
        ant_pos = choose_path(P, d_size)
        H = update_heuristic(H, ant_pos, d_size)
        print(ant_pos)
        # print('\n'.join([''.join(['{:10}'.format(round(item, 4)) for item in row]) for row in H]))


def ant_movement(H, phero_mat, d_size, alpha, beta, num_ants):
    for i in range(num_ants):
        ant(H, phero_mat, d_size, alpha, beta)
    return None
