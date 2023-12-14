from random import random


def update_heuristic(H, ant_pos, d_size):
    H = [[H[i][j] if i != j and j != 0 else 0 for j in range(d_size)] for i in range(d_size)]
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


def ant_movement(H, phero_mat, d_size, alpha, beta):
    # Initialise answer array
    ant_pos = 0
    i = 0
    sum = 0
    P = path_probability(H, phero_mat, d_size, alpha, beta, i)
    path = choose_path(P, d_size)
    print(path)

    return None
