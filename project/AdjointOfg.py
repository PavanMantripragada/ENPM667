import numpy as np
from numpy.linalg import inv


def Adjoint(g):
    # g is a 4x4 matrix consisting of the Rotational matrix and postion vector, import as a list
    # Extracting Roational matrix
    g = np.array(g)
    R = g[:3, :3]
    p = g[:3, 3]
    p_hat = np.array([[0, -p[2], p[1]],
                      [p[2], 0, -p[0]], [-p[1], p[0], 0]])
    pR = np.matmul(p_hat, R)
    Adj = np.array([[R[0, 0], R[0, 1], R[0, 2], pR[0, 0], pR[0, 1], pR[0, 2]], [
        R[1, 0], R[1, 1], R[1, 2], pR[1, 0], pR[1, 1], pR[1, 2]], [R[2, 0], R[2, 1], R[2, 2], pR[2, 0], pR[2, 1], pR[2, 2]], [0, 0, 0, R[0, 0], R[0, 1], R[0, 2]], [0, 0, 0, R[1, 0], R[1, 1], R[1, 2]], [0, 0, 0, R[2, 0], R[2, 1], R[2, 2]]])
    return(Adj)
