from random import random


def phero_init(d_size):
    phero_map = [[0] * d_size for i in range(d_size)]
    for i in range(d_size):
        for j in range(i+1, d_size):
            phero = random()
            phero_map[i][j] = phero
            phero_map[j][i] = phero
    return phero_map
