import numpy as np


def trans_matrix(w, q, theta):
    t = theta
    I = np.identity(3)
    w_hat = np.array([[0, -w[2], w[1]],
                      [w[2], 0, -w[0]], [-w[1], w[0], 0]])
    R = I+(w_hat*np.sin(t))+(np.matmul(w_hat, w_hat)*(1-np.cos(t)))
    a = (I-R)
    transform = np.matmul(a, q)
    trans_matrix = np.array([[R[0, 0], R[0, 1], R[0, 2], transform[0]], [
                            R[1, 0], R[1, 1], R[1, 2], transform[1]], [R[2, 0], R[2, 1], R[2, 2], transform[2]], [0, 0, 0, 1]])
    return(trans_matrix)
