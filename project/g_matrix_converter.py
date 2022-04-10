import numpy as np


def g_converter(x, y):
    g = np.array([[x[0, 0], x[0, 1], x[0, 2], y[0, 0]], [x[1, 0], x[1, 1], x[1, 2], y[1, 0]], [
        x[2, 0], x[2, 1], x[2, 2], y[2, 0]], [0, 0, 0, 1]])
    return g
